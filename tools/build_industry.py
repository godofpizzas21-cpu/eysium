import json

lf = 3_620_000_000   # labour force
gcp = 1_029_500_000_000_000

sectors_gcp = [
    ("services-care", "Care, health, education, and public service", 31, 31),
    ("manufacturing", "Manufacturing", 16, 12),
    ("construction", "Construction", 8, 7),
    ("retail-personal", "Retail, hospitality, and personal services", 9, 14),
    ("energy-utilities", "Energy, utilities, and materials recovery", 6, 4),
    ("logistics", "Transport and logistics", 5, 6),
    ("agriculture", "Agriculture and fisheries", 5, 4),
    ("mining", "Mining and extraction", 4, 1),
    ("research-technical", "Research, engineering, and technical", 6, 8),
    ("finance-professional", "Finance, legal, and professional", 5, 6),
    ("culture", "Culture, media, and sport", 3, 5),
    ("other", "Other and administrative", 2, 2),
]

sectors = []
for slug, name, gcp_share, emp_share in sectors_gcp:
    sectors.append({
        "id": f"ind.sector-{slug}", "name": name,
        "summary": "", "sources": ["ind.industry"],
        "gcpSharePct": gcp_share, "employmentSharePct": emp_share,
        "employment": round(lf * emp_share / 100),
    })

doc = {
  "schemaVersion": "1.0.0", "dataVersion": "1.0.0",
  "id": "ind.industry-data",
  "name": "Industry, Concentration, and Inequality",
  "summary": "Circular-materials doctrine, manufacturing, robotics and the transition right, mining, construction, logistics, the concentration regime, and inequality measures.",
  "sources": ["ind.industry", "ind.concentration"],
  "asOf": "EY-0412-M08-D16",
  "units": {"employment": "individuals", "share": "percent"},
  "labourForce": {
    "total": lf,
    "employed": 3508000000,
    "unemploymentPct": 3.1,
    "publicServants": 579000000,
    "publicServantSharePct": 16.0,
    "note": "Labour force spans ages 16 EY to beyond the median retirement of 88 EY; 31% of Elysians over 88 continue in some paid work."
  },
  "materialsDoctrine": {
    "principle": "You may sell the product. You may not sell the material.",
    "producerResponsibilityPermanent": True,
    "secondaryShareOfMetalInputPct": 71,
    "secondaryShareCopperAluminiumIronPct": 80,
    "residualWasteSharePct": 3.4,
    "landfillOfPassportedMaterialPermitted": False,
    "instruments": [
      {"id": "ind.material-passport", "name": "Material passport", "summary": "Machine-readable record of composition, disassembly sequence, Constrained List provenance, and recovery route. A legal document; falsification is a band 3 offence.", "sources": ["ind.industry"], "relatedTo": "law.band-3"},
      {"id": "ind.design-for-disassembly", "name": "Design for disassembly", "summary": "Products must separate into material streams using published tools; permanent bonding of dissimilar materials requires justification and a recovery route.", "sources": ["ind.industry"]},
      {"id": "ind.right-to-repair", "name": "The right to repair", "summary": "Parts, manuals, tools, and firmware available to any owner or independent repairer at non-discriminatory prices for 20 Elysian years after last sale; repair-blocking software locks are void.", "sources": ["ind.industry"], "availabilityYears": 20, "sectorEmployment": 34000000}
    ]
  },
  "sectors": sectors,
  "manufacturing": {
    "gcpSharePct": 16,
    "employment": round(lf * 0.12),
    "outputInFacilitiesUnder500WorkersPct": 41,
    "robotsPer10000Workers": 2400,
    "distributedNotConcentrated": True,
    "twoSourceSufficiency": {
      "minimumProducingRegions": 2,
      "maximumSingleRegionCapacityPct": 60,
      "listedProductCategories": 1900
    },
    "rationale": "A planetary supply chain with a single source has a single point of failure, and distributed production also removes freight that concentrated production would require."
  },
  "automation": {
    "robotsPer10000Workers": 2400,
    "aggregateUnemploymentCausedByAutomation": False,
    "disclosure": {
      "id": "ind.automation-disclosure",
      "name": "The automation disclosure",
      "summary": "Firms above 250 workers must publish planned displacing automation two Elysian years ahead, identifying affected roles. Surprise, not automation, is what makes displacement destructive.",
      "sources": ["ind.industry"],
      "firmSizeThreshold": 250,
      "noticeYears": 2,
      "public": True
    },
    "transitionRight": {
      "id": "ind.transition-right",
      "name": "The transition right",
      "summary": "Attaches to the worker, not the job, and cannot be waived by contract.",
      "sources": ["ind.industry"],
      "incomeContinuationYears": 2,
      "fundedRetrainingYears": 3,
      "formerEmployerPriorityYears": 5,
      "takeUpPct": 71,
      "answeredBy": ["phase-08"]
    },
    "robotTax": {
      "adopted": False,
      "rejectedEY": 289,
      "reasoning": "A tax on the specific form of capital that substitutes for labour would distort investment toward less productive alternatives without helping the displaced worker, whom the transition right helps directly.",
      "argumentRecursEveryYears": 30
    }
  },
  "mining": {
    "gcpSharePct": 4,
    "employment": 21000000,
    "primaryShareOfMetalInputPct": 29,
    "activeMajorOperations": 1240,
    "provinces": ["region.vail-spine", "region.cindral-arc", "region.thalassar-rim", "region.sirocc-basin"],
    "deepSeaMiningPermitted": False,
    "deepSeaChallenges": 2,
    "lastDeepSeaChallengeEY": 356,
    "restorationBondRequiredBeforeOpening": True,
    "abandonedSitesPredatingRule": 7,
    "siroccWaterClosedLoop": True,
    "bindingConstraint": "resource.beryllium"
  },
  "construction": {
    "gcpSharePct": 8,
    "employment": round(lf * 0.07),
    "defaultStructuralMaterialBelow12Storeys": "engineered timber",
    "designLifeYears": 150,
    "manufacturedOffSitePct": 68,
    "demolitionToRubbleTreatedAsRecoveryFailure": True,
    "answeredBy": ["phase-10"]
  },
  "logistics": {
    "gcpSharePct": 5,
    "employmentSharePct": 6,
    "freightGtKmPerCapita": 41.2,
    "modalSharePct": {"railAndMaglev": 61, "sea": 27, "road": 11, "air": 1},
    "freightIntensityVsIntegrationFraction": 0.33,
    "justInTimeRejected": True,
    "strategicReserveInterruptionCoverYears": 2,
    "rationale": "Just-in-time is an optimisation that converts a robust system into a fragile one."
  },
  "publicIndustry": {
    "dominatesIn": ["natural monopolies", "strategic materials", "long-horizon research infrastructure"],
    "naturalMonopolies": ["grid", "water", "rail track", "ports", "payment", "identity"],
    "payRatioLimit": 8,
    "cooperativeEmploymentShareInConstructionFoodRepairPrecisionPct": 40,
    "mayFailAndBeRestructured": True
  },
  "concentrationRegime": {
    "enforcer": {
      "id": "ind.concentration-board",
      "name": "The Concentration Board",
      "summary": "Statutory body within the Treasury and Materials portfolio; not one of the five Independent Offices, but its decisions are appealable only to the Court of Review, not to the Executive Board.",
      "sources": ["ind.concentration"],
      "portfolio": "gov.portfolio-treasury-materials",
      "adjudicatedBy": "law.court-of-review"
    },
    "philosophy": "Limit structure, treat conduct as secondary. Conduct rules arrive too late: by the time a firm's behaviour is worth prosecuting, its power is already a constitutional fact.",
    "originEra": "hist.era-integration",
    "thresholds": [
      {"id": "ind.threshold-registration", "name": "Above 20% of a relevant market", "summary": "Mandatory registration and annual reporting.", "sources": ["ind.concentration"], "marketSharePct": 20},
      {"id": "ind.threshold-reversed-burden", "name": "Above 30% of a relevant market", "summary": "Reversed burden: the firm must publicly justify its continued scale every 5 years.", "sources": ["ind.concentration"], "marketSharePct": 30, "reviewIntervalYears": 5, "successfulRebuttalsSinceEY300": 34},
      {"id": "ind.threshold-structural-remedy", "name": "Above 45% of a relevant market", "summary": "Structural remedy presumed; the firm must divest unless it rebuts the presumption.", "sources": ["ind.concentration"], "marketSharePct": 45}
    ],
    "absoluteProhibitions": [
      {"id": "ind.prohibit-competitor-acquisition", "name": "Acquiring a competitor above threshold", "summary": "Actual or potential competitors, above the 20% threshold.", "sources": ["ind.concentration"]},
      {"id": "ind.prohibit-interlocking", "name": "Interlocking directorates", "summary": "Between firms in the same or adjacent markets.", "sources": ["ind.concentration"]},
      {"id": "ind.prohibit-data-exclusivity", "name": "Exclusive control of an essential dataset", "summary": "Data a market needs to function must be licensed on published, non-discriminatory terms.", "sources": ["ind.concentration"], "answeredBy": ["phase-13"]},
      {"id": "ind.prohibit-vertical-monopoly", "name": "Vertical integration with a natural monopoly", "summary": "Grid, rails, ports, payment, and identity are public precisely so the question does not arise.", "sources": ["ind.concentration"]},
      {"id": "ind.prohibit-parity-clauses", "name": "Most-favoured-nation and parity clauses", "summary": "In platform contracts.", "sources": ["ind.concentration"]}
    ],
    "outcomes": {
      "largestPrivateFirmShareOfGcpPct": 0.9,
      "top100FirmsShareOfGcpPct": 14,
      "concentrationVsIntegrationFraction": 0.33
    },
    "acknowledgedCost": {
      "estimatedOutputForgonePct": [3, 5],
      "worstAffected": ["semiconductor fabrication", "large-scale pharmaceutical development", "orbital launch"],
      "canonPosition": "Probably correct on the numbers and unresolved on the tradeoff."
    }
  },
  "inequality": {
    "incomeGiniPreTaxTransfer": 0.38,
    "incomeGiniPostTaxTransfer": 0.21,
    "wealthGini": 0.44,
    "top1PctWealthSharePct": 11,
    "top10PctWealthSharePct": 34,
    "bottom40PctWealthSharePct": 14,
    "interregionalIncomeRatioPostTransfer": 1.9,
    "p90p10IncomeRatio": 3.1,
    "payRatioDisclosureThresholdWorkers": 250,
    "publicEnterprisePayRatioCap": 8,
    "typicalCooperativePayRatioCap": 6,
    "wealthInequalityFallingOver90Years": False,
    "causes": [
      {"id": "ind.wealth-cause-compounding", "name": "Long lives compound", "summary": "A 96-year adult life accumulates far more than an Earth-length one at identical saving rates. Time does most of the work and cannot be legislated against.", "sources": ["ind.concentration"]},
      {"id": "ind.wealth-cause-avoidance", "name": "Transfer avoidance", "summary": "112-year lifespans give enormous scope to structure transfers as lifetime gifts, trusts, and foundations; yield has drifted down for sixty years.", "sources": ["ind.concentration"]},
      {"id": "ind.wealth-cause-housing", "name": "Housing appreciation", "summary": "Land value tax captures much of the unearned gain but not all; long-tenured households in high-demand Districts hold substantial appreciated wealth.", "sources": ["ind.concentration"], "answeredBy": ["phase-10"]}
    ],
    "debatedRemedies": [
      {"id": "ind.remedy-net-wealth-tax", "name": "Periodic net wealth tax", "summary": "Debated, no majority.", "sources": ["ind.concentration"]},
      {"id": "ind.remedy-receipts-cap", "name": "Lifetime receipts cap", "summary": "Debated, no majority.", "sources": ["ind.concentration"]},
      {"id": "ind.remedy-sovereign-endowment", "name": "Sovereign endowment paying a universal capital dividend", "summary": "Supported by the Office of Future Generations; blocked by the Council of Regions.", "sources": ["ind.concentration"], "supportedBy": "gov.office-future-generations"}
    ],
    "decoupling": {
      "summary": "Wealth does not purchase advantage in the systems that matter most: political donations are prohibited, healthcare and education are universal with no significant private tier, courts provide free representation, and housing is a right.",
      "cannotBuy": ["a better court", "a better school", "a better hospital", "a better legislator"],
      "rejoinder": "This is exactly what a comfortable society tells itself about its remaining inequalities. Canon offers the decoupling as the Concord's own account of itself, not as a settled finding."
    }
  },
  "knownWeaknesses": [
    {"id": "ind.weakness-distributed-cost", "name": "Distributed production costs efficiency", "summary": "Two-source sufficiency and moderate scale carry a 9-14% unit-cost penalty in affected categories, paid deliberately and criticised constantly.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-beryllium", "name": "Beryllium ceiling", "summary": "A materials constraint on fusion growth with no terrestrial solution and an unproven off-world one.", "sources": ["ind.industry"], "answeredBy": ["phase-07", "phase-15"]},
    {"id": "ind.weakness-recovery-plateau", "name": "Recovery plateau", "summary": "Recovery rates have not improved in forty years; further gains would cost more energy than the materials are worth.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-passport-falsification", "name": "Passport falsification", "summary": "Falsified passports found in 0.9% of audited output from small producers.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-transition-takeup", "name": "Transition right take-up", "summary": "71% of eligible displaced workers claim it; non-claimants are disproportionately older and in small firms.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-repair-capacity", "name": "Repair prestige without repair capacity", "summary": "Vacancies run at 8.1% against 2.9% economy-wide.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-inventory-cost", "name": "Inventory cost", "summary": "Rejecting just-in-time ties up capital and warehouse space and has never been costed against a counterfactual.", "sources": ["ind.industry"]},
    {"id": "ind.weakness-wealth-flat", "name": "Wealth inequality is not falling", "summary": "Flat for ninety years; causes understood, remedies blocked, no majority for any proposal.", "sources": ["ind.concentration"]},
    {"id": "ind.weakness-scale-forgone", "name": "Scale forgone", "summary": "An estimated 3-5% of potential output, most clearly in semiconductors, pharmaceutical development, and launch.", "sources": ["ind.concentration"]},
    {"id": "ind.weakness-market-definition", "name": "Relevant-market definition", "summary": "Every structural threshold depends on a market definition that is contestable, litigated, and quietly political.", "sources": ["ind.concentration"]},
    {"id": "ind.weakness-data-licensing", "name": "Data licensing is weak in practice", "summary": "The Concentration Board has lost four of its last seven data cases.", "sources": ["ind.concentration"], "answeredBy": ["phase-13"]},
    {"id": "ind.weakness-threshold-clustering", "name": "Small-firm exemptions accumulate", "summary": "Thresholds at 250 workers create visible clustering at 240-249, recognised for a century and never fixed.", "sources": ["ind.concentration"]},
    {"id": "ind.weakness-public-enterprise-accountability", "name": "Public enterprise accountability", "summary": "Public enterprises escape the concentration regime by construction; their accountability is to Districts and Regions of varying capacity.", "sources": ["ind.concentration"]}
  ]
}

with open('data/industry.json', 'w') as f:
    json.dump(doc, f, indent=2)

print("gcp shares:", sum(s['gcpSharePct'] for s in sectors))
print("emp shares:", sum(s['employmentSharePct'] for s in sectors))
print("employment sum:", f"{sum(s['employment'] for s in sectors):,}", "vs labour force", f"{lf:,}")
