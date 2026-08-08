import json

TW = 44.0
mix = [
    ("fusion", "Fusion", 58, None, "Deuterium-tritium, magnetically confined; fuel-limited rather than flux-limited."),
    ("solar", "Solar", 20, "resource.solar", "Concentrated in the Sirocc Basin, whose arrays also power the lithium brine operations beneath them."),
    ("wind", "Wind", 9, "resource.wind", "Overwhelmingly austral and offshore, in the Ferrel westerly belt and the Austral storm track."),
    ("geothermal", "Geothermal", 7, "resource.geothermal", "Follows the plate margins; supplies both electricity and direct heat."),
    ("tidal", "Tidal", 3, "resource.tidal", "Built out toward its physical limit because Kalyra's tides are predictable centuries in advance."),
    ("hydro", "Hydro", 2, "resource.hydro", "Alcyon system and Thalassar Rim orographic runoff."),
    ("marine", "Marine thermal and current", 1, "resource.marine-thermal", "Solward Current thermal and kinetic extraction."),
]
potentials = {"resource.solar":1900,"resource.wind":310,"resource.geothermal":62,
              "resource.hydro":4.1,"resource.tidal":2.8,"resource.marine-thermal":1.4}

sources=[]
for slug,name,share,res,summary in mix:
    out_tw = round(TW*share/100, 2)
    e = {"id": f"energy.source-{slug}", "name": name, "summary": summary,
         "sources": ["energy.generation"], "sharePct": share, "outputTW": out_tw}
    if res:
        e["resource"] = res
        e["shareOfTechnicalPotentialPct"] = round(out_tw/potentials[res]*100, 1)
    sources.append(e)

storage = [
    ("thermal","Thermal storage",34,"Molten salt, rock, and district heat stores; hours to days for industrial and district heat."),
    ("pumped-gravity","Pumped hydro and gravity",27,"Hours to days; the Thalassar Rim and Cindral Arc provide the head."),
    ("flow-battery","Flow batteries",21,"Minutes to hours; grid stabilisation."),
    ("hydrogen","Hydrogen and synthetic fuel",14,"Weeks to seasons; the long-duration seasonal reserve, deliberately inefficient."),
    ("electrochemical","Fixed electrochemical",4,"Sub-second to minutes; frequency response."),
]

doc = {
  "schemaVersion":"1.0.0","dataVersion":"1.1.0",
  "id":"energy.energy-data",
  "name":"Energy System of the Elysian Concord",
  "summary":"Demand, the generation mix, the fusion fleet and its beryllium constraint, the four-layer grid, storage, resilience failures, and energy pricing.",
  "sources":["energy.generation","energy.grid"],
  "asOf":"EY-0412-M08-D16",
  "units":{"power":"TW unless stated","energy":"TWh","time":"civil hours or Elysian years as stated"},
  "demand":{
    "meanPlanetaryTW": TW,
    "perCapitaW": 6070,
    "peakToMeanRatio": 1.31,
    "electricitySharePct": 91,
    "gcpSharePct": 6,
    "loadShape": "Two peaks and two troughs, following biphasic sleep: a morning rise, a pronounced dip through the Stillness, a long second-waking peak, and a deep overnight trough.",
    "stillnessDipNote": "The Stillness trough arrives in the middle of the solar day at a predictable time every day, and grid operators schedule storage charging and industrial heat around it."
  },
  "generationMix": sources,
  "fusion":{
    "id":"energy.fusion-fleet","name":"The fusion fleet",
    "summary":"6,200 magnetically confined deuterium-tritium plants averaging 4.1 GW, operated as public enterprises.",
    "sources":["energy.generation"],"tags":["fusion","public-enterprise"],
    "plants":6200,"meanCapacityGW":4.1,"totalOutputTW":25.5,
    "capacityFactor":0.86,"designLifeYears":60,
    "firstCommercialEY":103,"gridTransitionCompleteEY":158,
    "ownership":"econ.form-public-enterprise",
    "fuels":{"deuterium":"resource.deuterium","breeder":"resource.lithium",
             "neutronMultiplier":"resource.beryllium","plasmaFacing":"resource.tungsten"},
    "berylliumGrossConsumptionTPerYear":30000,
    "berylliumNetVirginDrawTPerYear":7500,
    "berylliumRecoveryRatePct":75,
    "berylliumHorizonWithoutRecoveryYears":30,
    "berylliumHorizonYears":120,
    "berylliumPosition":"The Concord has about a century to solve this and no current solution. Substitution has not matched beryllium, recovery is near its ceiling because neutron-activated beryllium is hard to reprocess, and off-world sourcing is a hope with a budget rather than a plan.",
    "runawayFailureMode": False,
    "longLivedHighLevelWaste": False,
    "activatedMaterialManagementYears":120,
    "significantReleaseIncidents":[{"ey":219,"contained":True,"deaths":0},{"ey":302,"contained":True,"deaths":0}]
  },
  "renewableFunctions":[
    {"id":"energy.function-distributed","name":"Distributed generation","summary":"Solar and small wind at Commune and District scale, on rooftops, over car parks and rail corridors, and in agricultural dual use. This is what makes microgrid islanding possible.","sources":["energy.generation"]},
    {"id":"energy.function-remote-siting","name":"Siting where fusion cannot go","summary":"The Myriad Isles, Northreach, Austral Shore, and thousands of remote settlements run on local renewables and storage rather than distant transmission.","sources":["energy.generation"]},
    {"id":"energy.function-load-following","name":"Load-following","summary":"Fusion runs best at steady output; solar, wind, and hydro absorb variation while tidal supplies the scheduled component.","sources":["energy.generation"]}
  ],
  "capacityBelowRegionalGridPct":34,
  "gridLayers":[
    {"id":"energy.layer-backbone","name":"Planetary backbone","summary":"HVDC links between continents and Regions, balancing across time zones and weather systems.","sources":["energy.grid"],"operator":"gov.portfolio-networks","capacityTW":9.4,"longestLinkKm":11400,"transmissionLossPct":4.1},
    {"id":"energy.layer-regional","name":"Regional grids","summary":"Bulk transmission and regional balancing.","sources":["energy.grid"],"mustSurvive":"loss of the backbone indefinitely at 80% of normal load"},
    {"id":"energy.layer-district","name":"District networks","summary":"Distribution.","sources":["energy.grid"],"mustSurvive":"loss of the regional grid for 30 days at 60% of load"},
    {"id":"energy.layer-microgrid","name":"Commune microgrids","summary":"Local generation, storage, and critical loads.","sources":["energy.grid"],"mustSurvive":"loss of everything above for 14 days at 100% of critical load","islandingDays":14}
  ],
  "grid":{
    "governingRequirement":"Every layer must be able to lose the layer above it.",
    "statutoryReserveMarginPct":22,
    "currentReserveMarginPct":24.6,
    "generationMayOwnTransmission": False,
    "islandingDrillAnnual": True,
    "islandingDrillUnannounced": True,
    "communesFailingDrillPct":6.1,
    "failuresConcentratedIn":["polity.northreach","polity.austral-shore"],
    "redundancyPremiumPct":11,
    "redundancyArgument":"A grid optimised only for cost is a grid that has never been asked what happens afterwards."
  },
  "storage":{
    "totalTWh":2140,
    "planetaryCoverCivilHours":48.6,
    "criticalLoadCoverCivilDays":21,
    "roundTripEfficiencyPct":71,
    "longDayStoragePenaltyPct":8,
    "seasonalReserveDeliberatelyInefficient": True,
    "media":[{"id":f"energy.storage-{s}","name":n,"summary":d,"sources":["energy.grid"],"capacitySharePct":p} for s,n,p,d in storage]
  },
  "gridEmergencies":[
    {"id":"energy.event-kessandra-blackout","name":"The Kessandra Blackout","summary":"A protection-relay misconfiguration propagated across northern Elandris, taking 380 million people off supply for up to 60 civil hours. Islanding largely failed because most Communes had never tested it.","sources":["energy.grid"],"ey":271,"affected":380000000,"durationCivilHours":60,"regions":["polity.kessandra"],"produced":["mandatory annual islanding drill","published failure register","statutory 22% reserve margin"]},
    {"id":"energy.event-vail-cascade","name":"The Vail Cascade","summary":"A winter storm brought down three Aurorian backbone links in nine hours. Islanding worked, with 94% of affected Communes sustaining critical load; restoration took 31 days because spare high-voltage transformer stock had fallen to eleven units planet-wide.","sources":["energy.grid"],"ey":344,"restorationDays":31,"communesSustainingCriticalLoadPct":94,"regions":["polity.vailmark"],"produced":["two-year strategic reserves of grid components"]}
  ],
  "nonElectricEnergy":[
    {"id":"energy.synthetic-hydrocarbons","name":"Synthetic hydrocarbons","summary":"Made from atmospheric carbon using fusion electricity for aviation, long-distance shipping, and a few industrial processes. The carbon is drawn down and returned, so the cycle is closed and the fuel is not fossil.","sources":["energy.generation"],"fossil": False,"retainedCarbonAffected": False},
    {"id":"energy.hydrogen","name":"Hydrogen","summary":"High-temperature industrial processes and long-duration storage.","sources":["energy.generation"]},
    {"id":"energy.direct-heat","name":"Direct fusion heat","summary":"Piped to co-located industry and to district heating; 71% of Aurorian buildings are heated from a plant rather than individually.","sources":["energy.generation"],"aurorianDistrictHeatingPct":71}
  ],
  "pricing":{
    "model":"three-part tariff",
    "baselineAllowanceFree": True,
    "householdsNeverExceedingAllowancePct":61,
    "baselineCovers":["lighting","cooking","refrigeration","communications","heating to a defined comfort standard","hot water"],
    "baselineRationale":"Not a subsidy but the delivery mechanism for the commons limb of Charter right 12: a household without power in Northreach in Tavric is not participating in civic life.",
    "deliversRight":"gov.right-commons",
    "usageChargeBanded": True,
    "capacityChargeFundsConstruction": True,
    "industrialMaterialsSurcharge":"econ.tax-constrained-list",
    "designIntent":"Energy in the Concord is cheap and materials are not, and the price system is designed to make that distinction impossible to miss."
  },
  "knownWeaknesses":[
    {"id":"energy.weakness-beryllium","name":"Beryllium","summary":"A century of headroom and no solution; substitution has not worked, recovery is near its ceiling, off-world supply is unproven.","sources":["energy.generation"],"answeredBy":["phase-15"]},
    {"id":"energy.weakness-tidal-ceiling","name":"Tidal near ceiling","summary":"At 47% of technical potential, with remaining sites inside protected areas that canon does not expect to open.","sources":["energy.generation"]},
    {"id":"energy.weakness-seismic-siting","name":"Fusion siting in seismic zones","summary":"Cindral and Thalassar Rim plants sit where the demand is, which is also where the earthquakes are.","sources":["energy.generation"]},
    {"id":"energy.weakness-activated-inventory","name":"Activated material inventory","summary":"A 120-year management obligation on a growing inventory with no agreed permanent disposal route — deferred rather than solved.","sources":["energy.generation"]},
    {"id":"energy.weakness-capacity-plateau","name":"Capacity factor plateau","summary":"Fleet capacity factor has sat at 0.85-0.87 for sixty years; further gains need designs the beryllium constraint makes unaffordable to prototype.","sources":["energy.generation"]},
    {"id":"energy.weakness-renewable-materials","name":"Renewable materials footprint","summary":"Distributed solar and wind consume indium, gallium, and rare earths, so the renewable share cannot expand without worsening a different scarcity. Every path forward is a trade between two scarcities.","sources":["energy.generation"]},
    {"id":"energy.weakness-islanding-failures","name":"Islanding failures","summary":"6.1% of Communes failed the 14-day drill, concentrated in the Regions least able to fix it.","sources":["energy.grid"]},
    {"id":"energy.weakness-reserve-gaming","name":"Reserve margin gaming","summary":"Regions count assets toward the 22% margin that are unavailable in the conditions that would need them; flagged three times without a satisfactory definition emerging.","sources":["energy.grid"]},
    {"id":"energy.weakness-storage-losses","name":"Storage round-trip losses","summary":"71% fleet efficiency wastes energy on a scale that would be indefensible if energy were scarce.","sources":["energy.grid"]},
    {"id":"energy.weakness-backbone-concentration","name":"Backbone concentration","summary":"9.4 TW across a small number of very long links; the Vail Cascade showed three failures can matter.","sources":["energy.grid"]},
    {"id":"energy.weakness-component-base","name":"Transformer and component lead times","summary":"The manufacturing base for the largest HVDC components sits in four Regions, which sits uneasily with two-source sufficiency.","sources":["energy.grid"]},
    {"id":"energy.weakness-untested-premium","name":"Cost of redundancy is never independently tested","summary":"The 11% islanding premium is estimated by the institution that requires the islanding, with no counterfactual grid to check it against.","sources":["energy.grid"]}
  ]
}

with open('data/energy.json','w') as f: json.dump(doc,f,indent=2)
print("mix shares:", sum(s['sharePct'] for s in sources))
print("mix output TW:", round(sum(s['outputTW'] for s in sources),2), "vs", TW)
print("storage shares:", sum(m['capacitySharePct'] for m in doc['storage']['media']))
