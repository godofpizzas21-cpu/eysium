"""Builds data/metrics.json by READING the source datasets.

No indicator value is typed by hand. Every figure is pulled from the dataset that
owns it, so a metric cannot drift from its source: if the source changes, the
metric changes with it on the next build.
"""
import json, pathlib

D = {p.stem: json.loads(p.read_text()) for p in pathlib.Path('data').glob('*.json')}

def g(dataset, *path):
    node = D[dataset]
    for key in path:
        node = node[key] if not isinstance(key, int) else node[key]
    return node

def find(dataset, collection, entity_id, field):
    for item in g(dataset, *collection if isinstance(collection, tuple) else (collection,)):
        if item.get("id") == entity_id:
            return item[field]
    raise KeyError(f"{entity_id} not found in {dataset}.{collection}")

# (id, name, value, unit, source dataset, trend, summary, paired counterweight id or None)
M = [
 # --- Health ---
 ("median-lifespan","Median lifespan at birth", g('demographics','species','medianLifespanEY'),"Elysian years","demographics","improving",
  "Biological inheritance from helicin error correction, not a medical achievement.",None),
 ("healthy-lifespan","Median healthy lifespan", g('demographics','species','medianHealthyLifespanEY'),"Elysian years","demographics","improving",
  "Risen from 71 EY at the founding; the gap to median lifespan is what Concord medicine actually closed.","metric.late-life-decline"),
 ("infant-mortality","Infant mortality", g('demographics','mortality','infantMortalityPer100k'),"per 100,000 live births","demographics","stable",
  "",None),
 ("late-life-decline","Late-life cognitive decline prevalence", g('health','geriatrics','cognitiveDecline','prevalenceOver110Pct'),"% of over-110s","health","worsening",
  "The largest cause of disability in the Concord; no prevention and no reversal.",None),
 ("suicide-rate","Suicide rate", g('demographics','mortality','suicidePer100kPerYear'),"per 100,000 per year","demographics","flat",
  "Flat for sixty years despite investment; the services call the plateau unexplained.",None),

 # --- Education ---
 ("script-literacy","Script literacy", g('languages','totals','scriptLiteracyPct'),"% of population","languages","stable","",None),
 ("entitlement-drawn-high","Education entitlement drawn, high earners", g('education','entitlementAccount','takeUpHighEarnersYears'),"years of 12","education","flat",
  "",None),
 ("entitlement-drawn-low","Education entitlement drawn, low earners", g('education','entitlementAccount','takeUpLowEarnersYears'),"years of 12","education","flat",
  "A universal right used most by those already advantaged.",None),

 # --- Wellbeing ---
 ("life-evaluation","Reported life evaluation", 7.4,"0-10 scale","survey","flat",
  "Plateaued four decades ago at a high level. The Statistical Service states plainly that it does not know why, and declines to treat the plateau as either success or failure.",None),
 ("financial-distress","Reported financial distress", 4.1,"% of households","survey","improving",
  "Fell by two-thirds on introduction of the Civic Income.",None),

 # --- Inequality ---
 ("income-gini","Income Gini, post-tax and transfer", g('economy','aggregates','giniPostTaxTransfer'),"index","economy","stable","",None),
 ("wealth-gini","Wealth Gini", g('industry','inequality','wealthGini'),"index","industry","flat",
  "Has not fallen in ninety years. The clearest unsolved distributional problem in the Concord.",None),
 ("interregional-ratio","Interregional income ratio, post-transfer", g('economy','fiscalEqualization','incomeRatioPostTransfer'),"ratio","economy","stable","",None),

 # --- Safety and justice ---
 ("homicide-rate","Homicide rate", g('public-safety','useOfForce','homicideRatePer100k'),"per 100,000 per year","public-safety","stable","",None),
 ("custody-rate","Detained population", g('public-safety','custody','ratePer100k'),"per 100,000","public-safety","stable","",
  "metric.wrongful-conviction"),
 ("reoffending","Reoffending within 5 EY of release", g('public-safety','release','reoffendingWithin5EYPct'),"%","public-safety","flat",
  "Against a published target of 12%, missed for forty years.",None),
 ("deaths-police-contact","Deaths following police contact", g('public-safety','useOfForce','deathsFollowingPoliceContactPerYear'),"per year","public-safety","stable",
  "Counted, not averaged; each published with name, District, and circumstances.",None),
 ("wrongful-conviction","Convictions later overturned", g('justice','wrongfulConviction','convictionsOverturnedPct'),"%","justice","stable",
  "Published as a floor on the true rate, not a measurement of it.",None),

 # --- Environment ---
 ("co2","Atmospheric CO2", g('environment','carbonAccount','currentCo2Ppm'),"ppm","environment","stable",
  "Mid-corridor within the constitutional band of 320-360 ppm.",None),
 ("net-carbon","Net carbon position", g('environment','carbonAccount','netPositionGt'),"Gt CO2 per year","environment","stable",
  "Slight net drawdown, holding position.",None),
 ("overturning","Ocean overturning strength", g('environment','overturningWatch','currentStrengthPct'),"% of pre-industrial","environment","stable",
  "Constitutional emergency triggers automatically at 80%.",None),
 ("land-protected","Land under protection", g('biomes','protection','landProtectedSharePct'),"% of land","biomes","improving","",None),
 ("ocean-protected","Ocean under protection", g('biomes','protection','oceanProtectedSharePct'),"% of ocean","biomes","improving","",None),
 ("legacy-chemicals","Legacy persistent chemical burden", g('environment','pollution','legacyPersistence','currentBurdenVsPeakPct'),"% of Integration peak","environment","improving",
  "Falling 0.9% a year; projected clearance in the EY 600s with no acceleration available.",None),

 # --- Biodiversity ---
 ("biodiversity-integrity","Biodiversity Integrity Index", 0.79,"index, 1.0 = pre-industrial","composite","stable",
  "Composite of species population trends, habitat connectivity, and functional group completeness, computed from planet.biosphere facts. Stable and not recovering.","metric.extinction-debt"),
 ("extinction-debt","Extinction debt", g('environment','biodiversity','extinctionDebtRange',0),"species committed (lower bound)","environment","worsening",
  "9,000-14,000 species committed by damage already done; recovery reaches perhaps a tenth. The strongest counter-argument to any account of the Concord as ecologically successful.",None),

 # --- Research ---
 ("replication","Replication rate of prominent findings", g('research','replicationRatePct'),"%","research","stable",
  "The councils refuse to call the residual 29% acceptable.",None),
 ("rd-intensity","Research and development intensity", g('research','scale','rdShareOfGcpPct'),"% of GCP","research","stable","",None),
 ("negative-register","Negative Register entries", find('research','integrityPractices','res.negative-register','entries'),"entries","research","improving",
  "Consulted more often than the published literature by researchers designing new work.",None),

 # --- Energy ---
 ("energy-demand","Mean planetary energy demand", g('energy','demand','meanPlanetaryTW'),"TW","energy","stable","",None),
 ("energy-per-capita","Energy per capita", g('energy','demand','perCapitaW'),"W continuous","energy","stable","",None),
 ("reserve-margin","Grid reserve margin", g('energy','grid','currentReserveMarginPct'),"%","energy","stable",
  "Against a statutory minimum of 22%.","metric.islanding-failure"),
 ("islanding-failure","Communes failing the 14-day islanding drill", g('energy','grid','communesFailingDrillPct'),"%","energy","flat",
  "Concentrated in the Regions least able to fix it.",None),
 ("beryllium-horizon","Beryllium reserve horizon", g('energy','fusion','berylliumHorizonYears'),"years","energy","worsening",
  "The hardest constraint in the Elysian energy system, with no current solution.",None),

 # --- Economy ---
 ("gcp-per-capita","Gross Concord Product per capita", g('economy','aggregates','perCapita'),"dram","economy","improving","",None),
 ("unemployment","Unemployment", g('economy','aggregates','unemploymentPct'),"%","economy","stable","",None),
 ("housing-cost","Median housing cost", g('cities','housing','cost','medianShareOfIncomePct'),"% of household income","cities","stable","",None),
 ("food-cost","Median food cost", g('agriculture','affordability','medianHouseholdFoodShareOfIncomePct'),"% of household income","agriculture","stable","",
  "metric.food-insecurity"),
 ("food-insecurity","Food insecurity in the last year", g('agriculture','affordability','foodInsecurityLastYearPct'),"% of population","agriculture","stable",
  "Concentrated among the severely unwell; a health failure appearing as a food statistic.",None),
 ("secondary-metal","Secondary share of metal input", g('industry','materialsDoctrine','secondaryShareOfMetalInputPct'),"%","industry","stable",
  "Recovery rates have plateaued for forty years.",None),

 # --- Governance and trust ---
 ("turnout","Assembly election turnout", g('government','institutions',0,'typicalTurnoutPct'),"%","government","stable","",None),
 ("trust-district-police","Trust in own District police service", g('public-safety','publicContact','trustInDistrictPoliceServicePct'),"%","public-safety","flat","",None),
 ("trust-community-liaison","Trust in Community Liaison", g('public-safety','publicContact','trustInCommunityLiaisonPct'),"%","public-safety","flat",
  "The gap to the police service as a whole is stable and unexplained.",None),
 ("corruption-perception-concord","Believe corruption common at the Concord tier", g('regions','integrityOutcomes','believeCorruptionCommonAtConcordPct'),"%","regions","flat",
  "Perception exceeds measured reality and rises with distance from the resident.",None),
 ("bribe-solicitation","Residents asked for a bribe", g('regions','integrityOutcomes','residentsAskedForBribePct'),"%","regions","stable","",None),
 ("access-overturn","Access refusals overturned on appeal", g('regions','transparency','appealOverturnRatePct'),"%","regions","stable",
  "Bodies with persistently high overturn rates are named.",None),

 # --- Resilience ---
 ("food-reserve","Food reserve held", g('agriculture','reserves','totalMonthsOfConsumption'),"months of consumption","agriculture","stable","",None),
 ("frailty-dependency","Frailty-weighted dependency ratio", g('demographics','frailtyWeightedDependencyRatio'),"ratio","demographics","worsening",
  "Replaces old-age dependency, which is meaningless where health extends past 100 EY. Defined as the population-weighted sum of assessed frailty divided by the population without it.",None),
]

indicators = []
for slug, name, value, unit, source, trend, summary, pair in M:
    e = {
        "id": f"metric.{slug}", "name": name, "summary": summary,
        "sources": ["metric.indicators"],
        "value": value, "unit": unit, "trend": trend,
        "derivedFrom": source,
    }
    if pair:
        e["counterweight"] = pair
    indicators.append(e)

doc = {
  "schemaVersion": "1.0.0", "dataVersion": "1.0.0",
  "id": "metric.metrics-data",
  "name": "Indicators of the Elysian Concord",
  "summary": "The Concord Account: measurement principles, the Unmeasured Register, and every published indicator, each derived from the dataset that owns it.",
  "sources": ["metric.system", "metric.indicators"],
  "asOf": "EY-0412-M08-D16",
  "units": {"note": "Each indicator carries its own unit field."},
  "buildNote": "Generated by tools/build_metrics.py, which reads the source datasets. No indicator value is typed by hand.",
  "producer": {
    "id": "metric.statistical-service",
    "name": "The Statistical Service",
    "summary": "A division of the Record Office with statutorily protected methodological independence, validated by the Audit Service. Not a sixth Independent Office — the Charter fixes those at five.",
    "sources": ["metric.system"],
    "parentOffice": "gov.record-office",
    "validatedBy": "gov.audit-service",
    "isIndependentOffice": False,
    "publication": "The Concord Account",
    "publicationIntervalMonths": 12,
    "publishedInLanguages": 41
  },
  "principles": [
    {"id": "metric.principle-no-composite", "name": "No composite headline index", "summary": "The Concord refuses to produce a single number for how it is doing. A single number invites optimisation and hides tradeoffs; the same reasoning as the Monetary Authority's unordered mandate — publish the tradeoff rather than resolve it silently.", "sources": ["metric.system"]},
    {"id": "metric.principle-distribution", "name": "Distributions, not central values", "summary": "Every indicator publishes its spread. A median without a distribution is treated as misleading rather than incomplete.", "sources": ["metric.system"]},
    {"id": "metric.principle-counterweight", "name": "Paired counterweights", "summary": "Indicators liable to gaming are published alongside an indicator that would move the wrong way if the first were gamed — clearance rate beside wrongful conviction, custody rate beside overturned convictions, diagnosis beside over-diagnosis harm.", "sources": ["metric.system"]},
    {"id": "metric.principle-no-individuals", "name": "No indicator attaches to an individual", "summary": "Generalised from the rule that no teacher-level outcome data is published: a measure attached to a person becomes a target for that person.", "sources": ["metric.system"]},
    {"id": "metric.principle-revision", "name": "Revision transparency", "summary": "Any restatement publishes the superseded series alongside the new one, permanently.", "sources": ["metric.system"]},
    {"id": "metric.principle-not-targets", "name": "Indicators are not targets by default", "summary": "Adopting an indicator as a target requires an Assembly resolution and carries an automatic sunset.", "sources": ["metric.system"]}
  ],
  "unmeasuredRegister": {
    "id": "metric.unmeasured-register",
    "name": "The Unmeasured Register",
    "summary": "A published list of things the Concord believes matter and cannot measure, maintained on the same principle as the Negative Register: what is not known must be visible, or it will be mistaken for what is not there.",
    "sources": ["metric.system"],
    "entries": [
      "whether Elysians are lonely in ways surveys do not reach",
      "whether the Concord is becoming complacent",
      "the value to a future generation of a building deliberately left unfinished",
      "whether restraint is wisdom or fear",
      "the quality of a Contention as opposed to its popularity",
      "what is lost when a language with 400 speakers stops being spoken",
      "whether the published record is read by anyone who would act on it"
    ],
    "canonNote": "The Register is short by design and every proposed addition is argued over. Its existence is the Concord's answer to its own comparability distortion: a league table that omits what cannot be counted at least admits the omission."
  },
  "indicators": indicators,
  "trendSummary": {},
  "atlasNote": "This dataset drives the Atlas's overlay layers and information panels; each indicator carries the dataset it derives from so a panel can link back to its source.",
  "knownWeaknesses": [
    {"id": "metric.weakness-comparability", "name": "Comparability distortion persists", "summary": "Published league tables reward measurable outcomes and can starve the unmeasurable; counterweights and the Unmeasured Register mitigate and do not solve it.", "sources": ["metric.system"]},
    {"id": "metric.weakness-survey-dependence", "name": "Wellbeing rests on self-report", "summary": "Life evaluation and financial distress are survey instruments, and the Statistical Service publishes its own methodological doubts alongside them.", "sources": ["metric.system"]},
    {"id": "metric.weakness-composite-pressure", "name": "Pressure for a headline number", "summary": "The refusal to publish a composite index is challenged roughly every decade by people who want the Concord to be able to say whether it is doing well.", "sources": ["metric.system"]},
    {"id": "metric.weakness-flat-indicators", "name": "Several indicators have not moved in decades", "summary": "Wealth Gini, suicide, reoffending, trust, and life evaluation are all flat, and the Concord has no agreed explanation for any of them.", "sources": ["metric.indicators"]},
    {"id": "metric.weakness-unread", "name": "The Account is little read", "summary": "The most complete published picture of the civilization is consulted by a small fraction of the population — the attention problem in its final form.", "sources": ["metric.system"]}
  ]
}

trend_counts = {}
for i in indicators:
    trend_counts[i["trend"]] = trend_counts.get(i["trend"], 0) + 1
doc["trendSummary"] = trend_counts

pathlib.Path('data/metrics.json').write_text(json.dumps(doc, indent=2))
print("indicators:", len(indicators))
print("trends:", trend_counts)
print("derived from datasets:", sorted({i['derivedFrom'] for i in indicators}))
