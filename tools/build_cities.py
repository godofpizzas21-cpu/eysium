import json

# (slug, name, polity, lat, lon, population, tags, summary)
C = [
 # --- Meridia ---
 ("sennary","Sennary","polity.meridian",28.0,-10.0,1_400_000,["capital-function","civic"],
  "Purpose-built seat of the Assembly on the Alcyon estuary, within sight of the Meridian Stone. Kept deliberately small."),
 ("alcyon-mouth","Alcyon Mouth","polity.ilvaret",13.0,1.0,9_100_000,["port","river"],
  "Delta port at the end of the River Alcyon; the oldest continuously inhabited urban site on Elysium after Ilvaret itself."),
 ("ilvaret-new","New Ilvaret","polity.ilvaret",15.5,3.5,4_200_000,["heritage"],
  "Modern city beside the excavated ruins of Ilvaret, the first city, whose collapse in 1,900 BE remains the formative memory of Elysian culture."),
 ("kelvaran","Kelvaran","polity.alcyone",21.0,4.5,7_800_000,["river","agricultural"],
  "Middle-Alcyon city and centre of the flow-share tradition."),
 ("siroccar","Siroccar","polity.sirocc",25.5,7.0,3_100_000,["desert","energy"],
  "Desert city serving the Sirocc solar arrays and the lithium brine fields beneath them."),
 ("cindral-gate","Cindral Gate","polity.cindral",9.0,33.0,6_400_000,["montane","geothermal"],
  "Mountain city at the principal pass through the Cindral Arc; geothermal-heated and seismically engineered."),
 ("kethran-vale","Kethran Vale","polity.kethran",-4.5,27.5,5_200_000,["upland"],
  "Eastern Meridian upland centre."),
 ("meridian-plain-city","Tessarel","polity.meridian",31.0,-14.0,11_200_000,["agricultural","rail"],
  "Largest city of the Meridian Plain and the freight hub of western Meridia."),
 ("verdanne-edge","Verdanne Edge","polity.verdanne",-11.0,9.0,2_900_000,["rainforest","research"],
  "Research city on the margin of the Verdanne, gateway to the inviolable core."),
 ("amarath-port","Amarath Port","polity.amarath-coast",-2.5,39.0,8_600_000,["port"],
  "Principal Meridian port on the Amarant Ocean."),
 ("sudmark-crossing","Sudmark Crossing","polity.sudmark",-20.5,-5.0,4_800_000,["savanna"],
  "Southern Meridian junction city."),

 # --- Elandris ---
 ("kessandra-reach","Kessandra Reach","polity.kessandra",2.5,111.0,21_400_000,["megacity","monsoon","port"],
  "Largest city on Elysium at 21.4 million; monsoon lowland delta metropolis and the Concord's densest urban region."),
 ("andrivar","Andrivar","polity.andriel",-8.5,127.0,12_100_000,["capital-function"],
  "Seat of the five Independent Offices, chosen for the Concord's most populous continent."),
 ("serrance-city","Serrance","polity.serrance",-28.5,149.5,9_700_000,["storm-coast","port"],
  "The most cyclone-exposed large city on the planet, built to a 285 km/h design basis."),
 ("halvane-bay","Halvane Bay","polity.halvane",-18.5,119.5,10_400_000,["port","fishery"],
  "Amarant Upwelling fishery port and processing centre."),
 ("terrace-north-city","Ostervale","polity.terrace-north",6.5,131.0,8_200_000,["agricultural","terraced"],
  "Terraced-agriculture capital of northern Elandris."),
 ("terrace-south-city","Lundareth","polity.terrace-south",-12.5,139.5,7_100_000,["agricultural"],
  "Southern Terraces city."),
 ("mirran-city","Mirran","polity.mirran",-22.5,133.5,6_600_000,["interior"],
  "Interior Elandric city; first Region to adopt sortition for Council delegates."),
 ("oshaal-city","Oshaal","polity.oshaal",-32.0,125.5,5_800_000,["temperate"],
  "Southern Elandric temperate city."),
 ("delvane-city","Delvane","polity.delvane",10.5,141.5,6_100_000,["port"],
  "Northeastern Elandric coastal city."),

 # --- Thalassar ---
 ("tessarene","Tessarene","polity.mistral",18.5,-115.5,5_900_000,["capital-function","port"],
  "Seat of the Constitutional Court, on the Mistral Shelf coast."),
 ("mistral-harbour","Mistral Harbour","polity.mistral",16.0,-118.0,9_300_000,["port","fishery"],
  "Principal fishing port of the richest fishery on Elysium."),
 ("fjordmark-city","Kalthane","polity.fjordmark",40.5,-123.5,6_700_000,["fjord","hydro"],
  "Fjord city in the wettest inhabited landscape on the planet."),
 ("rimward-city","Rimward","polity.rimward",8.5,-105.5,5_400_000,["plateau"],
  "Interior plateau city behind the Thalassar Rim."),
 ("sablewater-city","Sablewater","polity.sablewater",-3.5,-119.5,4_900_000,["coastal"],
  "Southern Thalassari coastal city."),
 ("coronal-city","Coronal","polity.coronal",29.5,-109.5,3_800_000,["interior"],
  "Northern interior city governed by a council of District delegates."),

 # --- Auroria ---
 ("korrast","Korrast","polity.vailmark",51.5,77.5,4_600_000,["capital-function","industrial"],
  "Seat of the Council of Regions, in the mineral province where Elysian industry began."),
 ("vail-forge","Vail Forge","polity.vailmark",53.5,81.0,7_900_000,["industrial","mining"],
  "Principal industrial city of the Vail Spine; the cradle of the Vail Awakening."),
 ("seraphine","Seraphine","polity.serapht",57.5,95.5,6_300_000,["lake","snow-belt"],
  "Lake Serapht city in the lake-effect snow belt; district heating serves 94% of dwellings."),
 ("korren-city","Korren","polity.korren",48.5,109.5,5_100_000,["forest"],
  "Southern Aurorian broadleaf city."),
 ("northreach-station","Northreach","polity.northreach",67.5,87.5,1_100_000,["subpolar","remote"],
  "Subpolar centre; the Concord's longest emergency response times and its hardest winters."),
 ("hollen-city","Hollen","polity.hollen",60.5,65.5,3_400_000,["taiga"],
  "Western Aurorian taiga city."),

 # --- Myriad Isles ---
 ("orphir-reach","Orphir Reach","polity.orphir-group",3.0,178.0,2_100_000,["capital-function","island"],
  "Seat of the Monetary Authority, placed in the Isles because it belongs to no region's imperial past."),
 ("kaelis-town","Kaelis","polity.kaelis-group",-1.0,172.0,3_300_000,["island","stewardship"],
  "Largest Isle city and the birthplace of the ocean-stewardship traditions."),
 ("sable-anchorage","Sable Anchorage","polity.sable-group",-5.0,-175.5,1_600_000,["island","research"],
  "Hydrothermal research hub above the Myriad vent fields."),

 # --- Veydra ---
 ("highmarch-station","Highmarch","polity.highmarch",-51.5,-44.0,1_900_000,["research","cold"],
  "Principal Veydran city and administrative centre of the Veydran Commons."),
 ("austral-landing","Austral Landing","polity.austral-shore",-61.5,-61.0,900_000,["port","cold"],
  "Southernmost city on Elysium; supply port for the austral research network."),
]

seats = {
  "sennary": "gov.assembly",
  "korrast": "gov.council-of-regions",
  "tessarene": "gov.constitutional-court",
  "orphir-reach": "econ.monetary-authority",
}

cities = []
for slug, name, polity, lat, lon, pop, tags, summary in C:
    e = {
        "id": f"city.{slug}", "name": name, "summary": summary,
        "sources": ["city.urbanism"], "tags": tags,
        "population": pop,
        "polity": polity,
        "coordinates": {"lat": lat, "lon": lon},
    }
    if slug in seats:
        e["seatOf"] = seats[slug]
    if slug == "andrivar":
        e["seatOfNote"] = "Hosts the five Independent Offices."
    cities.append(e)

doc = {
  "schemaVersion": "1.0.0", "dataVersion": "1.0.0",
  "id": "city.cities-data",
  "name": "Cities, Settlement, and Housing",
  "summary": "Named cities with coordinates for the Atlas, the distributed capital, urban design standards, tenure and housing cost, homelessness, and subsea stations.",
  "sources": ["city.urbanism", "city.housing"],
  "asOf": "EY-0412-M08-D16",
  "units": {"population": "individuals", "coordinates": "decimal degrees", "area": "million km^2"},
  "settlement": {
    "urbanPopulation": 6_341_500_000,
    "urbanSharePct": 87.4,
    "builtEnvironmentMkm2": 2.54,
    "builtShareOfLandPct": 1.4,
    "meanUrbanDensityPerKm2": 5760,
    "citiesOverOneMillion": 412,
    "largestCity": "city.kessandra-reach",
    "policy": "More cities rather than bigger cities: a settlement pattern with a few dominant nodes has a small number of very expensive failure modes."
  },
  "distributedCapital": {
    "hasCapitalCity": False,
    "rationale": "A capital is a single point of failure, and so is a capital's political culture.",
    "seats": [
      {"institution": "gov.assembly", "city": "city.sennary"},
      {"institution": "gov.council-of-regions", "city": "city.korrast"},
      {"institution": "gov.constitutional-court", "city": "city.tessarene"},
      {"institution": "econ.monetary-authority", "city": "city.orphir-reach"}
    ],
    "independentOfficesCity": "city.andrivar"
  },
  "cities": cities,
  "urbanStandards": {
    "twentyMinuteStandard": {
      "id": "city.twenty-minute-standard",
      "name": "The twenty-minute standard",
      "summary": "Every dwelling within 20 civil minutes on foot or cycle of a health post, school, library, food market, green space, and transit stop. A Concord floor, audited per Commune.",
      "sources": ["city.urbanism"],
      "minutes": 20,
      "compliancePct": 94.1,
      "services": ["health post", "school", "library", "food market", "green space", "transit stop"]
    },
    "quarterPopulationRange": [20000, 60000],
    "polycentric": True,
    "stillnessAcousticLimitApplies": True,
    "stillnessRestrictions": ["deliveries", "construction", "through-traffic"],
    "greenSpaceWithinM": 300,
    "greenSpaceCompliancePct": 96.8,
    "darkSkyStandardsApplyInCities": True,
    "netGreenAreaLossPermitted": False
  },
  "buildingStandards": {
    "designLifeYears": 150,
    "defaultStructuralMaterialBelow12Storeys": "engineered timber",
    "offSiteManufacturePct": 68,
    "disassemblyRequired": True,
    "wholeBuildingMaterialPassport": True,
    "accessibilityAsBuilt": True,
    "subdividableAndRecombinable": True,
    "adaptabilityRationale": "A dwelling is expected to hold different numbers of people at different points in a 150-year life; Elysians move house far less often than Earth populations and reconfigure far more.",
    "accessibilityRationale": "710 million Elysians are over 100 EY and home-first healthcare depends on dwellings a frail person can be cared for in."
  },
  "land": {
    "urbanDistrictsWithPublicLandLeaseholdPct": 61,
    "leaseTermYears": 99,
    "leaseRenewalAutomatic": True,
    "renewalRefusalForGroundRentPermitted": False,
    "freeholdSubjectTo": ["law.substantive stewardship obligation", "econ.tax-land-value"],
    "purpose": "The building depreciates and is maintained; the land's value accrues to the Commune that created it."
  },
  "resilience": {
    "islandingDays": 14,
    "coolRefugePerCommune": True,
    "coolRefugeSizedForResidentsPct": 30,
    "cycloneDesignBasisKmh": 285,
    "cycloneRegions": ["polity.serrance", "polity.delvane", "polity.kaelis-group"],
    "floodDesignBasisReturnYears": 500,
    "floodRegions": ["polity.ilvaret", "polity.alcyone"],
    "retreatLinesPublished": True,
    "retreatLineBindingOnNewConstruction": True
  },
  "subseaStations": {
    "count": 41,
    "populationOnRotation": 41000,
    "areCities": False,
    "types": ["continental shelf research stations", "hydrothermal observatories", "undersea grid maintenance bases"],
    "canonNote": "Stations, not cities. No Elysian settlement of any size exists underwater, no one is born in one, and the Concord has never proposed subsea urbanisation. Living permanently below the sea is regarded as an expensive answer to a question nobody has."
  },
  "housing": {
    "households": 2132352941,
    "meanHouseholdSize": 3.4,
    "deliversRight": "gov.right-housing",
    "dutyBearer": "gov.tier-district",
    "adequacyCriteria": ["secure tenure", "affordable against income", "physically fit and warm", "accessible to the occupant's needs", "within the twenty-minute service set", "not conditional on behaviour"],
    "conditionalOnBehaviourPermitted": False,
    "tenure": [
      {"id": "city.tenure-owner", "name": "Owner-occupied", "summary": "", "sources": ["city.housing"], "sharePct": 44},
      {"id": "city.tenure-cooperative", "name": "Cooperative and mutual housing", "summary": "Members hold a right of occupancy rather than a tradeable asset, pay cost rent, and recover contributions indexed to construction costs rather than land values, so nobody profits from the shortage.", "sources": ["city.housing"], "sharePct": 24},
      {"id": "city.tenure-public", "name": "Public and social rented", "summary": "", "sources": ["city.housing"], "sharePct": 21},
      {"id": "city.tenure-private-rented", "name": "Private rented", "summary": "Indefinite tenancies by default, indexed rent caps, eviction only for specified cause through a court, and landlord licensing.", "sources": ["city.housing"], "sharePct": 11}
    ],
    "cost": {
      "medianShareOfIncomePct": 14.1,
      "cooperativeShareOfIncomePct": 11.2,
      "privateRentShareOfIncomePct": 19.4,
      "householdsOver30PctOfIncome": 3.9,
      "reasons": ["land value tax removes most speculative return", "leasehold separates land from building", "cooperatives price at cost", "off-site manufacture lowers construction cost", "supply is permitted and District duty is justiciable"]
    },
    "homelessness": {
      "experiencedInLastYear": 2200000,
      "shareOfPopulationPct": 0.03,
      "rehousedWithin30DaysPct": 84,
      "rehousedWithinSeasonPct": 11,
      "overOneYear": 94000,
      "approach": "housing first, unconditionally",
      "offerWithdrawnOnRefusal": False,
      "vagrancyOffenceExists": False,
      "canonNote": "Rare, brief, and non-punitive, and not eliminated. The residual is a problem of illness and autonomy that the housing system cannot solve alone."
    },
    "specialProvision": [
      {"id": "city.provision-release", "name": "Housing on release from custody", "summary": "Guaranteed and arranged before release, not applied for after.", "sources": ["city.housing"], "relatedTo": "law.supervision-order"},
      {"id": "city.provision-retreat", "name": "Managed retreat replacement", "summary": "Full replacement value with the Commune relocated together where residents choose.", "sources": ["city.housing"]},
      {"id": "city.provision-disaster", "name": "Emergency housing capacity", "summary": "Held at District level for 4% of District population and exercised annually.", "sources": ["city.housing"], "districtCapacityPct": 4, "answeredBy": ["phase-12"]},
      {"id": "city.provision-adaptation", "name": "Frailty adaptation", "summary": "Funded on assessment rather than on means, delivered within 45 days in 88% of cases.", "sources": ["city.housing"], "targetDays": 45, "onTimePct": 88}
    ]
  },
  "knownWeaknesses": [
    {"id": "city.weakness-twenty-minute-gap", "name": "The twenty-minute standard is not universal", "summary": "The 5.9% shortfall concentrates in older Elandric quarters and Aurorian settlements too small to support the services.", "sources": ["city.urbanism"]},
    {"id": "city.weakness-housing-wealth", "name": "Housing wealth still accumulates", "summary": "Leasehold and land value tax slow appreciation without stopping it; housing remains a principal driver of the flat wealth Gini.", "sources": ["city.urbanism", "city.housing"], "answeredBy": ["phase-16"]},
    {"id": "city.weakness-heritage-density", "name": "Heritage against density", "summary": "Communes hold real power over their own built form and some use it to prevent density the Region needs; there is no override and canon does not propose one.", "sources": ["city.urbanism"]},
    {"id": "city.weakness-retreat-lines", "name": "Retreat lines are contested", "summary": "A published retreat line lowers property value the day it is drawn; three Regions have litigated their own lines.", "sources": ["city.urbanism"]},
    {"id": "city.weakness-small-settlements", "name": "Small-settlement viability", "summary": "Below about 8,000 residents a settlement cannot support the full Commune service set; 6,100 settlements are subsidised to remain viable.", "sources": ["city.urbanism"]},
    {"id": "city.weakness-sennary", "name": "Sennary is unloved", "summary": "A capital nobody has a reason to move to is also a capital nobody knows; Concord-tier remoteness is partly architectural.", "sources": ["city.urbanism"]},
    {"id": "city.weakness-homelessness-residual", "name": "Homelessness is not zero", "summary": "94,000 people homeless for over a year; a health and autonomy problem the housing system cannot reach.", "sources": ["city.housing"]},
    {"id": "city.weakness-duty-enforcement", "name": "District duty is unevenly enforced", "summary": "The right is only as strong as a person's willingness to litigate, and take-up is lowest among those most affected.", "sources": ["city.housing"]},
    {"id": "city.weakness-cooperative-rationing", "name": "Cooperative entry is rationed", "summary": "The cheapest tenure has waiting lists averaging 2.4 Elysian years, and entry favours those with existing connections.", "sources": ["city.housing"]},
    {"id": "city.weakness-adaptation-delay", "name": "Adaptation delays", "summary": "12% wait beyond 45 days, concentrated in Regions with the oldest populations and thinnest administrations.", "sources": ["city.housing"]},
    {"id": "city.weakness-rural-housing", "name": "Rural housing quality", "summary": "Pre-standard housing concentrates in small Aurorian and Veydran settlements where replacement is uneconomic and subsidy has not closed the gap.", "sources": ["city.housing"]}
  ]
}

with open('data/cities.json', 'w') as f:
    json.dump(doc, f, indent=2)

print("cities:", len(cities))
print("tenure sum:", sum(t['sharePct'] for t in doc['housing']['tenure']))
print("largest:", max(cities, key=lambda c: c['population'])['name'],
      f"{max(c['population'] for c in cities):,}")
