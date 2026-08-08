#!/usr/bin/env python3
"""
lint_canon.py — Project Elysium canon integrity checker.

Enforces the obligations in docs/charter/CANON_RULES.md:
  1. Every JSON dataset parses and declares schemaVersion / dataVersion.
  2. Every Markdown document in docs/ carries a Document ID / Status / Version header.
  3. Every entity ID is unique across the whole data layer.
  4. Every ID referenced by a dataset resolves to a defined entity (no dangling refs).
  5. Canonical totals agree across documents (land, ocean, biome and land-use sums).

Run from the repository root:  python3 tools/lint_canon.py
Exit code 0 = clean, 1 = violations found.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

# Reference fields and symbolic values are defined once, in
# tools/reference-fields.json, and read by both this linter and the Atlas
# data pipeline so the two cannot drift.
REF_FIELDS: set[str] = set(
    json.loads((ROOT / "tools" / "reference-fields.json").read_text())["fields"]
)

# IDs that are deliberately symbolic rather than entity references.
SYMBOLIC = set(
    json.loads((ROOT / "tools" / "reference-fields.json").read_text())["symbolic"]
)

# Fields holding a dataset filename rather than an entity ID.
DATASET_FIELDS: set[str] = set(
    json.loads((ROOT / "tools" / "reference-fields.json").read_text())["datasetFields"]
)

errors: list[str] = []
warnings: list[str] = []


def walk(node, fn):
    if isinstance(node, dict):
        fn(node)
        for value in node.values():
            walk(value, fn)
    elif isinstance(node, list):
        for item in node:
            walk(item, fn)


def load_datasets() -> dict[str, dict]:
    datasets = {}
    for path in sorted(DATA.glob("*.json")):
        try:
            datasets[path.name] = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON — {exc}")
    return datasets


def check_envelopes(datasets: dict[str, dict]) -> set[str]:
    defined: set[str] = set()
    for name, doc in datasets.items():
        for field in ("schemaVersion", "dataVersion", "id", "sources"):
            if field not in doc:
                errors.append(f"{name}: missing top-level '{field}'")

        def collect(node: dict):
            ident = node.get("id")
            if isinstance(ident, str):
                if ident in defined:
                    errors.append(f"{name}: duplicate entity id '{ident}'")
                defined.add(ident)

        walk(doc, collect)
    return defined


def check_references(datasets: dict[str, dict], defined: set[str]) -> None:
    def check(node: dict):
        for field, value in node.items():
            if field in DATASET_FIELDS:
                for name in (value if isinstance(value, list) else [value]):
                    if isinstance(name, str) and not (DATA / name).exists():
                        errors.append(f"{name_} : dataset '{name}' in '{field}' does not exist")
                continue
            if field not in REF_FIELDS:
                continue
            values = value if isinstance(value, list) else [value]
            for ref in values:
                if not isinstance(ref, str) or ref in SYMBOLIC:
                    continue
                if ref not in defined:
                    errors.append(f"{name}: dangling reference '{ref}' in field '{field}'")

    for name_, doc in datasets.items():
        walk(doc, check)


def check_markdown() -> None:
    pattern = re.compile(
        r"\*\*Document ID:\*\* `[a-z0-9.\-]+`.*?"
        r"\*\*Status:\*\*.*?"
        r"\*\*Version:\*\* \d+\.\d+\.\d+",
        re.S,
    )
    for path in sorted(DOCS.rglob("*.md")):
        if not pattern.search(path.read_text()):
            errors.append(f"{path.relative_to(ROOT)}: missing or malformed canon header")


def approx(a: float, b: float, tol: float = 0.15) -> bool:
    return abs(a - b) <= tol


def check_totals(datasets: dict[str, dict]) -> None:
    continents = datasets.get("continents.json")
    biomes = datasets.get("biomes.json")
    physical = datasets.get("planet-physical.json")
    if not (continents and biomes and physical):
        warnings.append("totals check skipped — required datasets absent")
        return

    land_from_continents = sum(c["areaMkm2"] for c in continents["continents"])
    totals = biomes["totals"]

    if not approx(land_from_continents, totals["landAreaMkm2"]):
        errors.append(
            f"land area mismatch: continents.json sums to {land_from_continents:.2f} "
            f"but biomes.json declares {totals['landAreaMkm2']}"
        )

    radius = physical["planet"]["meanRadiusKm"]
    surface = 4 * 3.141592653589793 * radius**2 / 1e6
    if not approx(surface, totals["surfaceAreaMkm2"], tol=1.0):
        errors.append(
            f"surface area mismatch: r={radius} km implies {surface:.1f} M km^2, "
            f"biomes.json declares {totals['surfaceAreaMkm2']}"
        )

    land_fraction = physical["planet"]["landFraction"]
    if not approx(surface * land_fraction, totals["landAreaMkm2"], tol=1.0):
        errors.append("land fraction in planet-physical.json disagrees with declared land area")

    if not approx(totals["landAreaMkm2"] + totals["oceanAreaMkm2"], totals["surfaceAreaMkm2"], tol=1.0):
        errors.append("land + ocean does not equal surface area in biomes.json")

    biome_sum = sum(b["areaMkm2"] for b in biomes["terrestrialBiomes"])
    if not approx(biome_sum, totals["landAreaMkm2"]):
        errors.append(f"terrestrial biomes sum to {biome_sum:.2f}, expected {totals['landAreaMkm2']}")

    marine_sum = sum(b["areaMkm2"] for b in biomes["marineRealms"])
    if not approx(marine_sum, totals["oceanAreaMkm2"], tol=0.5):
        errors.append(f"marine realms sum to {marine_sum:.2f}, expected {totals['oceanAreaMkm2']}")

    land_use = sum(v["sharePct"] for v in biomes["landUse"].values())
    if not approx(land_use, 100.0, tol=0.1):
        errors.append(f"land-use shares sum to {land_use:.2f}%, expected 100%")

    for key, entry in biomes["landUse"].items():
        implied = totals["landAreaMkm2"] * entry["sharePct"] / 100
        if not approx(implied, entry["areaMkm2"], tol=0.2):
            errors.append(f"landUse.{key}: {entry['sharePct']}% implies {implied:.2f} M km^2, declared {entry['areaMkm2']}")


def check_demographics(datasets: dict[str, dict]) -> None:
    demo = datasets.get("demographics.json")
    langs = datasets.get("languages.json")
    if not demo:
        warnings.append("demographics check skipped — dataset absent")
        return

    total = demo["population"]["total"]
    by_region = sum(r["population"] for r in demo["populationByRegion"])
    if by_region != total:
        errors.append(f"population by region sums to {by_region}, declared total is {total}")

    share_sets = [
        ("populationByRegion", [r["sharePct"] for r in demo["populationByRegion"]]),
        ("ageStructure", [a["sharePct"] for a in demo["ageStructure"]]),
        ("households.types", [h["sharePct"] for h in demo["households"]["types"]]),
    ]
    if langs:
        share_sets.append(("belief", [b["sharePct"] for b in langs["belief"]]))

    for label, shares in share_sets:
        if not approx(sum(shares), 100.0, tol=0.1):
            errors.append(f"{label} shares sum to {sum(shares):.2f}%, expected 100%")

    for region in demo["populationByRegion"]:
        if "sharePct" not in region:
            continue
        implied = total * region["sharePct"] / 100
        if abs(implied - region["population"]) > total * 0.002:
            errors.append(
                f"{region['id']}: {region['sharePct']}% implies {implied:,.0f} "
                f"but population is {region['population']:,}"
            )

    if langs:
        l1 = sum(f["l1Speakers"] for f in langs["families"])
        if l1 > total:
            errors.append(f"first-language speakers ({l1:,}) exceed total population ({total:,})")
        l2 = langs["concordial"]["l2Speakers"]
        implied_share = 100 * l2 / total
        if not approx(implied_share, langs["concordial"]["l2SharePct"], tol=0.5):
            errors.append(
                f"Concordial L2 share {langs['concordial']['l2SharePct']}% disagrees "
                f"with {l2:,} of {total:,} ({implied_share:.1f}%)"
            )


def check_regions(datasets: dict[str, dict]) -> None:
    """Regional populations must reconcile to the demographic totals."""
    regions = datasets.get("regions.json")
    demo = datasets.get("demographics.json")
    if not (regions and demo):
        warnings.append("regions check skipped — required datasets absent")
        return

    declared_total = demo["population"]["total"]
    region_total = sum(r["population"] for r in regions["regions"])
    if region_total != declared_total:
        errors.append(
            f"Regions sum to {region_total:,} but demographics declares {declared_total:,}"
        )

    if len(regions["regions"]) != regions["tiers"][1]["count"]:
        errors.append(
            f"{len(regions['regions'])} Regions defined but tier count says "
            f"{regions['tiers'][1]['count']}"
        )

    # Each continent's Regions must sum to its demographic population.
    by_continent: dict[str, int] = {}
    for region in regions["regions"]:
        for parent in region.get("regions", []):
            by_continent[parent] = by_continent.get(parent, 0) + region["population"]

    demo_by_continent = {
        parent: entry["population"]
        for entry in demo["populationByRegion"]
        for parent in entry.get("regions", [])
    }
    for parent, total in by_continent.items():
        expected = demo_by_continent.get(parent)
        if expected is not None and total != expected:
            errors.append(
                f"{parent}: Regions sum to {total:,}, demographics declares {expected:,}"
            )

    # Governing-form and delegate-method tallies must match the Regions themselves.
    for field, collection in (
        ("governingForm", "governingForms"),
        ("delegateSelection", "delegateSelectionMethods"),
    ):
        actual: dict[str, int] = {}
        for region in regions["regions"]:
            actual[region[field]] = actual.get(region[field], 0) + 1
        for entry in regions[collection]:
            claimed = entry["regionCount"]
            found = actual.get(entry["id"], 0)
            if claimed != found:
                errors.append(
                    f"{entry['id']}: claims {claimed} Regions but {found} reference it"
                )


def check_justice(datasets: dict[str, dict]) -> None:
    """Court counts and regional tallies must match the government tiers."""
    justice = datasets.get("justice.json")
    regions = datasets.get("regions.json")
    if not (justice and regions):
        warnings.append("justice check skipped — required datasets absent")
        return

    tier_counts = {tier["name"]: tier["count"] for tier in regions["tiers"]}
    expectations = [
        ("law.mediation-house", tier_counts["Commune"], "Communes"),
        ("law.regional-appeal", tier_counts["Region"], "Regions"),
    ]
    courts = {court["id"]: court for court in justice["courts"]}
    for court_id, expected, label in expectations:
        actual = courts[court_id]["count"]
        if actual != expected:
            errors.append(f"{court_id}: {actual} courts but there are {expected} {label}")

    if courts["law.district-court"]["systems"] != tier_counts["District"]:
        errors.append("law.district-court: system count does not match the District tier")

    method_total = sum(m["regionCount"] for m in justice["judiciary"]["regionalAppointmentMethods"])
    if method_total != tier_counts["Region"]:
        errors.append(
            f"judicial appointment methods cover {method_total} Regions, expected {tier_counts['Region']}"
        )

    bands = [b["band"] for b in justice["offenceBands"]]
    if bands != sorted(bands) or len(set(bands)) != len(bands):
        errors.append("offence bands are not a strict ascending sequence")

    max_band = max(justice["offenceBands"], key=lambda b: b["band"])
    if max_band["maxCustodyEY"] != justice["criminalLaw"]["maximumSentenceEY"]:
        errors.append("highest offence band does not match the declared maximum sentence")


def check_public_safety(datasets: dict[str, dict]) -> None:
    """Per-100k rates must reconcile with the declared population."""
    safety = datasets.get("public-safety.json")
    demo = datasets.get("demographics.json")
    regions = datasets.get("regions.json")
    if not (safety and demo):
        warnings.append("public safety check skipped — required datasets absent")
        return

    population = demo["population"]["total"]

    def rate_matches(absolute: float, rate: float, tolerance: float = 0.01) -> bool:
        implied = population / 100_000 * rate
        return abs(implied - absolute) <= max(implied * tolerance, 1)

    for service in safety["services"]:
        if "strength" in service and "ratePer100k" in service:
            if not rate_matches(service["strength"], service["ratePer100k"]):
                errors.append(
                    f"{service['id']}: strength {service['strength']:,} does not match "
                    f"{service['ratePer100k']} per 100,000 of {population:,}"
                )

    custody = safety["custody"]
    if not rate_matches(custody["detainedPopulation"], custody["ratePer100k"]):
        errors.append("custody: detained population does not match the declared rate")

    implied_remand = custody["detainedPopulation"] * custody["remandSharePct"] / 100
    if abs(implied_remand - custody["remandPopulation"]) > 1000:
        errors.append("custody: remand population does not match the remand share")

    force = safety["useOfForce"]
    if not rate_matches(force["homicidesPerYear"], force["homicideRatePer100k"]):
        errors.append("useOfForce: homicide count does not match the declared rate")

    if force["deathsRoutedToPoliceInError"] > force["deathsFollowingPoliceContactPerYear"]:
        errors.append("useOfForce: misrouted deaths exceed total deaths following police contact")

    if custody["maxResidentsPerFacility"] * custody["facilities"] < custody["detainedPopulation"]:
        errors.append("custody: facility capacity is below the detained population")

    if regions:
        region_count = regions["tiers"][1]["count"]
        for body in safety["oversight"]:
            if body["id"] == "law.police-conduct-office" and body["count"] != region_count:
                errors.append(
                    f"law.police-conduct-office: {body['count']} offices but {region_count} Regions"
                )

    # Restorative disposal must beat conventional on every published measure.
    for outcome in safety["restorativeJustice"]["outcomes"]:
        if outcome["restorativePct"] == outcome["conventionalPct"]:
            warnings.append(f"{outcome['id']}: restorative and conventional figures are identical")


def check_economy(datasets: dict[str, dict]) -> None:
    """Economic shares must sum and aggregates must reconcile with population."""
    econ = datasets.get("economy.json")
    demo = datasets.get("demographics.json")
    if not econ:
        warnings.append("economy check skipped — dataset absent")
        return

    aggregates = econ["aggregates"]

    if demo:
        population = demo["population"]["total"]
        if aggregates["population"] != population:
            errors.append(
                f"economy declares population {aggregates['population']:,}, "
                f"demographics says {population:,}"
            )
        implied = aggregates["perCapita"] * population
        if abs(implied - aggregates["grossConcordProduct"]) > implied * 0.005:
            errors.append(
                "grossConcordProduct does not equal perCapita times population"
            )

    tax_shares = sum(tax["revenueSharePct"] for tax in econ["taxes"])
    if not approx(tax_shares, 100.0, tol=0.1):
        errors.append(f"tax revenue shares sum to {tax_shares:.1f}%, expected 100%")

    ownership = sum(f["employmentSharePct"] for f in econ["ownershipForms"])
    if not approx(ownership, 100.0, tol=0.1):
        errors.append(f"ownership employment shares sum to {ownership:.1f}%, expected 100%")

    tiers = sum(econ["revenueByTier"].values())
    if not approx(tiers, 100.0, tol=0.1):
        errors.append(f"revenueByTier sums to {tiers:.1f}%, expected 100%")

    equal = econ["fiscalEqualization"]
    if equal["netContributorRegions"] + equal["netRecipientRegions"] != 34:
        errors.append("equalization contributor and recipient Regions do not sum to 34")
    if equal["incomeRatioPostTransfer"] >= equal["incomeRatioPreTransfer"]:
        errors.append("equalization does not reduce the interregional income ratio")

    if aggregates["giniPostTaxTransfer"] >= aggregates["giniPreTaxTransfer"]:
        errors.append("post-transfer Gini is not below pre-transfer Gini")

    if aggregates["publicSpendingSharePct"] < aggregates["taxTakeSharePct"]:
        pass  # a deficit is permitted; borrowing rules are separate
    fallow = econ["labour"]["fallowEntitlement"]
    if not (fallow["takeUpLowEarnersPct"] <= fallow["takeUpPct"] <= fallow["takeUpHighEarnersPct"]):
        errors.append("fallow take-up rates are not ordered low <= overall <= high")


def check_industry(datasets: dict[str, dict]) -> None:
    """Sector shares, labour force, and concentration figures must reconcile."""
    ind = datasets.get("industry.json")
    econ = datasets.get("economy.json")
    regions = datasets.get("regions.json")
    if not ind:
        warnings.append("industry check skipped — dataset absent")
        return

    for field, label in (("gcpSharePct", "GCP"), ("employmentSharePct", "employment")):
        total = sum(sector[field] for sector in ind["sectors"])
        if not approx(total, 100.0, tol=0.1):
            errors.append(f"sector {label} shares sum to {total:.1f}%, expected 100%")

    force = ind["labourForce"]
    employment_sum = sum(sector["employment"] for sector in ind["sectors"])
    if abs(employment_sum - force["total"]) > force["total"] * 0.005:
        errors.append(
            f"sector employment sums to {employment_sum:,}, labour force is {force['total']:,}"
        )

    implied_employed = force["total"] * (1 - force["unemploymentPct"] / 100)
    if abs(implied_employed - force["employed"]) > force["total"] * 0.005:
        errors.append("employed count does not match labour force minus unemployment")

    implied_public = force["total"] * force["publicServantSharePct"] / 100
    if abs(implied_public - force["publicServants"]) > force["total"] * 0.005:
        errors.append("public servant count does not match the declared labour-force share")

    if regions:
        declared = regions["civilService"]["totalPublicServants"]
        if declared != force["publicServants"]:
            errors.append(
                f"regions.json declares {declared:,} public servants, "
                f"industry.json says {force['publicServants']:,}"
            )

    if econ:
        if force["unemploymentPct"] != econ["aggregates"]["unemploymentPct"]:
            errors.append("unemployment rate disagrees between economy.json and industry.json")
        inequality = ind["inequality"]
        aggregates = econ["aggregates"]
        for key, other in (
            ("incomeGiniPreTaxTransfer", "giniPreTaxTransfer"),
            ("incomeGiniPostTaxTransfer", "giniPostTaxTransfer"),
        ):
            if inequality[key] != aggregates[other]:
                errors.append(f"{key} disagrees between economy.json and industry.json")
        if inequality["interregionalIncomeRatioPostTransfer"] != econ["fiscalEqualization"]["incomeRatioPostTransfer"]:
            errors.append("interregional income ratio disagrees between economy.json and industry.json")

    inequality = ind["inequality"]
    if inequality["wealthGini"] <= inequality["incomeGiniPostTaxTransfer"]:
        errors.append("wealth Gini is not above post-transfer income Gini")
    if inequality["top10PctWealthSharePct"] < inequality["top1PctWealthSharePct"]:
        errors.append("top 10% wealth share is below the top 1% share")

    modal = ind["logistics"]["modalSharePct"]
    if not approx(sum(modal.values()), 100.0, tol=0.1):
        errors.append(f"freight modal shares sum to {sum(modal.values())}%, expected 100%")

    thresholds = [x["marketSharePct"] for x in ind["concentrationRegime"]["thresholds"]]
    if thresholds != sorted(thresholds):
        errors.append("concentration thresholds are not in ascending order")


def check_energy(datasets: dict[str, dict]) -> None:
    """Generation mix, storage, and renewable use must reconcile with resources."""
    energy = datasets.get("energy.json")
    resources = datasets.get("resources.json")
    if not energy:
        warnings.append("energy check skipped — dataset absent")
        return

    demand = energy["demand"]["meanPlanetaryTW"]
    mix = energy["generationMix"]

    shares = sum(source["sharePct"] for source in mix)
    if not approx(shares, 100.0, tol=0.1):
        errors.append(f"generation mix shares sum to {shares:.1f}%, expected 100%")

    output = sum(source["outputTW"] for source in mix)
    if abs(output - demand) > demand * 0.01:
        errors.append(f"generation mix outputs sum to {output:.2f} TW, demand is {demand} TW")

    for source in mix:
        implied = demand * source["sharePct"] / 100
        if abs(implied - source["outputTW"]) > max(implied * 0.02, 0.01):
            errors.append(f"{source['id']}: output does not match its declared share of demand")

    # No source may exceed the technical potential canonized in Phase 2B.
    if resources:
        potentials = {
            entry["id"]: entry["technicalPotentialTW"]
            for entry in resources["renewablePotential"]
        }
        for source in mix:
            resource = source.get("resource")
            if not resource:
                continue
            if resource not in potentials:
                errors.append(f"{source['id']}: unknown renewable resource '{resource}'")
                continue
            potential = potentials[resource]
            if source["outputTW"] > potential:
                errors.append(
                    f"{source['id']}: {source['outputTW']} TW exceeds the "
                    f"{potential} TW technical potential of {resource}"
                )
            implied_share = 100 * source["outputTW"] / potential
            if not approx(implied_share, source["shareOfTechnicalPotentialPct"], tol=0.5):
                errors.append(
                    f"{source['id']}: shareOfTechnicalPotentialPct disagrees with "
                    f"output over potential ({implied_share:.1f}%)"
                )

    storage_shares = sum(m["capacitySharePct"] for m in energy["storage"]["media"])
    if not approx(storage_shares, 100.0, tol=0.1):
        errors.append(f"storage capacity shares sum to {storage_shares:.1f}%, expected 100%")

    cover = energy["storage"]["totalTWh"] / demand  # TWh over TW gives hours
    if abs(cover - energy["storage"]["planetaryCoverCivilHours"]) > 1.0:
        errors.append("storage cover hours do not match total storage over mean demand")

    grid = energy["grid"]
    if grid["currentReserveMarginPct"] < grid["statutoryReserveMarginPct"]:
        errors.append("current reserve margin is below the statutory minimum")

    fusion = energy["fusion"]
    implied_fusion = fusion["plants"] * fusion["meanCapacityGW"] / 1000
    if abs(implied_fusion - fusion["totalOutputTW"]) > fusion["totalOutputTW"] * 0.02:
        errors.append("fusion fleet capacity does not match plants times mean capacity")


def check_environment(datasets: dict[str, dict]) -> None:
    """Protection, restoration, carbon and biodiversity must reconcile with Phase 2B."""
    env = datasets.get("environment.json")
    biomes = datasets.get("biomes.json")
    energy = datasets.get("energy.json")
    physical = datasets.get("planet-physical.json")
    if not env:
        warnings.append("environment check skipped — dataset absent")
        return

    protection = env["protection"]
    for field, declared in (("landMkm2", protection["landProtectedMkm2"]),
                            ("oceanMkm2", protection["oceanProtectedMkm2"])):
        total = sum(tier[field] for tier in env["protectionTiers"])
        if not approx(total, declared, tol=0.05):
            errors.append(
                f"protection tiers sum to {total:.2f} for {field}, declared {declared}"
            )

    if biomes:
        canon = biomes["protection"]
        for ours, theirs in (("landProtectedMkm2", "landProtectedMkm2"),
                             ("oceanProtectedMkm2", "oceanProtectedMkm2"),
                             ("landProtectedSharePct", "landProtectedSharePct"),
                             ("oceanProtectedSharePct", "oceanProtectedSharePct")):
            if protection[ours] != canon[theirs]:
                errors.append(f"protection.{ours} disagrees with biomes.json")

        land_use = biomes["landUse"]["restorationInProgress"]
        restoration = env["restoration"]
        if restoration["totalMkm2"] != land_use["areaMkm2"]:
            errors.append("restoration total disagrees with the land-use restoration area")
        if restoration["shareOfLandPct"] != land_use["sharePct"]:
            errors.append("restoration share disagrees with the land-use restoration share")

        bio = env["biodiversity"]
        canon_bio = biomes["biodiversity"]
        for ours, theirs in (("describedSpecies", "describedMulticellularSpecies"),
                             ("industrialEraExtinctions", "industrialEraExtinctions"),
                             ("activeRecoveryProgrammes", "activeRecoveryProgrammes"),
                             ("extinctInWildPreserved", "extinctInWildPreserved")):
            if bio[ours] != canon_bio[theirs]:
                errors.append(f"biodiversity.{ours} disagrees with biomes.json")

    programmes = sum(p["areaMkm2"] for p in env["restoration"]["programmes"])
    if not approx(programmes, env["restoration"]["totalMkm2"], tol=0.05):
        errors.append(
            f"restoration programmes sum to {programmes:.2f}, total declares "
            f"{env['restoration']['totalMkm2']}"
        )

    account = env["carbonAccount"]
    removal = sum(m["annualGt"] for m in account["removalMethods"])
    if not approx(removal, account["removalGt"], tol=0.01):
        errors.append(f"removal methods sum to {removal:.2f} Gt, declared {account['removalGt']}")

    net = account["grossResidualEmissionsGt"] - account["removalGt"]
    if not approx(net, account["netPositionGt"], tol=0.01):
        errors.append("net carbon position does not equal emissions minus removal")

    low, high = account["corridorPpm"]
    if not low <= account["currentCo2Ppm"] <= high:
        errors.append("current CO2 is outside the declared constitutional corridor")

    if physical:
        atmosphere = json.dumps(physical)
        if str(account["currentCo2Ppm"]) not in atmosphere:
            warnings.append("planet-physical.json does not state the current CO2 figure")

    if energy:
        dac = next(m for m in account["removalMethods"] if m["id"] == "env.removal-dac")
        demand = energy["demand"]["meanPlanetaryTW"]
        implied = 100 * dac["energyTW"] / demand
        if not approx(implied, dac["shareOfPlanetaryEnergyPct"], tol=0.05):
            errors.append("direct air capture energy share disagrees with planetary demand")

    watch = env["overturningWatch"]
    if watch["currentStrengthPct"] <= watch["emergencyTriggerPct"]:
        errors.append("overturning strength is at or below the emergency trigger")
    if watch["longEmergencyTroughPct"] >= watch["currentStrengthPct"]:
        errors.append("Long Emergency overturning trough is not below the current value")

    sea = env["seaLevel"]
    if sea["riseAbovePreIndustrialM"] > sea["cryosphericBudgetM"]:
        errors.append("sea-level rise exceeds the total cryospheric budget")
    if sea["committedRiseRemainingM"] > sea["committedRiseTotalM"]:
        errors.append("remaining committed rise exceeds the total commitment")


def check_education(datasets: dict[str, dict]) -> None:
    """Enrolment must reconcile with demographics, institutions with tiers."""
    edu = datasets.get("education.json")
    demo = datasets.get("demographics.json")
    regions = datasets.get("regions.json")
    econ = datasets.get("economy.json")
    if not edu:
        warnings.append("education check skipped — dataset absent")
        return

    schooling = edu["schooling"]
    staged = sum(
        stage["enrolment"] for stage in edu["stages"]
        if "enrolment" in stage and stage["id"] != "edu.stage-post-secondary"
    )
    if abs(staged - schooling["totalInSchool"]) > schooling["totalInSchool"] * 0.005:
        errors.append(
            f"school stages sum to {staged:,}, totalInSchool declares "
            f"{schooling['totalInSchool']:,}"
        )

    if demo:
        population = demo["population"]["total"]
        minors = next(
            band for band in demo["ageStructure"] if band["id"] == "demo.age-minor"
        )
        minor_count = population * minors["sharePct"] / 100
        if schooling["totalInSchool"] > minor_count:
            errors.append("more pupils in school than there are minors in the population")

        implied = 100 * schooling["totalInSchool"] / population
        if not approx(implied, schooling["shareOfPopulationPct"], tol=0.1):
            errors.append("school share of population does not match the enrolment figure")

        # Stage age bands must lie inside the minor age band, and not overlap.
        bounded = [s for s in edu["stages"] if "maxAgeEY" in s]
        bounded.sort(key=lambda s: s["minAgeEY"])
        for earlier, later in zip(bounded, bounded[1:]):
            if earlier["maxAgeEY"] != later["minAgeEY"]:
                errors.append(
                    f"school stages {earlier['id']} and {later['id']} do not meet cleanly"
                )
        if bounded[-1]["maxAgeEY"] != demo["species"]["legalMajorityEY"]:
            errors.append("upper school does not end at legal majority")

    if regions:
        communes = next(t for t in regions["tiers"] if t["name"] == "Commune")["count"]
        for entry in edu["institutions"]:
            if entry["id"] == "edu.commune-learning-centres" and entry["count"] != communes:
                errors.append("Commune learning centres do not match the Commune count")
        if edu["libraries"]["total"] < communes:
            errors.append("fewer libraries than Communes, but canon promises one in every Commune")

    if econ:
        retraining = edu["adultLearning"]["inSubstantialRetraining"]
        share = econ["labour"]["workforceInSubstantialRetrainingPct"]
        # Labour force lives in industry.json; recompute only if available.
        industry = datasets.get("industry.json")
        if industry:
            implied = industry["labourForce"]["total"] * share / 100
            if abs(implied - retraining) > implied * 0.02:
                errors.append(
                    "retraining headcount does not match the declared workforce share"
                )

    account = edu["entitlementAccount"]
    if account["takeUpLowEarnersYears"] > account["takeUpHighEarnersYears"]:
        errors.append("entitlement take-up is not ordered low <= high")
    if account["takeUpHighEarnersYears"] > account["yearsGranted"]:
        errors.append("entitlement take-up exceeds the years granted")
    if account["grantedAtAgeEY"] != demo["species"]["legalMajorityEY"] if demo else False:
        errors.append("entitlement is not granted at legal majority")


def check_research(datasets: dict[str, dict]) -> None:
    """Research funding, scale, and science figures must reconcile."""
    res = datasets.get("research.json")
    econ = datasets.get("economy.json")
    industry = datasets.get("industry.json")
    edu = datasets.get("education.json")
    demo = datasets.get("demographics.json")
    if not res:
        warnings.append("research check skipped — dataset absent")
        return

    shares = sum(entry["sharePct"] for entry in res["funding"])
    if not approx(shares, 100.0, tol=0.1):
        errors.append(f"research funding shares sum to {shares:.1f}%, expected 100%")

    scale = res["scale"]
    if econ:
        gcp = econ["aggregates"]["grossConcordProduct"]
        implied = gcp * scale["rdShareOfGcpPct"] / 100
        if abs(implied - scale["rdSpendingDram"]) > implied * 0.02:
            errors.append("R&D spending does not match its declared share of GCP")

        replication = next(
            p for p in res["integrityPractices"] if p["id"] == "res.replication-line"
        )
        implied_line = scale["rdSpendingDram"] * replication["budgetSharePct"] / 100
        if abs(implied_line - replication["budgetDram"]) > implied_line * 0.02:
            errors.append("replication budget does not match its declared share of R&D")

    if industry:
        sector = next(
            (s for s in industry["sectors"] if s["id"] == "ind.sector-research-technical"),
            None,
        )
        if sector and sector["employment"] != scale["researchEngineeringTechnicalEmployment"]:
            errors.append(
                "research employment disagrees between industry.json and research.json"
            )
        if scale["dedicatedResearchers"] > scale["researchEngineeringTechnicalEmployment"]:
            errors.append("dedicated researchers exceed total research-sector employment")

    if edu:
        for key, entry_id in (("universities", "edu.universities"),
                              ("researchAcademies", "edu.research-academies")):
            declared = next(i["count"] for i in edu["institutions"] if i["id"] == entry_id)
            if scale[key] != declared:
                errors.append(f"{key} disagrees between education.json and research.json")

    astronomy = next(f for f in res["sciences"] if f["id"] == "res.field-astronomy")
    if astronomy["candidateSignalsResolved"] > astronomy["candidateSignalsSinceEY96"]:
        errors.append("more candidate signals resolved than were ever detected")
    if astronomy["contactConfirmed"]:
        errors.append("astronomy claims confirmed contact, which no phase has canonized")

    biology = next(f for f in res["sciences"] if f["id"] == "res.field-biology")
    if biology["escapesContainedWithinSeason"] + biology["persistentEngineeredPopulations"] != biology["escapesSinceEY200"]:
        errors.append("synthetic biology escape outcomes do not sum to total escapes")

    if demo:
        medicine = next(f for f in res["sciences"] if f["id"] == "res.field-medicine")
        species = demo["species"]
        if medicine["maximumVerifiedLifespanEY"] != species["maxVerifiedLifespanEY"]:
            errors.append("maximum lifespan disagrees between demographics.json and research.json")
        if medicine["medianHealthyLifespanNowEY"] != species["medianHealthyLifespanEY"]:
            errors.append("median healthy lifespan disagrees between demographics and research")
        if medicine["medianHealthyLifespanAtFoundingEY"] >= medicine["medianHealthyLifespanNowEY"]:
            errors.append("healthy lifespan at founding is not below the present value")

    programmes = res["centuryProgrammes"]
    if programmes["endedForCost"] != 0:
        errors.append("canon states no century programme has been ended for cost")
    for entry in programmes["named"]:
        if entry["startEY"] > 412:
            errors.append(f"{entry['id']}: start year is after the reference date")


def check_health(datasets: dict[str, dict]) -> None:
    """Health figures must reconcile with demographics, policing, and economy."""
    health = datasets.get("health.json")
    demo = datasets.get("demographics.json")
    regions = datasets.get("regions.json")
    econ = datasets.get("economy.json")
    industry = datasets.get("industry.json")
    safety = datasets.get("public-safety.json")
    if not health:
        warnings.append("health check skipped — dataset absent")
        return

    system = health["system"]
    if econ:
        gcp = econ["aggregates"]["grossConcordProduct"]
        implied = gcp * system["spendingShareOfGcpPct"] / 100
        if abs(implied - system["spendingDram"]) > implied * 0.02:
            errors.append("health spending does not match its declared share of GCP")

    if industry:
        force = industry["labourForce"]["total"]
        implied = force * system["workforceShareOfLabourForcePct"] / 100
        if abs(implied - system["workforce"]) > implied * 0.02:
            errors.append("health workforce does not match its declared labour-force share")

    if regions:
        communes = next(t for t in regions["tiers"] if t["name"] == "Commune")["count"]
        posts = next(f for f in health["facilities"] if f["id"] == "health.commune-post")
        if posts["count"] != communes:
            errors.append("Commune health posts do not match the Commune count")

    if demo:
        geriatrics = health["geriatrics"]
        population = demo["population"]["total"]
        centenarians = next(
            b for b in demo["ageStructure"] if b["id"] == "demo.age-centenarian"
        )
        implied = population * centenarians["sharePct"] / 100
        if abs(implied - geriatrics["populationOver100"]) > implied * 0.02:
            errors.append("over-100 population disagrees with the demographic age structure")

        mortality = demo["mortality"]
        if geriatrics["ageAssociatedDeathSharePct"] != mortality["ageAssociatedDeclineSharePct"]:
            errors.append("age-associated death share disagrees with demographics.json")
        if health["mentalHealth"]["suicideRatePer100k"] != mortality["suicidePer100kPerYear"]:
            errors.append("suicide rate disagrees with demographics.json")
        if geriatrics["frailtyWeightedDependencyRatio"] != demo["frailtyWeightedDependencyRatio"]:
            errors.append("frailty-weighted dependency ratio disagrees with demographics.json")

        substances = health["substanceUse"]
        if substances["minimumAgeEY"] != demo["species"]["legalMajorityEY"]:
            errors.append("substance minimum age does not match legal majority")

    if safety:
        teams = next(
            s for s in safety["services"] if s["id"] == "law.commune-response-teams"
        )
        if teams["armed"]:
            errors.append("Response Teams are armed in public-safety.json but unarmed in health canon")

    decline = health["geriatrics"]["cognitiveDecline"]
    if decline["medianOnsetNowEY"] <= decline["medianOnsetAtFoundingEY"]:
        errors.append("cognitive decline onset has not improved since the founding")
    if decline["preventionExists"] or decline["reversalExists"]:
        errors.append("canon states no prevention and no reversal for late-life cognitive decline")

    emergency = health["emergency"]
    if not (emergency["medianUrbanResponseCivilMinutes"]
            <= emergency["medianRuralResponseCivilMinutes"]
            <= emergency["worstRegionalMedianCivilMinutes"]):
        errors.append("emergency response medians are not ordered urban <= rural <= worst")

    eol = health["endOfLife"]["assistedDying"]
    if eol["lawful"] and not eol["safeguards"]:
        errors.append("assisted dying is lawful but no safeguards are recorded")
    if "canonPosition" not in eol or "objection" not in eol:
        errors.append("assisted dying entry must record both the objection and the canon position")


def check_cities(datasets: dict[str, dict]) -> None:
    """Cities must sit inside their continent, and within their Region's population."""
    cities = datasets.get("cities.json")
    continents = datasets.get("continents.json")
    regions = datasets.get("regions.json")
    demo = datasets.get("demographics.json")
    if not cities:
        warnings.append("cities check skipped — dataset absent")
        return

    # Build a bounding box per continent from its outline geometry.
    bounds: dict[str, tuple[float, float, float, float]] = {}
    if continents:
        for continent in continents["continents"]:
            rings = []
            if "outline" in continent:
                rings.append(continent["outline"])
            for island in continent.get("islandOutlines", []):
                rings.append(island["outline"])
            points = [point for ring in rings for point in ring]
            if not points:
                continue
            lons = [p[0] for p in points]
            lats = [p[1] for p in points]
            bounds[continent["id"]] = (min(lons), max(lons), min(lats), max(lats))

    # Map each Region to its parent continent.
    parent: dict[str, str] = {}
    population: dict[str, int] = {}
    if regions:
        for region in regions["regions"]:
            population[region["id"]] = region["population"]
            for continent in region.get("regions", []):
                parent[region["id"]] = continent

    by_region: dict[str, int] = {}
    for city in cities["cities"]:
        polity = city["polity"]
        coords = city["coordinates"]
        by_region[polity] = by_region.get(polity, 0) + city["population"]

        if not -90 <= coords["lat"] <= 90 or not -180 <= coords["lon"] <= 180:
            errors.append(f"{city['id']}: coordinates out of range")
            continue

        continent = parent.get(polity)
        if continent and continent in bounds:
            lon_min, lon_max, lat_min, lat_max = bounds[continent]
            margin = 3.0  # allow coastal cities slightly outside a coarse outline
            if not (lat_min - margin <= coords["lat"] <= lat_max + margin):
                errors.append(
                    f"{city['id']}: latitude {coords['lat']} lies outside {continent}"
                )
            # Longitude comparison is skipped for antimeridian-spanning continents.
            if lon_max - lon_min < 180 and not (
                lon_min - margin <= coords["lon"] <= lon_max + margin
            ):
                errors.append(
                    f"{city['id']}: longitude {coords['lon']} lies outside {continent}"
                )

    for polity, urban in by_region.items():
        total = population.get(polity)
        if total is not None and urban > total:
            errors.append(
                f"{polity}: named cities hold {urban:,} but the Region has {total:,}"
            )

    settlement = cities["settlement"]
    largest = max(cities["cities"], key=lambda c: c["population"])
    if settlement["largestCity"] != largest["id"]:
        errors.append(
            f"largestCity is {settlement['largestCity']} but {largest['id']} is larger"
        )

    if demo:
        total_population = demo["population"]["total"]
        implied = total_population * settlement["urbanSharePct"] / 100
        if abs(implied - settlement["urbanPopulation"]) > implied * 0.01:
            errors.append("urban population does not match its declared share")
        if settlement["urbanSharePct"] != demo["population"]["urbanizationPct"]:
            errors.append("urban share disagrees with demographics.json")

        households = cities["housing"]["households"]
        implied_households = total_population / cities["housing"]["meanHouseholdSize"]
        if abs(implied_households - households) > implied_households * 0.01:
            errors.append("household count does not match population over mean household size")
        if cities["housing"]["meanHouseholdSize"] != demo["households"]["meanSize"]:
            errors.append("mean household size disagrees with demographics.json")

    tenure = sum(t["sharePct"] for t in cities["housing"]["tenure"])
    if not approx(tenure, 100.0, tol=0.1):
        errors.append(f"housing tenure shares sum to {tenure:.1f}%, expected 100%")

    homeless = cities["housing"]["homelessness"]
    if homeless["rehousedWithin30DaysPct"] + homeless["rehousedWithinSeasonPct"] > 100:
        errors.append("homelessness rehousing shares exceed 100%")


def check_routes(datasets: dict[str, dict]) -> None:
    """Route geometry must connect real cities and match its own stated length."""
    routes = datasets.get("routes.json")
    cities = datasets.get("cities.json")
    industry = datasets.get("industry.json")
    if not routes:
        warnings.append("routes check skipped — dataset absent")
        return

    city_coords = {}
    if cities:
        city_coords = {
            c["id"]: (c["coordinates"]["lat"], c["coordinates"]["lon"])
            for c in cities["cities"]
        }

    def haversine(a, b):
        import math
        la1, lo1 = math.radians(a[0]), math.radians(a[1])
        la2, lo2 = math.radians(b[0]), math.radians(b[1])
        h = (math.sin((la2 - la1) / 2) ** 2
             + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
        return 6510 * 2 * math.asin(math.sqrt(h))

    for route in routes["routes"]:
        path = route["path"]
        if len(path) < 2:
            errors.append(f"{route['id']}: path has fewer than two points")
            continue

        for point in path:
            if not -90 <= point["lat"] <= 90 or not -180 <= point["lon"] <= 180:
                errors.append(f"{route['id']}: path point out of coordinate range")
                break

        # Endpoints must coincide with the first and last named stop.
        if city_coords and route.get("stops"):
            for index, stop in ((0, route["stops"][0]), (-1, route["stops"][-1])):
                if stop not in city_coords:
                    errors.append(f"{route['id']}: unknown stop '{stop}'")
                    continue
                lat, lon = city_coords[stop]
                end = path[index]
                if abs(end["lat"] - lat) > 0.05 or abs(end["lon"] - lon) > 0.05:
                    errors.append(
                        f"{route['id']}: path endpoint does not meet stop '{stop}'"
                    )

        measured = sum(
            haversine((path[i]["lat"], path[i]["lon"]),
                      (path[i + 1]["lat"], path[i + 1]["lon"]))
            for i in range(len(path) - 1)
        )
        if abs(measured - route["lengthKm"]) > max(route["lengthKm"] * 0.02, 5):
            errors.append(
                f"{route['id']}: stated length {route['lengthKm']} km, "
                f"geometry measures {measured:.0f} km"
            )

        if "travelTimeCivilHours" in route:
            implied = route["lengthKm"] / route["serviceSpeedKmh"]
            if abs(implied - route["travelTimeCivilHours"]) > 0.5:
                errors.append(f"{route['id']}: travel time does not match length over speed")

    shares = sum(m["sharePct"] for m in routes["modalShares"]["passengerTrips"])
    if not approx(shares, 100.0, tol=0.1):
        errors.append(f"passenger modal shares sum to {shares:.1f}%, expected 100%")

    freight = routes["modalShares"]["freightTonneKm"]
    if not approx(sum(freight.values()), 100.0, tol=0.1):
        errors.append("freight modal shares do not sum to 100%")

    if industry:
        canon = industry["logistics"]["modalSharePct"]
        for key in ("railAndMaglev", "sea", "road", "air"):
            if freight[key] != canon[key]:
                errors.append(f"freight share '{key}' disagrees with industry.json")

    launch = routes["launchRanges"]
    if not approx(sum(r["capacitySharePct"] for r in launch), 100.0, tol=0.1):
        errors.append("launch capacity shares do not sum to 100%")
    cap = routes["launchPolicy"]["maxSingleRangeCapacityPct"]
    for site in launch:
        if site["capacitySharePct"] > cap:
            errors.append(f"{site['id']} exceeds the {cap}% single-range capacity cap")

    urban = routes["urbanMobility"]
    if urban["transitFareFreeRegions"] > urban["transitFareFreeOfRegions"]:
        errors.append("more fare-free Regions than Regions exist")


def check_agriculture(datasets: dict[str, dict]) -> None:
    """Food figures must reconcile with land use, resources, and fisheries canon."""
    agri = datasets.get("agriculture.json")
    biomes = datasets.get("biomes.json")
    resources = datasets.get("resources.json")
    industry = datasets.get("industry.json")
    energy = datasets.get("energy.json")
    if not agri:
        warnings.append("agriculture check skipped — dataset absent")
        return

    shares = sum(s["caloriesSharePct"] for s in agri["calorieSources"])
    if not approx(shares, 100.0, tol=0.1):
        errors.append(f"calorie shares sum to {shares:.1f}%, expected 100%")

    if biomes:
        cultivated = biomes["landUse"]["cultivated"]["areaMkm2"]
        field = next(s for s in agri["calorieSources"] if s["id"] == "agri.source-field")
        if abs(field["landMkm2"] - cultivated) > 0.05:
            errors.append(
                f"field agriculture uses {field['landMkm2']} M km^2 but biomes.json "
                f"declares {cultivated} M km^2 cultivated"
            )
        land_total = sum(s["landMkm2"] for s in agri["calorieSources"])
        if land_total > biomes["totals"]["landAreaMkm2"]:
            errors.append("agricultural land exceeds total land area")

    fisheries = agri["fisheries"]
    if fisheries["wildCaptureMt"] + fisheries["aquacultureMt"] != fisheries["totalHarvestMt"]:
        errors.append("wild capture plus aquaculture does not equal total marine harvest")
    if resources:
        canon_harvest = resources["biologicalMaterials"]["marineHarvestMtPerYear"]
        if fisheries["totalHarvestMt"] != canon_harvest:
            errors.append("marine harvest disagrees with resources.json")

        phosphorus = next(m for m in resources["materials"] if m["id"] == "resource.phosphorus")
        ours = agri["nutrients"]["phosphorus"]
        if ours["recoveryRatePct"] / 100 != phosphorus["recoveryRate"]:
            errors.append("phosphorus recovery rate disagrees with resources.json")
        if ours["horizonYears"] != phosphorus["reserveHorizonYears"]:
            errors.append("phosphorus horizon disagrees with resources.json")
        if ours["horizonWithoutRecoveryYears"] != phosphorus["horizonWithoutRecoveryYears"]:
            errors.append("phosphorus no-recovery horizon disagrees with resources.json")

    if industry:
        sector = next(
            (s for s in industry["sectors"] if s["id"] == "ind.sector-agriculture"), None
        )
        if sector and sector["employment"] != agri["fieldAgriculture"]["employment"]:
            errors.append("agriculture employment disagrees with industry.json")

    if energy:
        cea = agri["controlledEnvironment"]
        demand = energy["demand"]["meanPlanetaryTW"]
        implied = 100 * cea["energyTW"] / demand
        if not approx(implied, cea["shareOfGenerationPct"], tol=0.1):
            errors.append("controlled-environment energy share disagrees with planetary demand")

    reserves = agri["reserves"]
    tier_total = sum(t["months"] for t in reserves["tiers"])
    if tier_total != reserves["totalMonthsOfConsumption"]:
        errors.append(
            f"reserve tiers sum to {tier_total} months, total declares "
            f"{reserves['totalMonthsOfConsumption']}"
        )
    if reserves["floorMonths"] > reserves["reportTriggerMonths"]:
        errors.append("reserve floor exceeds the reporting trigger")
    if reserves["timesBelowFloorEver"] != 0:
        errors.append("canon states the reserve has never fallen below its floor")

    livestock = agri["livestock"]
    if livestock["caloriesSharePct"] >= livestock["preFoundingCaloriesSharePct"]:
        errors.append("livestock share has not fallen since the founding")
    if livestock["declineByProhibition"]:
        errors.append("canon states the livestock decline was not by prohibition")

    afford = agri["affordability"]
    if afford["lowestDecileFoodShareOfIncomePct"] <= afford["medianHouseholdFoodShareOfIncomePct"]:
        errors.append("lowest-decile food share is not above the median")

    if agri["foodAsRight"]["isCharterRight"]:
        errors.append("food is recorded as a Charter right, which gov.constitution does not list")


def check_defence(datasets: dict[str, dict]) -> None:
    """Service strengths, doctrine, and the Abolition must reconcile with canon."""
    defence = datasets.get("defence.json")
    safety = datasets.get("public-safety.json")
    energy = datasets.get("energy.json")
    health = datasets.get("health.json")
    research = datasets.get("research.json")
    if not defence:
        warnings.append("defence check skipped — dataset absent")
        return

    posture = defence["posture"]
    branch_total = sum(b["strength"] for b in defence["branches"])
    if branch_total != posture["totalStrength"]:
        errors.append(
            f"branch strengths sum to {branch_total:,}, total declares "
            f"{posture['totalStrength']:,}"
        )

    corps = next(b for b in defence["branches"] if b["id"] == "mil.response-corps")
    implied = 100 * corps["strength"] / posture["totalStrength"]
    if not approx(implied, corps["shareOfServicePct"], tol=0.2):
        errors.append("Response Corps share does not match its strength")

    if safety:
        police = next(
            s for s in safety["services"] if s["id"] == "law.district-police"
        )
        if posture["policeStrengthForComparison"] != police["strength"]:
            errors.append("police comparison strength disagrees with public-safety.json")
        if posture["totalStrength"] >= police["strength"]:
            errors.append("canon states the Service is smaller than the police")

    if posture["contactedCivilizations"] != 0 or posture["externalEnemyExists"]:
        errors.append("defence posture asserts an external enemy, which no phase has canonized")
    if research:
        astronomy = next(
            f for f in research["sciences"] if f["id"] == "res.field-astronomy"
        )
        if astronomy["contactConfirmed"] != (posture["contactedCivilizations"] > 0):
            errors.append("contact status disagrees between research.json and defence.json")

    reservists = defence["disasterCapability"]["reservists"]
    if reservists > corps["strength"]:
        errors.append("reservists exceed total Response Corps strength")

    if energy:
        plants = energy["fusion"]["plants"]
        accounting = next(
            i for i in defence["abolition"]["instruments"]
            if i["id"] == "mil.abolition-material-accounting"
        )
        if f"{plants:,}" not in accounting["summary"]:
            errors.append("Abolition material accounting does not cite the canonical plant count")

    if health:
        facilities = next(
            f for f in health["facilities"] if f["id"] == "health.concord-facility"
        )
        oversight = next(
            i for i in defence["abolition"]["instruments"]
            if i["id"] == "mil.abolition-pathogen-oversight"
        )
        if str(facilities["count"]) not in oversight["summary"]:
            errors.append("pathogen oversight does not cite the canonical containment facility count")

    abolition = defence["abolition"]
    if abolition["proceedingsConcerningConcealment"] > abolition["formalProceedingsSinceEY34"]:
        errors.append("concealment proceedings exceed total proceedings")
    if abolition["dualUseProblem"]["solvable"]:
        errors.append("canon states the dual-use problem is unsolvable")

    doctrine = defence["disasterDoctrine"]
    if doctrine["cancellationsSinceEY341"] > doctrine["activationsSinceEY341"]:
        errors.append("more protective activations cancelled than initiated")
    if doctrine["cancellationsLaterFoundWrong"] > doctrine["cancellationsSinceEY341"]:
        errors.append("more cancellations found wrong than were made")

    pd = defence["planetaryDefence"]
    if pd["catalogueAbove30mPct"] > pd["catalogueAbove100mPct"]:
        errors.append("30 m catalogue completeness exceeds the 100 m figure")
    if pd["operationalDeflections"] != 1:
        errors.append("canon records exactly one operational deflection")


def check_ai(datasets: dict[str, dict]) -> None:
    """AI canon must agree with the Cassian record and downstream constraints."""
    ai = datasets.get("ai.json")
    timeline = datasets.get("timeline.json")
    demo = datasets.get("demographics.json")
    edu = datasets.get("education.json")
    langs = datasets.get("languages.json")
    if not ai:
        warnings.append("AI check skipped — dataset absent")
        return

    cassian = ai["cassian"]
    if cassian["decisionWindowSeconds"] != 90:
        errors.append("the Cassian decision window is canonized at ninety seconds")
    if not cassian["cleared"]:
        errors.append("canon records the Cassian officer was cleared")
    for field in ("statuesExist",):
        if cassian[field]:
            errors.append("canon records no statue of the Cassian officer exists")
    for field in ("honoursAccepted", "buildingsNamedForHer", "decorationsIssuedInHerName"):
        if cassian[field] != 0:
            errors.append(f"cassian.{field} contradicts the recorded refusal of honours")

    if timeline:
        event = next(
            e for e in timeline["events"] if e["id"] == "hist.event-cassian-incident"
        )
        if event["year"] != -19:
            errors.append("Cassian Incident year disagrees with timeline.json")
        if cassian["originEvent"] != event["id"]:
            errors.append("cassian.originEvent does not point at the timeline event")

    rules = {r["id"]: r for r in ai["cassianRules"]}
    if len(rules) != 4:
        errors.append("canon defines exactly four Cassian Rules")
    rule4 = rules["ai.rule-preserved-refusal"]
    if not 0 <= rule4["complianceInTierAPct"] <= 100:
        errors.append("Rule 4 compliance is out of range")
    if rule4["complianceInTierAPct"] == 100:
        errors.append("canon records Rule 4 compliance as incomplete")

    tier_a = next(t for t in ai["tiers"] if t["id"] == "ai.tier-a")
    if not tier_a["allCassianRulesApply"]:
        errors.append("Tier A must carry all four Cassian Rules")
    for tier in ai["tiers"]:
        if tier["id"] != "ai.tier-a" and tier["allCassianRulesApply"]:
            errors.append(f"{tier['id']} should not carry all four rules")

    if ai["systemsBoard"]["isIndependentOffice"]:
        errors.append("the Charter fixes the Independent Offices at five; the Systems Board is not one")

    assistants = ai["applications"]["publicAssistants"]
    if assistants["engagementOptimisationPermitted"] or assistants["advertisingPermitted"]:
        errors.append("public assistants may not advertise or optimise for engagement")
    if demo:
        population = demo["population"]["total"]
        if assistants["users"] > population:
            errors.append("public assistant users exceed the population")

    medicine = ai["applications"]["medicine"]
    if medicine["treatmentRefusableOnSystemRecommendation"]:
        errors.append("canon forbids refusing treatment on a system recommendation")

    law = ai["applications"]["translationAndLaw"]
    for field in ("adjudicationMayBeAutomated", "assessmentOfEvidenceMayBeAutomated",
                  "sentencingMayBeAutomated"):
        if law[field]:
            errors.append(f"law.{field} contradicts the human-adjudication rule")
    if langs and law["languages"] != langs["totals"]["registeredLanguages"]:
        errors.append("translation language count disagrees with languages.json")

    if edu:
        constraints = {c["id"] for c in edu["aiTutors"]["constraints"]}
        if "edu.ai-no-concealed-uncertainty" not in constraints:
            errors.append("the tutor uncertainty constraint has gone missing from education.json")
        if edu["aiTutors"]["logsAccessibleToSchoolsForAssessment"]:
            errors.append("tutor logs must not be accessible to schools for assessment")

    if ai["moralStatus"]["anySystemRecognisedAsRightsBearer"]:
        errors.append("no phase has canonized recognition of an artificial rights-bearer")
    if ai["moralStatus"]["questionSettled"]:
        errors.append("canon records artificial moral status as an open question")


def check_culture(datasets: dict[str, dict]) -> None:
    """Cultural canon must agree with the calendar, demographics, and media policy."""
    culture = datasets.get("culture.json")
    calendar = datasets.get("calendar.json")
    languages = datasets.get("languages.json")
    demo = datasets.get("demographics.json")
    ai = datasets.get("ai.json")
    if not culture:
        warnings.append("culture check skipped — dataset absent")
        return

    music = culture["music"]
    if calendar:
        if music["defaultMetreBeats"] != calendar["year"]["daysPerWeek"]:
            errors.append("default musical metre does not match the days-per-week")
        if culture["context"]["dayLengthCivilHours"] != calendar["clock"]["hoursPerDay"]:
            errors.append("day length disagrees with calendar.json")

        # Dated festivals must fall inside the calendar.
        months = {m["index"] for m in calendar["months"]}
        days_per_month = calendar["year"]["daysPerMonth"]
        for festival in culture["festivals"]:
            if "month" in festival:
                if festival["month"] not in months:
                    errors.append(f"{festival['id']}: month {festival['month']} does not exist")
                if not 1 <= festival.get("day", 1) <= days_per_month:
                    errors.append(f"{festival['id']}: day is outside the {days_per_month}-day month")

    if demo:
        digits = demo["species"]["digitsPerHand"]
        if music["standardOctaveDivisions"] != digits * 2:
            errors.append("octave divisions do not follow from digits per hand")
        cassine = music["signatureInstrument"]
        if cassine["strings"] != digits * 2:
            errors.append("the cassine's string count does not follow from digits per hand")
        cassel = culture["sport"]["principalGame"]
        if calendar and cassel["playersPerSide"] != calendar["year"]["daysPerWeek"]:
            errors.append("cassel side size does not match the eight-day week")

    if languages:
        small = languages["totals"]["endangeredUnder1000Speakers"]
        weakness = next(
            w for w in culture["knownWeaknesses"]
            if w["id"] == "cult.weakness-small-language-fragility"
        )
        if str(small) not in weakness["summary"]:
            errors.append("small-language weakness does not cite the canonical endangered count")

    media = culture["media"]
    shares = sum(f["sharePct"] for f in media["funding"])
    if not approx(shares, 100.0, tol=0.1):
        errors.append(f"media funding shares sum to {shares:.1f}%, expected 100%")
    if media["attentionProblemSolved"]:
        errors.append("canon records the attention problem as unsolved")
    if media["levy"]["bodyMayConsiderEditorialContent"]:
        errors.append("the media levy body may not consider editorial content")

    standing = media["journalistStanding"]
    if standing["accessRequestsFiledByJournalistsPct"] + standing["accessRequestsFiledByLibrariesPct"] > 100:
        errors.append("access request shares exceed 100%")

    if ai:
        if culture["machineAssistedWork"]["prohibited"]:
            errors.append("machine-assisted art is not prohibited in ai.applications")
        if not culture["machineAssistedWork"]["provenanceDisclosureRequired"]:
            errors.append("provenance disclosure is required by ai.applications")

    arch = culture["architecture"]["unfinishedTradition"]
    if arch["shareLaterCompletedPct"] > 100:
        errors.append("more unfinished elements completed than exist")

    heritage = culture["heritage"]["repatriation"]
    if heritage["objectsContested"] > heritage["objectsReturned"]:
        warnings.append("contested objects outnumber returned objects")


def check_space(datasets: dict[str, dict]) -> None:
    """Off-world canon must agree with demographics, regions, physics, and contact status."""
    space = datasets.get("space.json")
    demo = datasets.get("demographics.json")
    regions = datasets.get("regions.json")
    physical = datasets.get("planet-physical.json")
    research = datasets.get("research.json")
    defence = datasets.get("defence.json")
    if not space:
        warnings.append("space check skipped — dataset absent")
        return

    off = space["offWorldPopulation"]
    distributed = sum(p["population"] for p in off["distribution"])
    if distributed != off["total"]:
        errors.append(
            f"off-world distribution sums to {distributed:,}, total declares {off['total']:,}"
        )

    if demo:
        canon_off = next(
            r for r in demo["populationByRegion"] if r["id"] == "demo.pop-offworld"
        )
        if off["total"] != canon_off["population"]:
            errors.append("off-world total disagrees with demographics.json")
        implied = 100 * off["total"] / demo["population"]["total"]
        if not approx(implied, off["shareOfPopulationPct"], tol=0.05):
            errors.append("off-world share does not match the declared population")

    territory = space["orbitalTerritory"]
    if regions:
        polity = next(
            r for r in regions["regions"] if r["id"] == territory["polity"]
        )
        if polity["population"] != off["total"]:
            errors.append("Orbital Territory population disagrees with regions.json")
        if territory["councilSeats"] != polity["councilSeats"]:
            errors.append("Orbital Territory Council seats disagree with regions.json")
        implied = polity["population"] / territory["councilSeats"]
        if abs(implied - territory["populationPerSeat"]) > 1000:
            errors.append("population per seat does not follow from population and seats")

        comparison = next(
            r for r in regions["regions"] if r["id"] == territory["comparisonRegion"]
        )
        implied_cmp = comparison["population"] / comparison["councilSeats"]
        if abs(implied_cmp - territory["comparisonPopulationPerSeat"]) > 1000:
            errors.append(
                "comparison region population per seat is wrong — check that a Region, "
                "not a continent, is being compared"
            )
        if territory["settledPopulation"] > off["total"]:
            errors.append("settled off-world population exceeds the total")

    if physical:
        mechanics = space["orbitalMechanics"]
        if mechanics["siderealDayHours"] != physical["planet"]["siderealDayHours"]:
            errors.append("sidereal day disagrees with planet-physical.json")

        # Stationary orbit must follow from the planet's own mass and rotation.
        import math
        gm = 6.674e-11 * physical["planet"]["massEarth"] * 5.972e24
        period = mechanics["siderealDayHours"] * 3600
        radius = (gm * period ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
        altitude = radius / 1000 - physical["planet"]["meanRadiusKm"]
        if abs(altitude - mechanics["stationaryOrbitAltitudeKm"]) > 200:
            errors.append(
                f"stationary orbit altitude {mechanics['stationaryOrbitAltitudeKm']} km "
                f"does not follow from the planet's mass and rotation ({altitude:.0f} km)"
            )

    contact = space["firstContact"]
    if contact["candidateSignalsResolved"] != contact["candidateSignalsSinceEY96"]:
        errors.append("canon records every candidate signal as resolved")
    if contact["contactConfirmed"]:
        errors.append("no phase has canonized first contact")
    if research:
        astronomy = next(
            f for f in research["sciences"] if f["id"] == "res.field-astronomy"
        )
        if astronomy["candidateSignalsSinceEY96"] != contact["candidateSignalsSinceEY96"]:
            errors.append("candidate signal count disagrees with research.json")
    if defence and defence["posture"]["contactedCivilizations"] != space["externalRelations"]["contactedCivilizations"]:
        errors.append("contacted civilization count disagrees with defence.json")

    if space["marn"]["elysiansLanded"] != 0 or space["marn"]["crewedLandingPermitted"]:
        errors.append("Marn is under permanent quarantine with no crewed landing")

    if space["lightLagRule"]["relaxed"]:
        errors.append("canon records the light-lag rule as never relaxed")


def check_reserve_horizons(datasets: dict[str, dict]) -> None:
    """A reserve horizon must follow from the reserve and the NET draw after recovery.

    planet.resources defines a reserve horizon as years of supply at current net
    consumption after recovery. Any material stating a reserve, a gross
    consumption, and a recovery rate must satisfy that definition arithmetically.
    """
    resources = datasets.get("resources.json")
    energy = datasets.get("energy.json")
    space = datasets.get("space.json")
    if not resources:
        warnings.append("reserve horizon check skipped — dataset absent")
        return

    for material in resources["materials"]:
        reserve_mt = material.get("reserveMt")
        gross = material.get("grossConsumptionTPerYear")
        net = material.get("netVirginDrawTPerYear")
        recovery = material.get("recoveryRate")
        horizon = material.get("reserveHorizonYears")
        if not (reserve_mt and gross and net and recovery is not None and horizon):
            continue

        reserve_t = reserve_mt * 1e6

        implied_net = gross * (1 - recovery)
        if abs(implied_net - net) > max(net * 0.02, 1):
            errors.append(
                f"{material['id']}: gross {gross:,} t/yr at {recovery:.0%} recovery implies "
                f"a net draw of {implied_net:,.0f} t/yr, but {net:,} is declared"
            )

        implied_horizon = reserve_t / net
        if abs(implied_horizon - horizon) > max(horizon * 0.05, 1):
            errors.append(
                f"{material['id']}: reserve over net draw is {implied_horizon:.0f} yr, "
                f"but the horizon is stated as {horizon} yr"
            )

        without = material.get("horizonWithoutRecoveryYears")
        if without:
            implied_without = reserve_t / gross
            if abs(implied_without - without) > max(without * 0.05, 1):
                errors.append(
                    f"{material['id']}: reserve over gross consumption is "
                    f"{implied_without:.0f} yr, but {without} yr is stated without recovery"
                )
            if without >= horizon:
                errors.append(f"{material['id']}: recovery does not extend the horizon")

        if energy and material["id"] == "resource.beryllium":
            fusion = energy["fusion"]
            for ours, theirs in (
                ("grossConsumptionTPerYear", "berylliumGrossConsumptionTPerYear"),
                ("netVirginDrawTPerYear", "berylliumNetVirginDrawTPerYear"),
                ("reserveHorizonYears", "berylliumHorizonYears"),
            ):
                if material[ours] != fusion[theirs]:
                    errors.append(f"beryllium {ours} disagrees between resources.json and energy.json")
            if material["recoveryRate"] * 100 != fusion["berylliumRecoveryRatePct"]:
                errors.append("beryllium recovery rate disagrees between resources.json and energy.json")

            if space:
                belt_share = space["belt"]["berylliumSupplySharePct"]
                if belt_share >= 100:
                    errors.append("Belt beryllium share is not a share")
                terrestrial = net * (1 - belt_share / 100)
                extended = reserve_t / terrestrial
                if extended <= horizon:
                    errors.append("Belt supply does not extend the beryllium horizon")


# Each indicator is checked against the exact canonical location it derives from.
METRIC_SOURCES = {
    "metric.median-lifespan": ("demographics.json", ["species", "medianLifespanEY"]),
    "metric.healthy-lifespan": ("demographics.json", ["species", "medianHealthyLifespanEY"]),
    "metric.infant-mortality": ("demographics.json", ["mortality", "infantMortalityPer100k"]),
    "metric.suicide-rate": ("demographics.json", ["mortality", "suicidePer100kPerYear"]),
    "metric.frailty-dependency": ("demographics.json", ["frailtyWeightedDependencyRatio"]),
    "metric.late-life-decline": ("health.json", ["geriatrics", "cognitiveDecline", "prevalenceOver110Pct"]),
    "metric.script-literacy": ("languages.json", ["totals", "scriptLiteracyPct"]),
    "metric.entitlement-drawn-high": ("education.json", ["entitlementAccount", "takeUpHighEarnersYears"]),
    "metric.entitlement-drawn-low": ("education.json", ["entitlementAccount", "takeUpLowEarnersYears"]),
    "metric.income-gini": ("economy.json", ["aggregates", "giniPostTaxTransfer"]),
    "metric.wealth-gini": ("industry.json", ["inequality", "wealthGini"]),
    "metric.interregional-ratio": ("economy.json", ["fiscalEqualization", "incomeRatioPostTransfer"]),
    "metric.homicide-rate": ("public-safety.json", ["useOfForce", "homicideRatePer100k"]),
    "metric.custody-rate": ("public-safety.json", ["custody", "ratePer100k"]),
    "metric.reoffending": ("public-safety.json", ["release", "reoffendingWithin5EYPct"]),
    "metric.deaths-police-contact": ("public-safety.json", ["useOfForce", "deathsFollowingPoliceContactPerYear"]),
    "metric.wrongful-conviction": ("justice.json", ["wrongfulConviction", "convictionsOverturnedPct"]),
    "metric.co2": ("environment.json", ["carbonAccount", "currentCo2Ppm"]),
    "metric.net-carbon": ("environment.json", ["carbonAccount", "netPositionGt"]),
    "metric.overturning": ("environment.json", ["overturningWatch", "currentStrengthPct"]),
    "metric.land-protected": ("biomes.json", ["protection", "landProtectedSharePct"]),
    "metric.ocean-protected": ("biomes.json", ["protection", "oceanProtectedSharePct"]),
    "metric.legacy-chemicals": ("environment.json", ["pollution", "legacyPersistence", "currentBurdenVsPeakPct"]),
    "metric.replication": ("research.json", ["replicationRatePct"]),
    "metric.rd-intensity": ("research.json", ["scale", "rdShareOfGcpPct"]),
    "metric.energy-demand": ("energy.json", ["demand", "meanPlanetaryTW"]),
    "metric.energy-per-capita": ("energy.json", ["demand", "perCapitaW"]),
    "metric.reserve-margin": ("energy.json", ["grid", "currentReserveMarginPct"]),
    "metric.islanding-failure": ("energy.json", ["grid", "communesFailingDrillPct"]),
    "metric.beryllium-horizon": ("energy.json", ["fusion", "berylliumHorizonYears"]),
    "metric.gcp-per-capita": ("economy.json", ["aggregates", "perCapita"]),
    "metric.unemployment": ("economy.json", ["aggregates", "unemploymentPct"]),
    "metric.housing-cost": ("cities.json", ["housing", "cost", "medianShareOfIncomePct"]),
    "metric.food-cost": ("agriculture.json", ["affordability", "medianHouseholdFoodShareOfIncomePct"]),
    "metric.food-insecurity": ("agriculture.json", ["affordability", "foodInsecurityLastYearPct"]),
    "metric.food-reserve": ("agriculture.json", ["reserves", "totalMonthsOfConsumption"]),
    "metric.secondary-metal": ("industry.json", ["materialsDoctrine", "secondaryShareOfMetalInputPct"]),
    "metric.trust-district-police": ("public-safety.json", ["publicContact", "trustInDistrictPoliceServicePct"]),
    "metric.trust-community-liaison": ("public-safety.json", ["publicContact", "trustInCommunityLiaisonPct"]),
    "metric.corruption-perception-concord": ("regions.json", ["integrityOutcomes", "believeCorruptionCommonAtConcordPct"]),
    "metric.bribe-solicitation": ("regions.json", ["integrityOutcomes", "residentsAskedForBribePct"]),
    "metric.access-overturn": ("regions.json", ["transparency", "appealOverturnRatePct"]),
}


def check_metrics(datasets: dict[str, dict]) -> None:
    """Every indicator must equal the value held in its own domain dataset."""
    metrics = datasets.get("metrics.json")
    if not metrics:
        warnings.append("metrics check skipped — dataset absent")
        return

    indicators = {m["id"]: m for m in metrics["indicators"]}

    for metric_id, (filename, path) in METRIC_SOURCES.items():
        metric = indicators.get(metric_id)
        if metric is None:
            errors.append(f"{metric_id} is registered for checking but absent from metrics.json")
            continue
        source = datasets.get(filename)
        if source is None:
            continue
        cursor = source
        for key in path:
            cursor = cursor[key]
        if float(metric["value"]) != float(cursor):
            errors.append(
                f"{metric_id}: metrics.json says {metric['value']} but "
                f"{filename} says {cursor}"
            )
        if metric.get("sourceDataset") != filename:
            errors.append(f"{metric_id}: sourceDataset should be {filename}")

    # Provenance must be declared exactly one way.
    for metric in metrics["indicators"]:
        has_dataset = "sourceDataset" in metric
        has_derivation = "derivation" in metric
        if has_dataset == has_derivation:
            errors.append(f"{metric['id']}: must declare either a sourceDataset or a derivation")
        if has_dataset and not (ROOT / "data" / metric["sourceDataset"]).exists():
            errors.append(f"{metric['id']}: sourceDataset {metric['sourceDataset']} does not exist")

    # Principle 1: no composite headline index.
    for principle in metrics["principles"]:
        if "composite" in principle["name"].lower() and "no" not in principle["name"].lower():
            errors.append("principle 1 must forbid a composite headline index")
    composites = [m for m in metrics["indicators"] if m.get("derivation") == "composite"]
    if len(composites) > 1:
        errors.append("more than one declared composite indicator; principle 1 permits none at headline level")

    if not metrics["unmeasuredRegister"]["entries"]:
        errors.append("the Unmeasured Register may not be empty")


def check_engineering_specs(datasets: dict[str, dict]) -> None:
    """Engineering specs must stay tied to the canon they claim to derive from."""
    spec_dir = ROOT / "docs" / "engineering"
    if not spec_dir.exists():
        return

    design = spec_dir / "DESIGN_SYSTEM.md"
    biomes = datasets.get("biomes.json")
    if design.exists() and biomes:
        text = design.read_text()
        palette = {}
        for key in ("terrestrialBiomes", "marineRealms"):
            for entry in biomes[key]:
                palette[entry["id"]] = entry["palette"]

        # Any biome cited as a palette source must exist and its hex must match.
        for biome_id in re.findall(r"`(biome\.[a-z-]+)` — ", text):
            if biome_id not in palette:
                errors.append(f"DESIGN_SYSTEM.md cites unknown palette source {biome_id}")
            elif palette[biome_id].lower() not in text.lower():
                errors.append(
                    f"DESIGN_SYSTEM.md cites {biome_id} but not its canonical colour "
                    f"{palette[biome_id]}"
                )

        # The green rule: canon records green as the exotic pigment.
        if "green is the exotic pigment" not in text.lower():
            errors.append("DESIGN_SYSTEM.md must carry the green-as-exotic rule from cult.arts")

    # Every engineering document carries the standard canon header.
    for path in sorted(spec_dir.glob("*.md")):
        if not re.search(r"\*\*Document ID:\*\* `eng\.[a-z-]+`", path.read_text()):
            errors.append(f"{path.name}: missing an eng. document ID")


def check_polygons(datasets: dict[str, dict]) -> None:
    continents = datasets.get("continents.json")
    if not continents:
        return
    for continent in continents["continents"]:
        rings = []
        if "outline" in continent:
            rings.append((continent["id"], continent["outline"]))
        for island in continent.get("islandOutlines", []):
            rings.append((island["featureId"], island["outline"]))
        for ident, ring in rings:
            # Unwrap longitudes so consecutive steps never exceed 180 degrees.
            # A naive modulo would break any ring crossing the prime meridian.
            normalised = [[ring[0][0], ring[0][1]]]
            for lon, lat in ring[1:]:
                previous = normalised[-1][0]
                while lon - previous > 180:
                    lon -= 360
                while previous - lon > 180:
                    lon += 360
                normalised.append([lon, lat])
            area2 = sum(
                normalised[i][0] * normalised[(i + 1) % len(normalised)][1]
                - normalised[(i + 1) % len(normalised)][0] * normalised[i][1]
                for i in range(len(normalised))
            )
            if area2 <= 0:
                errors.append(f"{ident}: outer ring is not counter-clockwise")
            for lon, lat in ring:
                if not -90 <= lat <= 90:
                    errors.append(f"{ident}: latitude {lat} out of range")


def main() -> int:
    datasets = load_datasets()
    defined = check_envelopes(datasets)
    check_references(datasets, defined)
    check_markdown()
    check_totals(datasets)
    check_demographics(datasets)
    check_regions(datasets)
    check_justice(datasets)
    check_public_safety(datasets)
    check_economy(datasets)
    check_industry(datasets)
    check_energy(datasets)
    check_environment(datasets)
    check_education(datasets)
    check_research(datasets)
    check_health(datasets)
    check_cities(datasets)
    check_routes(datasets)
    check_agriculture(datasets)
    check_defence(datasets)
    check_ai(datasets)
    check_culture(datasets)
    check_space(datasets)
    check_reserve_horizons(datasets)
    check_metrics(datasets)
    check_engineering_specs(datasets)
    check_polygons(datasets)

    for warning in warnings:
        print(f"WARN  {warning}")
    for error in errors:
        print(f"ERROR {error}")

    print(
        f"\n{len(datasets)} datasets, {len(defined)} entities, "
        f"{len(errors)} errors, {len(warnings)} warnings."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
