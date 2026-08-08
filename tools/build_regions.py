import json

R = [
 # (slug, name, continent, pop_millions, form, delegateMethod, lat, lon, summary)
 ("ilvaret","Ilvaret","region.meridia",340,"assembly-executive","assembly",14.0,2.0,"Lower Alcyon Region; site of the ruins of Ilvaret and the oldest continuously administered territory on Elysium."),
 ("alcyone","Alcyone","region.meridia",310,"assembly-executive","assembly",21.0,4.0,"Middle Alcyon Region; heartland of the flow-share tradition."),
 ("sirocc","Sirocc","region.meridia",255,"assembly-manager","direct",26.0,8.0,"Desert Region of the Sirocc Basin; lithium brine fields and the planet's largest solar installations."),
 ("cindral","Cindral","region.meridia",210,"assembly-executive","assembly",8.0,34.0,"Mountain Region along the Cindral Arc; seismic, geothermal, and mineral-rich."),
 ("kethran","Kethran","region.meridia",190,"assembly-manager","assembly",-4.0,28.0,"Eastern Meridian uplands between the Cindral Arc and the Amarant coast."),
 ("meridian","Meridian","region.meridia",265,"assembly-executive","direct",30.0,-12.0,"The Meridian Plain; historic agricultural core and site of the Meridian Stone."),
 ("verdanne","Verdanne","region.meridia",225,"assembly-executive","assembly",-12.0,10.0,"Equatorial rainforest Region; the Verdanne core is permanently protected."),
 ("amarath-coast","Amarath Coast","region.meridia",180,"assembly-manager","assembly",-2.0,40.0,"Eastern seaboard Region facing the Amarant Ocean."),
 ("sudmark","Sudmark","region.meridia",205,"assembly-manager","assembly",-20.0,-6.0,"Southern Meridian Region of seasonal woodland and savanna."),

 ("kessandra","Kessandra","region.elandris",355,"assembly-executive","assembly",2.0,112.0,"Most populous Region on Elysium; northern Elandric monsoon lowlands."),
 ("serrance","Serrance","region.elandris",320,"assembly-executive","direct",-28.0,150.0,"Storm-coast Region at Cape Serrance; the most cyclone-exposed inhabited territory on the planet."),
 ("andriel","Andriel","region.elandris",290,"assembly-manager","assembly",-8.0,128.0,"Central Elandric Region of dense river settlement."),
 ("halvane","Halvane","region.elandris",270,"assembly-executive","assembly",-18.0,120.0,"Southwestern Elandris; Amarant Upwelling fisheries."),
 ("terrace-north","Terrace North","region.elandris",245,"assembly-executive","assembly",6.0,132.0,"Northern Elandric Terraces; intensive terraced agriculture."),
 ("terrace-south","Terrace South","region.elandris",230,"assembly-manager","assembly",-12.0,140.0,"Southern Elandric Terraces."),
 ("mirran","Mirran","region.elandris",220,"assembly-executive","sortition",-22.0,134.0,"Interior Elandric Region; the first to adopt sortition for Council delegates."),
 ("oshaal","Oshaal","region.elandris",195,"assembly-executive","assembly",-32.0,126.0,"Southern Elandric temperate Region."),
 ("delvane","Delvane","region.elandris",185,"assembly-manager","assembly",10.0,142.0,"Northeastern Elandric coastal Region."),

 ("mistral","Mistral","region.thalassar",290,"assembly-executive","direct",18.0,-116.0,"Region of the Mistral Shelf; the richest fishery on Elysium."),
 ("fjordmark","Fjordmark","region.thalassar",265,"assembly-executive","assembly",41.0,-124.0,"Northern fjord coast; the wettest inhabited land on the planet."),
 ("rimward","Rimward","region.thalassar",230,"assembly-manager","assembly",8.0,-106.0,"Interior plateau Region behind the Thalassar Rim."),
 ("sablewater","Sablewater","region.thalassar",205,"assembly-executive","direct",-4.0,-120.0,"Southern Thalassari coast and winter-wet scrublands."),
 ("coronal","Coronal","region.thalassar",170,"delegate-council","direct",30.0,-110.0,"Northern interior Region governed by a council of District delegates."),

 ("vailmark","Vailmark","region.auroria",285,"assembly-executive","assembly",52.0,78.0,"Region of the Vail Spine; the most important mineral province on Elysium and the cradle of industry."),
 ("serapht","Serapht","region.auroria",245,"assembly-executive","direct",58.0,96.0,"Region around Lake Serapht; lake-effect snow belt."),
 ("korren","Korren","region.auroria",215,"assembly-manager","assembly",49.0,110.0,"Southern Aurorian broadleaf and mixed-forest Region."),
 ("northreach","Northreach","region.auroria",190,"delegate-council","rotation",68.0,88.0,"Subpolar Region of scattered settlement and long winter darkness."),
 ("hollen","Hollen","region.auroria",155,"delegate-council","assembly",61.0,66.0,"Western Aurorian taiga Region."),

 ("kaelis-group","Kaelis Group","region.myriad-isles",140,"direct-democratic","direct",-1.0,172.5,"Largest Isle Region; birthplace of the ocean-stewardship traditions."),
 ("orphir-group","Orphir Group","region.myriad-isles",115,"direct-democratic","direct",3.0,178.5,"Central Isle Region straddling the antimeridian."),
 ("sable-group","Sable Group","region.myriad-isles",87,"direct-democratic","sortition",-5.0,-175.0,"Eastern Isle Region; hydrothermal research hub."),

 ("highmarch","Highmarch","region.veydra",88,"direct-democratic","sortition",-52.0,-40.0,"Veydran highland Region; scientific commons and the Ice Cap's guardian jurisdiction."),
 ("austral-shore","Austral Shore","region.veydra",52,"direct-democratic","sortition",-62.0,-62.0,"Coastal Veydran Region facing the Austral Ocean."),

 ("orbital-territory","Orbital Territory",None,28,"delegate-council","rotation",None,None,"The off-world Region: Kalyra settlements, orbital habitats, and Tyrran Belt stations. Its constitutional position is unsettled (dipl.external)."),
]

regions = []
for slug, name, cont, pop, form, method, lat, lon, summary in R:
    e = {
        "id": f"polity.{slug}", "name": name, "summary": summary,
        "sources": ["gov.regions"], "tags": ["region"],
        "population": pop * 1_000_000,
        "governingForm": f"gov.form-{form}",
        "delegateSelection": f"gov.delegate-{method}",
        "councilSeats": 4,
    }
    if cont:
        e["regions"] = [cont]
    else:
        e["tags"] = ["region", "off-world"]
    if lat is not None:
        e["labelPoint"] = {"lat": lat, "lon": lon}
    regions.append(e)

doc = {
  "schemaVersion": "1.0.0", "dataVersion": "1.1.0",
  "id": "gov.regions-data",
  "name": "Regions, Local Government, and Public Administration",
  "summary": "The 34 constituent Regions of the Concord, the four tiers of government, governing forms, the civil service, and integrity systems.",
  "sources": ["gov.regions", "gov.administration"],
  "asOf": "EY-0412-M08-D16",
  "units": {"population": "individuals", "term": "Elysian years"},
  "tiers": [
    {"id": "gov.tier-concord", "name": "Concord", "summary": "Planetary tier; the ten enumerated powers.", "sources": ["gov.regions"], "count": 1, "typicalPopulation": 7250000000, "shareOfPublicServantsPct": 1.9, "shareOfPublicSpendingPct": 22},
    {"id": "gov.tier-region", "name": "Region", "summary": "Constituent units; health, education, housing, policing, land use, most taxation.", "sources": ["gov.regions"], "count": 34, "typicalPopulation": 213000000, "shareOfPublicServantsPct": 21},
    {"id": "gov.tier-district", "name": "District", "summary": "Delivery tier; hospitals, schools, transit, utilities, planning.", "sources": ["gov.regions"], "count": 1104, "typicalPopulation": 6600000, "shareOfPublicServantsPct": 63},
    {"id": "gov.tier-commune", "name": "Commune", "summary": "Neighbourhood tier; public space, local services, participatory allocation.", "sources": ["gov.regions"], "count": 47900, "typicalPopulation": 151000, "shareOfPublicServantsPct": 14}
  ],
  "subsidiarityTest": [
    {"id": "gov.subsidiarity-capability", "name": "Can the lower tier do this at all?", "summary": "If yes, the enquiry usually ends.", "sources": ["gov.regions"], "order": 1},
    {"id": "gov.subsidiarity-boundary", "name": "Does the problem cross the lower tier's boundary?", "summary": "Atmosphere does; refuse collection does not.", "sources": ["gov.regions"], "order": 2},
    {"id": "gov.subsidiarity-fragmentation", "name": "Would fragmentation impose costs the gain does not justify?", "summary": "The only economic question, and deliberately the third one.", "sources": ["gov.regions"], "order": 3},
    {"id": "gov.subsidiarity-reversibility", "name": "Is the transfer reversible?", "summary": "Irreversible centralization requires a Tier 2 amendment. About a third of competence disputes turn on this alone.", "sources": ["gov.regions"], "order": 4}
  ],
  "governingForms": [
    {"id": "gov.form-assembly-executive", "name": "Assembly-Executive", "summary": "Elected assembly choosing a small collegial executive; commonest form.", "sources": ["gov.regions"], "regionCount": 16},
    {"id": "gov.form-assembly-manager", "name": "Assembly-Manager", "summary": "Elected assembly sets policy, a professionally appointed manager executes on fixed contract. Highest service delivery, lowest public trust, unexplained.", "sources": ["gov.regions"], "regionCount": 9},
    {"id": "gov.form-direct-democratic", "name": "Direct-democratic", "summary": "Frequent binding referendums with a small standing council.", "sources": ["gov.regions"], "regionCount": 5},
    {"id": "gov.form-delegate-council", "name": "Delegate council", "summary": "Governed by delegates from its Districts, with no separately elected regional body.", "sources": ["gov.regions"], "regionCount": 4}
  ],
  "delegateSelectionMethods": [
    {"id": "gov.delegate-assembly", "name": "Elected by the regional assembly", "summary": "", "sources": ["gov.regions"], "regionCount": 19},
    {"id": "gov.delegate-direct", "name": "Directly elected by the regional electorate", "summary": "", "sources": ["gov.regions"], "regionCount": 9},
    {"id": "gov.delegate-sortition", "name": "Selected by a sortition panel from a qualified pool", "summary": "", "sources": ["gov.regions"], "regionCount": 4},
    {"id": "gov.delegate-rotation", "name": "Rotated among District heads on a fixed schedule", "summary": "", "sources": ["gov.regions"], "regionCount": 2}
  ],
  "regionalFloors": [
    {"id": "gov.floor-elected", "name": "Government by an elected body", "summary": "On a franchise no narrower than the Concord's.", "sources": ["gov.regions"]},
    {"id": "gov.floor-rights", "name": "Charter rights fully enforceable", "summary": "", "sources": ["gov.regions"]},
    {"id": "gov.floor-audit", "name": "An independent audit body", "summary": "One the regional government cannot appoint, fund, or discipline.", "sources": ["gov.regions"]},
    {"id": "gov.floor-records", "name": "Publication of records to the Concord standard", "summary": "", "sources": ["gov.regions"]}
  ],
  "regions": regions,
  "commune": {
    "participatoryAllocationSharePct": [8, 15],
    "participationRatePct": 31,
    "votingAgeEY": 16,
    "localObjection": "A Commune may compel a published response and public hearing on any District or Regional decision affecting it, but cannot block."
  },
  "compacts": {
    "active": 340,
    "summary": "Binding agreements between Regions requiring no planetary approval; must be registered and published.",
    "mayBindNonParties": False
  },
  "portfolios": [
    {"id": "gov.portfolio-atmosphere-ocean", "name": "Atmosphere and Ocean", "summary": "The Article 12 climate and ocean systems.", "sources": ["gov.administration"]},
    {"id": "gov.portfolio-commons-orbit", "name": "Commons and Orbit", "summary": "Deep ocean, polar ice, orbital space, off-world territory.", "sources": ["gov.administration"]},
    {"id": "gov.portfolio-resilience-defence", "name": "Resilience and Defence", "summary": "Defence, disarmament verification, disaster response.", "sources": ["gov.administration"], "answeredBy": ["phase-12"]},
    {"id": "gov.portfolio-biosecurity", "name": "Biosecurity and Health Security", "summary": "Epidemic response and pathogen governance.", "sources": ["gov.administration"], "answeredBy": ["phase-09"]},
    {"id": "gov.portfolio-networks", "name": "Networks", "summary": "Interregional transport, grid, and communications backbone.", "sources": ["gov.administration"], "answeredBy": ["phase-10"]},
    {"id": "gov.portfolio-treasury-materials", "name": "Treasury and Materials", "summary": "Currency, monetary policy, Constrained List, strategic reserves.", "sources": ["gov.administration"], "answeredBy": ["phase-06"]},
    {"id": "gov.portfolio-rights-legal", "name": "Rights and Legal Affairs", "summary": "Rights enforcement, legislative drafting, Court liaison.", "sources": ["gov.administration"], "answeredBy": ["phase-05"]},
    {"id": "gov.portfolio-external", "name": "External Relations", "summary": "Diplomacy, treaties, first-contact preparedness.", "sources": ["gov.administration"], "answeredBy": ["phase-15"]},
    {"id": "gov.portfolio-public-administration", "name": "Public Administration", "summary": "The civil service, records, and delivery standards.", "sources": ["gov.administration"]}
  ],
  "civilService": {
    "totalPublicServants": 579000000,
    "shareOfLabourForcePct": 16.0,
    "entry": "open competitive examination in all 41 registered languages",
    "politicalAppointmentsBelowBoard": False,
    "tenureProtected": True,
    "politicalActivityPermittedOutsideOffice": True,
    "exposedPostRotationYears": 5,
    "exposedPostReturnBarYears": 15,
    "shareOfTimeOnReasonsDocumentationPct": 9,
    "correctionNote": "Corrected in Phase 6B: the Phase 4B figure of 43.1 million was arithmetically inconsistent with a population of 7.25 billion providing universal healthcare, education, and housing."
  },
  "integritySystems": [
    {"id": "gov.integrity-open-contracting", "name": "Open contracting by default", "summary": "Every contract at every tier published in machine-readable form within 30 days; no exemption threshold; price redaction capped at 3 years and itself published.", "sources": ["gov.administration"], "originEvent": "hist.event-corran-scandal"},
    {"id": "gov.integrity-asset-disclosure", "name": "Asset and interest disclosure", "summary": "Annual, on leaving office, and again at 2 and 5 years afterwards — because the payoff usually arrives later than the favour.", "sources": ["gov.administration"]},
    {"id": "gov.integrity-conflict-registry", "name": "The conflict registry", "summary": "Conflicts must be registered before acting; acting on an unregistered conflict is an offence independent of the underlying decision.", "sources": ["gov.administration"]},
    {"id": "gov.integrity-two-key", "name": "Two-key authorisation", "summary": "No single official may authorise a payment, licence, or consent above a modest threshold; the second key comes from a different reporting line and pairings are randomised.", "sources": ["gov.administration"]},
    {"id": "gov.integrity-random-audit", "name": "Random deep audit", "summary": "2% of public bodies selected annually by public verifiable lot for full unannounced audit. Purpose is uncertainty, not detection efficiency.", "sources": ["gov.administration"], "annualSharePct": 2},
    {"id": "gov.integrity-protected-disclosure", "name": "Protected disclosure", "summary": "Retaliation is criminal with reversed burden of proof: adverse treatment within 3 years of disclosure is presumed retaliatory. Anonymous disclosure protected equally.", "sources": ["gov.administration"]},
    {"id": "gov.integrity-cooling-off", "name": "Cooling-off with continuing salary", "summary": "10 years for office heads, 5 for exposed posts and Board members, paid — because an unpaid restriction restricts only those who cannot afford it.", "sources": ["gov.administration"]}
  ],
  "integrityOutcomes": {
    "procurementValueFlaggedPct": 0.7,
    "valueRecoveredPct": 0.4,
    "prosecutionsPerYear": 1340,
    "convictionRatePct": 61,
    "adverseAuditOpinionsPct": 2.1,
    "residentsAskedForBribePct": 0.3,
    "believeCorruptionCommonInDistrictPct": 11,
    "believeCorruptionCommonAtConcordPct": 19,
    "note": "Corruption is small, prosecuted, and mostly petty. The Audit Service states in every annual report that the residual rate is not zero and will not become zero. Perception exceeds measured reality and rises with distance from the resident."
  },
  "transparency": {
    "publicationDefault": "open",
    "exemptions": ["active security operations", "personal data", "live commercial negotiation", "legal privilege"],
    "exemptionsTimeLimited": True,
    "deliberativeMaterialOpensAfterYears": 3,
    "permanentCabinetSecrecy": False,
    "refusalLedgerPublished": True,
    "appealOverturnRatePct": 34,
    "failureReportingRequired": True,
    "failureReportingNote": "Bodies that publish no failures are audited on that basis; a flawless self-report is treated as evidence of inattention or concealment."
  },
  "digitalAdministration": {
    "publiclyBuiltAndOperated": True,
    "sourcePublished": True,
    "rationale": "A state that cannot read its own systems cannot be audited, and a state that cannot leave a supplier is governed by it.",
    "automatedDecisionConstraints": [
      "an identified human official is accountable for every decision affecting rights",
      "the reasons requirement applies identically to automated decisions",
      "any person may demand non-automated reconsideration"
    ],
    "answeredBy": ["phase-13"]
  },
  "knownWeaknesses": [
    {"id": "gov.weakness-interregional-inequality", "name": "Interregional inequality", "summary": "Floors without ceilings lets wealthy Regions race ahead; equalization narrows but does not close the gap.", "sources": ["gov.regions"], "answeredBy": ["phase-06"]},
    {"id": "gov.weakness-capacity-asymmetry", "name": "Capacity asymmetry", "summary": "Small Regions cannot staff competences they legally hold; Concord-funded shared services are criticised as centralization by the back door.", "sources": ["gov.regions"]},
    {"id": "gov.weakness-comparability-distortion", "name": "Comparability distortion", "summary": "Published league tables reward measurable outcomes and can starve the unmeasurable.", "sources": ["gov.regions"], "answeredBy": ["phase-16"]},
    {"id": "gov.weakness-orbital-anomaly", "name": "Orbital Territory anomaly", "summary": "A Region defined by installations rather than territory strains every assumption in Article 3.", "sources": ["gov.regions"], "answeredBy": ["phase-15"]},
    {"id": "gov.weakness-boundary-conservatism", "name": "Boundary conservatism", "summary": "Founding watershed boundaries no longer match settlement in three Regions; correction is slow.", "sources": ["gov.regions"]},
    {"id": "gov.weakness-compact-opacity", "name": "Compact opacity", "summary": "340 compacts are published but rarely read, and can shape obligations without planetary debate.", "sources": ["gov.regions"]},
    {"id": "gov.weakness-documentation-burden", "name": "Documentation burden", "summary": "9% of civil service time goes to producing reasons; permanently contested.", "sources": ["gov.administration"]},
    {"id": "gov.weakness-rotation-expertise", "name": "Rotation versus expertise", "summary": "Five-year rotation removes mastery from the posts where mastery is most useful.", "sources": ["gov.administration"]},
    {"id": "gov.weakness-perception-gap", "name": "Perception gap", "summary": "Trust in the planetary tier is lower than its measured performance; unexplained and unfixed.", "sources": ["gov.administration"]},
    {"id": "gov.weakness-attention", "name": "Publication without readership", "summary": "The Concord has solved disclosure and not solved attention. A right of access is worth what someone's willingness to read is worth.", "sources": ["gov.administration"], "answeredBy": ["phase-14"]}
  ]
}

with open('data/regions.json', 'w') as f:
    json.dump(doc, f, indent=2)

print("regions:", len(regions))
print("population sum:", sum(r['population'] for r in regions))
