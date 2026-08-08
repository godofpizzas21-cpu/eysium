import json, math

cities = {c["id"]: c for c in json.load(open('data/cities.json'))["cities"]}

def coord(cid):
    c = cities[cid]["coordinates"]
    return {"lat": c["lat"], "lon": c["lon"]}

def great_circle_km(a, b):
    la1, lo1 = math.radians(a["lat"]), math.radians(a["lon"])
    la2, lo2 = math.radians(b["lat"]), math.radians(b["lon"])
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 6510 * 2 * math.asin(math.sqrt(h))

# (slug, name, mode, speed, continent, [city ids in order], summary)
LINES = [
 ("alcyon-trunk","The Alcyon Trunk","maglev",620,"region.meridia",
  ["city.alcyon-mouth","city.ilvaret-new","city.kelvaran","city.sennary","city.meridian-plain-city"],
  "Follows the River Alcyon from the delta to the Meridian Plain, linking the oldest urban corridor on Elysium to the seat of the Assembly."),
 ("cindral-line","The Cindral Line","maglev",620,"region.meridia",
  ["city.meridian-plain-city","city.cindral-gate","city.kethran-vale","city.amarath-port"],
  "Crosses the Cindral Arc at its principal pass to reach the Amarant seaboard."),
 ("sirocc-spur","The Sirocc Spur","rail",280,"region.meridia",
  ["city.kelvaran","city.siroccar"],
  "Serves the Sirocc solar arrays and lithium brine fields."),
 ("verdanne-branch","The Verdanne Branch","rail",280,"region.meridia",
  ["city.sudmark-crossing","city.verdanne-edge"],
  "Terminates at the margin of the inviolable Verdanne core; no line enters the core."),
 ("meridia-south","The Sudmark Line","maglev",620,"region.meridia",
  ["city.sennary","city.sudmark-crossing","city.kethran-vale"],
  "Southern Meridian connector."),

 ("terrace-trunk","The Terrace Trunk","evacuated-tube",900,"region.elandris",
  ["city.kessandra-reach","city.terrace-north-city","city.andrivar","city.terrace-south-city","city.oshaal-city"],
  "The busiest passenger corridor on Elysium, running the length of the Elandric Terraces at 900 km/h."),
 ("serrance-line","The Serrance Line","maglev",620,"region.elandris",
  ["city.andrivar","city.mirran-city","city.serrance-city"],
  "Storm-coast line, engineered to the 285 km/h cyclone design basis along its final section."),
 ("elandris-west","The Halvane Line","maglev",620,"region.elandris",
  ["city.terrace-south-city","city.halvane-bay"],
  "Connects the Terraces to the Amarant Upwelling fishery ports."),
 ("elandris-northeast","The Delvane Line","rail",280,"region.elandris",
  ["city.kessandra-reach","city.delvane-city"],
  "Northeastern coastal line."),

 ("rim-line","The Rim Line","evacuated-tube",900,"region.thalassar",
  ["city.fjordmark-city","city.tessarene","city.mistral-harbour","city.sablewater-city"],
  "Runs the Thalassari seaboard past the seat of the Constitutional Court."),
 ("rimward-branch","The Rimward Branch","rail",280,"region.thalassar",
  ["city.tessarene","city.rimward-city","city.coronal-city"],
  "Climbs behind the Thalassar Rim to the interior plateau."),

 ("vail-trunk","The Vail Trunk","evacuated-tube",900,"region.auroria",
  ["city.hollen-city","city.korrast","city.vail-forge","city.seraphine","city.korren-city"],
  "Spine of the Aurorian industrial belt, linking the Council of Regions to the mineral province where Elysian industry began."),
 ("northreach-line","The Northreach Line","rail",280,"region.auroria",
  ["city.vail-forge","city.northreach-station"],
  "Subpolar line; the most weather-interrupted scheduled service in the Concord."),

 ("austral-link","The Austral Link","rail",280,"region.veydra",
  ["city.highmarch-station","city.austral-landing"],
  "The only railway on Veydra, serving the Veydran Commons research network."),
]

SEA = [
 ("sea-meridia-elandris","Meridia–Elandris sea lane","sea",30,
  ["city.amarath-port","city.halvane-bay"],
  "Principal bulk route between the Amarant seaboards."),
 ("sea-thalassar-elandris","Thalassar–Elandris sea lane","sea",30,
  ["city.mistral-harbour","city.kessandra-reach"],
  "Longest regular crossing; 4.7 Elysian days at service speed."),
 ("sea-meridia-thalassar","Meridia–Thalassar sea lane","sea",30,
  ["city.alcyon-mouth","city.sablewater-city"],
  "Solward Current route, historically the fastest under sail."),
 ("sea-auroria-thalassar","Auroria–Thalassar sea lane","sea",30,
  ["city.vail-forge","city.fjordmark-city"],
  "Boreal route carrying Vail Spine ore."),
 ("sea-isles-elandris","Isles–Elandris sea lane","sea",30,
  ["city.kaelis-town","city.delvane-city"],
  "Isle provisioning and launch-support route."),
 ("sea-veydra-thalassar","Veydra–Thalassar sea lane","sea",30,
  ["city.austral-landing","city.sablewater-city"],
  "Austral supply route; interrupted by winter storms 20-30 times a season."),
]

AIR = [
 ("air-sennary-andrivar","Sennary–Andrivar air corridor",
  ["city.sennary","city.andrivar"],
  "Governance corridor between the Assembly and the Independent Offices; 15.5 civil hours."),
 ("air-sennary-korrast","Sennary–Korrast air corridor",
  ["city.sennary","city.korrast"],
  "Assembly to Council of Regions."),
 ("air-sennary-tessarene","Sennary–Tessarene air corridor",
  ["city.sennary","city.tessarene"],
  "Assembly to Constitutional Court."),
 ("air-andrivar-orphir","Andrivar–Orphir Reach air corridor",
  ["city.andrivar","city.orphir-reach"],
  "Independent Offices to the Monetary Authority."),
]

def interpolate(a, b, n=14):
    """Great-circle interpolation for smooth rendering on a globe."""
    la1, lo1 = math.radians(a["lat"]), math.radians(a["lon"])
    la2, lo2 = math.radians(b["lat"]), math.radians(b["lon"])
    d = 2*math.asin(math.sqrt(math.sin((la2-la1)/2)**2 +
                              math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
    if d == 0:
        return [a]
    pts = []
    for i in range(n+1):
        f = i/n
        A = math.sin((1-f)*d)/math.sin(d); B = math.sin(f*d)/math.sin(d)
        x = A*math.cos(la1)*math.cos(lo1) + B*math.cos(la2)*math.cos(lo2)
        y = A*math.cos(la1)*math.sin(lo1) + B*math.cos(la2)*math.sin(lo2)
        z = A*math.sin(la1) + B*math.sin(la2)
        pts.append({"lat": round(math.degrees(math.atan2(z, math.hypot(x, y))), 3),
                    "lon": round(math.degrees(math.atan2(y, x)), 3)})
    return pts

def build_path(city_ids, dense):
    pts = []
    for i in range(len(city_ids)-1):
        a, b = coord(city_ids[i]), coord(city_ids[i+1])
        seg = interpolate(a, b) if dense else [a, b]
        pts.extend(seg if i == 0 else seg[1:])
    return pts

routes = []
for slug, name, mode, speed, continent, ids, summary in LINES:
    path = build_path(ids, dense=False)
    length = sum(great_circle_km(path[i], path[i+1]) for i in range(len(path)-1))
    routes.append({
        "id": f"route.{slug}", "name": name, "summary": summary,
        "sources": ["route.transport"], "tags": ["land", mode],
        "mode": mode, "serviceSpeedKmh": speed,
        "continent": continent, "stops": ids,
        "lengthKm": round(length), "path": path,
    })

for slug, name, mode, speed, ids, summary in SEA:
    unknown = [i for i in ids if i not in cities]
    if unknown:
        raise SystemExit(f"unknown city ids in route {slug}: {unknown}")
    path = build_path(ids, dense=True)
    length = sum(great_circle_km(path[i], path[i+1]) for i in range(len(path)-1))
    routes.append({
        "id": f"route.{slug}", "name": name, "summary": summary,
        "sources": ["route.gateways"], "tags": ["sea", mode],
        "mode": mode, "serviceSpeedKmh": speed,
        "stops": ids, "lengthKm": round(length), "path": path,
    })

for slug, name, ids, summary in AIR:
    path = build_path(ids, dense=True)
    length = sum(great_circle_km(path[i], path[i+1]) for i in range(len(path)-1))
    routes.append({
        "id": f"route.{slug}", "name": name, "summary": summary,
        "sources": ["route.gateways"], "tags": ["air", "governance"],
        "mode": "air", "serviceSpeedKmh": 850,
        "stops": ids, "lengthKm": round(length),
        "travelTimeCivilHours": round(length/850, 1), "path": path,
    })

doc = {
  "schemaVersion": "1.0.0", "dataVersion": "1.0.0",
  "id": "route.routes-data",
  "name": "Transport Networks of the Elysian Concord",
  "summary": "Passenger modal shares, urban mobility, continental maglev and rail corridors with path geometry, sea lanes, governance air corridors, ports, launch ranges, and freight.",
  "sources": ["route.transport", "route.gateways"],
  "asOf": "EY-0412-M08-D16",
  "units": {"distance": "km", "speed": "km/h", "coordinates": "decimal degrees",
            "time": "civil hours (1 civil hour = 3,586.15 SI seconds)"},
  "modalShares": {
    "passengerTrips": [
      {"id": "route.mode-walking", "name": "Walking", "summary": "", "sources": ["route.transport"], "sharePct": 41.0},
      {"id": "route.mode-urban-transit", "name": "Urban transit", "summary": "Metro, tram, and bus.", "sources": ["route.transport"], "sharePct": 24.0},
      {"id": "route.mode-cycling", "name": "Cycling", "summary": "On 1.9 million km of protected cycleway.", "sources": ["route.transport"], "sharePct": 22.0},
      {"id": "route.mode-interurban-rail", "name": "Interurban rail and maglev", "summary": "", "sources": ["route.transport"], "sharePct": 8.0},
      {"id": "route.mode-road-vehicle", "name": "Road vehicle", "summary": "", "sources": ["route.transport"], "sharePct": 4.4},
      {"id": "route.mode-air", "name": "Air", "summary": "Priced deliberately to stay small.", "sources": ["route.transport"], "sharePct": 0.6}
    ],
    "freightTonneKm": {"railAndMaglev": 61, "sea": 27, "road": 11, "air": 1}
  },
  "urbanMobility": {
    "householdsOwningRoadVehiclePct": 11,
    "protectedCyclewayKm": 1900000,
    "cycleShareRangePct": [9, 38],
    "pedestrianPriorityLiabilityPresumed": True,
    "cityCentresClosedToPrivateMotorTraffic": True,
    "transitFareFreeRegions": 27,
    "transitFareFreeOfRegions": 34,
    "transitFundedFrom": "econ.tax-land-value",
    "eveningServiceToHour": 23,
    "fundingRationale": "Transit creates the land value it is paid from."
  },
  "networkPolicy": {
    "trackIsPublicMonopoly": True,
    "operationsMayBePrivate": True,
    "maglevServiceSpeedKmh": 620,
    "evacuatedTubeServiceSpeedKmh": 900,
    "evacuatedTubeCorridors": 4,
    "passageStandards": {
      "wildlifeCrossingMaxIntervalKm": 4,
      "continuousBarrierPermitted": False,
      "darkSkyLightingRequired": True,
      "railCorridorsQualifyingAsConnectivityLandPct": 61
    }
  },
  "routes": routes,
  "autonomousVehicles": {
    "fatalitiesPerBillionVehicleKm": 0.11,
    "manualDrivingLawful": True,
    "manualShareOfVehicleKmPct": 3,
    "manualShareOfRoadDeathsPct": 34,
    "rules": [
      {"id": "route.av-accountable-operator", "name": "An identified operator is accountable", "summary": "No vehicle may operate without a named legal person answerable for its decisions.", "sources": ["route.transport"]},
      {"id": "route.av-log-custody", "name": "The decision log is not held by the manufacturer", "summary": "Records go to the Record Office, which manufacturers may request but not edit — the same arrangement as custodial recordings, for the same reason.", "sources": ["route.transport"], "custodian": "gov.record-office"},
      {"id": "route.av-no-identity-target", "name": "No optimisation target may include a person's identity", "summary": "A vehicle may not weigh who is in its path. Settled by the Constitutional Court in EY 318 as an application of equality before the law.", "sources": ["route.transport"], "settledEY": 318, "relatedTo": "gov.right-equality"}
    ]
  },
  "ruralAccess": {
    "scheduledServiceThresholdResidents": 400,
    "demandResponsiveBelowThreshold": True,
    "maxBookingLeadDays": 1,
    "leastReliableRegions": ["polity.northreach", "polity.austral-shore", "polity.sable-group"]
  },
  "freight": {
    "intensityVsIntegrationFraction": 0.33,
    "seaServiceSpeedKmhRange": [26, 34],
    "roadFreightMaxJourneyKm": 300,
    "justInTimeRejected": True,
    "strategicReserveYears": 2,
    "rationale": "A logistics system that cannot absorb a two-year interruption is an unfinished logistics system."
  },
  "ports": {
    "majorPorts": 340,
    "publiclyOwned": True,
    "operationsFranchised": True,
    "largest": ["city.kessandra-reach", "city.halvane-bay", "city.mistral-harbour", "city.fjordmark-city", "city.amarath-port", "city.alcyon-mouth", "city.vail-forge"],
    "topSevenShareOfIntercontinentalTonnagePct": 41,
    "disasterReceptionNoticeHours": 48,
    "biosecurityControlPoint": True
  },
  "aviation": {
    "airports": 210,
    "cruiseSpeedKmh": 850,
    "supersonicService": False,
    "supersonicEvaluations": 2,
    "fuel": "energy.synthetic-hydrocarbons",
    "fossil": False,
    "constraintIsCostNotEmissions": True
  },
  "intercontinental": {
    "fixedLinksExist": False,
    "longestRegularCrossingKm": 13485,
    "longestCrossingSeaCivilHours": 123,
    "longestCrossingSeaElysianDays": 4.7,
    "longestCrossingAirCivilHours": 15.9,
    "governanceConductedRemotelyByDefault": True,
    "translationLanguages": 41,
    "acknowledgedCost": "A legislature that mostly meets remotely is less collegial, forms fewer cross-regional relationships, and is worse at the informal negotiation that resolves disputes before they become positions. Identified by every Assembly review since EY 250; none has proposed a capital city."
  },
  "launchRanges": [
    {"id": "route.launch-kaelis", "name": "Kaelis Range", "summary": "Principal equatorial site and heavy lift; sits beside inviolable reef systems and its licence was contested for eleven years.", "sources": ["route.gateways"], "polity": "polity.kaelis-group", "coordinates": {"lat": -1.0, "lon": 172.0}, "capacitySharePct": 47, "answeredBy": ["phase-15"]},
    {"id": "route.launch-verdanne", "name": "Verdanne Range", "summary": "Secondary equatorial site; crewed launch.", "sources": ["route.gateways"], "polity": "polity.verdanne", "coordinates": {"lat": -11.0, "lon": 9.0}, "capacitySharePct": 24, "answeredBy": ["phase-15"]},
    {"id": "route.launch-sirocc", "name": "Sirocc Range", "summary": "High-inclination and polar orbits; dry, empty, and heavily instrumented.", "sources": ["route.gateways"], "polity": "polity.sirocc", "coordinates": {"lat": 25.5, "lon": 7.0}, "capacitySharePct": 19, "answeredBy": ["phase-15"]},
    {"id": "route.launch-austral", "name": "Austral Range", "summary": "Polar and retrograde launch supporting the observation constellations.", "sources": ["route.gateways"], "polity": "polity.austral-shore", "coordinates": {"lat": -61.5, "lon": -61.0}, "capacitySharePct": 10, "answeredBy": ["phase-15"]}
  ],
  "launchPolicy": {
    "isEnumeratedConcordPower": True,
    "maxSingleRangeCapacityPct": 60,
    "escapeVelocityKmS": 11.42,
    "propellant": "synthetic, manufactured on site with fusion electricity"
  },
  "knownWeaknesses": [
    {"id": "route.weakness-manual-driving", "name": "Manual driving disproportion", "summary": "3% of vehicle-km and 34% of road deaths, published annually with no proposal to prohibit; the reasons are cultural rather than analytical.", "sources": ["route.transport"]},
    {"id": "route.weakness-terrain-cycling", "name": "Cycle share varies with terrain", "summary": "38% in delta cities and 9% in Cindral; topography defeats policy.", "sources": ["route.transport"]},
    {"id": "route.weakness-rural-reliability", "name": "Rural reliability", "summary": "Weather-interrupted links in three Regions; the Charter guarantees access and cannot guarantee it on any given day.", "sources": ["route.transport"]},
    {"id": "route.weakness-corridor-land-take", "name": "Corridor land take", "summary": "Passage standards make corridors wider and dearer, and Communes resist new corridors even when the Region needs them.", "sources": ["route.transport"]},
    {"id": "route.weakness-tube-fragility", "name": "Evacuated-tube corridors are fragile", "summary": "Four corridors with a failure mode that closes the whole line for weeks; expansion has stalled twice.", "sources": ["route.transport"]},
    {"id": "route.weakness-fare-inequity", "name": "Fare-free is not planet-wide", "summary": "The seven Regions still charging are disproportionately those with the weakest fiscal capacity, so the poorest Regions charge the most.", "sources": ["route.transport"]},
    {"id": "route.weakness-remote-governance", "name": "Remote governance costs collegiality", "summary": "Identified by every Assembly review since EY 250, never solved, and the alternative is refused on principle.", "sources": ["route.gateways"]},
    {"id": "route.weakness-ocean-crossing", "name": "Ocean crossing is slow and dear", "summary": "Most Elysians never leave their continent, and canon does not claim this is entirely healthy for a planetary polity.", "sources": ["route.gateways"]},
    {"id": "route.weakness-aviation-cost", "name": "Aviation cost has never fallen", "summary": "Synthetic fuel keeps aviation clean and expensive; the Isles and Veydra bear the isolation.", "sources": ["route.gateways"]},
    {"id": "route.weakness-port-concentration", "name": "Port concentration", "summary": "Seven ports handle 41% of intercontinental tonnage, sitting uneasily with the Concord's redundancy doctrine.", "sources": ["route.gateways"]},
    {"id": "route.weakness-launch-concentration", "name": "Launch concentration", "summary": "Kaelis at 47% is within the cap and above where planners would like it; the alternatives are all worse-placed.", "sources": ["route.gateways"]},
    {"id": "route.weakness-port-rail-capacity", "name": "Freight rail capacity at ports", "summary": "The landward side of major ports is the tightest capacity constraint in Elysian logistics and has been for forty years.", "sources": ["route.gateways"]}
  ]
}

with open('data/routes.json', 'w') as f:
    json.dump(doc, f, indent=2)

print("routes:", len(routes))
print("passenger shares:", sum(m['sharePct'] for m in doc['modalShares']['passengerTrips']))
print("freight shares:", sum(doc['modalShares']['freightTonneKm'].values()))
print("launch shares:", sum(r['capacitySharePct'] for r in doc['launchRanges']))
print("total path points:", sum(len(r['path']) for r in routes))
