/**
 * The layer registry.
 *
 * This is the only place map layers are enumerated. The switcher, the URL
 * parser, the accessible tree, and the generated manifests all read from here,
 * so adding a layer is one entry plus a folder — see `eng.architecture` section 3.
 *
 * `indicators` are the canonical metric ids a layer surfaces. The pipeline
 * fails the build if a layer names a dataset or an indicator that does not
 * exist, so a layer cannot promise data the Bible does not hold.
 */

/**
 * Geometry a layer can draw. Each kind states what the source data must carry,
 * and the pipeline verifies it — a layer cannot promise geometry the Bible does
 * not hold.
 *
 *  arc            source entities need `path`
 *  latitude-band  source entities need `latitudeBandDeg`
 *  point          source entities need `coordinates` or `labelPoint`
 *  region-point   source entities need `regions`, resolved to their label points
 *  orbit          source entities need `orbitalDistanceKm`
 */
export type GeometryKind = "arc" | "latitude-band" | "point" | "region-point" | "orbit";

export interface LayerGeometry {
  kind: GeometryKind;
  /** Dot path into the dataset, e.g. `biomes.terrestrialBiomes`. */
  source: string;
  /** `palette` reads each entity's own colour; otherwise a token name. */
  colour: string;
  /** For `point`, a numeric field that scales the symbol. */
  scaleBy?: string;
}

export interface Layer {
  id: string;
  name: string;
  /** One line, shown in the switcher and read by the accessible tree. */
  summary: string;
  datasets: string[];
  geometry: LayerGeometry[];
  selectable: string[];
  indicators?: string[];
  /** Layers beyond the first are lazy-loaded. */
  eager?: boolean;
  /** `space` widens the camera envelope to hold the moons. */
  view?: "surface" | "space";
  phase: string;
}

export const LAYERS: Layer[] = [
  {
    id: "layer.political",
    name: "Political",
    summary: "The 34 Regions, their capitals, and the seats of the distributed capital.",
    datasets: ["regions.json", "cities.json"],
    geometry: [
      { kind: "point", source: "cities.cities", colour: "--sirocc", scaleBy: "population" },
      { kind: "region-point", source: "regions.regions", colour: "--ice" },
    ],
    selectable: ["polity", "city"],
    indicators: ["metric.turnout", "metric.access-overturn"],
    eager: true,
    phase: "phase-21",
  },
  {
    id: "layer.ecology",
    name: "Ecology",
    summary: "Biomes in their canonical teal and amber, flagship species, and protected extents.",
    datasets: ["biomes.json", "environment.json"],
    // Biomes carry area and palette but no polygons, so they are drawn at the
    // label points of the regions they name rather than as fills.
    geometry: [
      { kind: "region-point", source: "biomes.terrestrialBiomes", colour: "palette" },
      { kind: "region-point", source: "biomes.flagshipSpecies", colour: "--phyllocyanin" },
    ],
    selectable: ["biome", "species"],
    indicators: ["metric.land-protected", "metric.ocean-protected", "metric.extinction-debt"],
    phase: "phase-21",
  },
  {
    id: "layer.climate",
    name: "Climate",
    summary: "The eleven climate classes, ocean currents, and the hazard set.",
    datasets: ["climate-zones.json", "oceans.json"],
    geometry: [
      { kind: "latitude-band", source: "climate-zones.zones", colour: "palette" },
      { kind: "arc", source: "oceans.currents", colour: "--shelf" },
    ],
    selectable: ["climate", "ocean"],
    indicators: ["metric.co2", "metric.overturning", "metric.net-carbon"],
    phase: "phase-21",
  },
  {
    id: "layer.transport",
    name: "Transport",
    summary: "Maglev and rail corridors, sea lanes, governance air corridors, and launch ranges.",
    datasets: ["routes.json", "cities.json"],
    geometry: [
      { kind: "arc", source: "routes.routes", colour: "--xantholin" },
      { kind: "point", source: "routes.launchRanges", colour: "--ice" },
    ],
    selectable: ["route", "city"],
    phase: "phase-21",
  },
  {
    id: "layer.population",
    name: "Population",
    summary: "Where the 7.25 billion live, by Region and by city.",
    datasets: ["demographics.json", "regions.json", "cities.json"],
    geometry: [
      { kind: "region-point", source: "regions.regions", colour: "--shelf" },
      { kind: "point", source: "cities.cities", colour: "--sirocc", scaleBy: "population" },
    ],
    selectable: ["polity", "city"],
    indicators: ["metric.median-lifespan", "metric.frailty-dependency"],
    phase: "phase-21",
  },
  {
    id: "layer.energy",
    name: "Energy",
    summary: "The fusion fleet, renewable siting, and the four-layer grid.",
    datasets: ["energy.json", "resources.json"],
    geometry: [
      { kind: "region-point", source: "resources.renewablePotential", colour: "--xantholin" },
    ],
    selectable: ["energy", "resource"],
    indicators: ["metric.energy-demand", "metric.reserve-margin", "metric.islanding-failure"],
    phase: "phase-21",
  },
  {
    id: "layer.economy",
    name: "Economy",
    summary: "Output, inequality, and the fiscal equalization flows between Regions.",
    datasets: ["economy.json", "industry.json", "regions.json"],
    geometry: [
      { kind: "region-point", source: "regions.regions", colour: "--xantholin" },
    ],
    selectable: ["polity"],
    indicators: ["metric.gcp-per-capita", "metric.income-gini", "metric.wealth-gini"],
    phase: "phase-21",
  },
  {
    id: "layer.research",
    name: "Research",
    summary: "Universities, century programmes, and the Veydran Commons.",
    datasets: ["research.json", "education.json"],
    geometry: [
      { kind: "region-point", source: "research.centuryProgrammes.named", colour: "--ice" },
    ],
    selectable: ["res", "edu"],
    indicators: ["metric.replication", "metric.rd-intensity"],
    phase: "phase-21",
  },
  {
    id: "layer.protection",
    name: "Protected areas",
    summary:
      "The four tiers of protection covering 44% of land and 38% of ocean, and the four places the Charter makes inviolable.",
    datasets: ["environment.json", "biomes.json"],
    geometry: [
      // Restoration programmes carry area but name no places, so protection is
      // shown through the biomes it covers and the hazards it answers.
      { kind: "region-point", source: "biomes.terrestrialBiomes", colour: "palette" },
      { kind: "region-point", source: "environment.hazardAdaptation", colour: "--xantholin" },
    ],
    selectable: ["env", "region", "biome"],
    indicators: ["metric.land-protected", "metric.ocean-protected", "metric.extinction-debt"],
    phase: "phase-24",
  },
  {
    id: "layer.governance",
    name: "Governance",
    summary:
      "The distributed capital, its five seats on five continents, and the 34 Regions that send delegates to it.",
    datasets: ["cities.json", "regions.json", "government.json"],
    geometry: [
      { kind: "point", source: "cities.cities", colour: "--ice" },
      { kind: "region-point", source: "regions.regions", colour: "--shelf" },
    ],
    selectable: ["city", "polity", "gov"],
    indicators: ["metric.turnout", "metric.access-overturn", "metric.bribe-solicitation"],
    phase: "phase-24",
  },
  {
    id: "layer.materials",
    name: "Materials",
    summary:
      "Where the Concord's minerals come from, including the three on the Constrained List.",
    datasets: ["resources.json", "industry.json"],
    geometry: [
      { kind: "region-point", source: "resources.materials", colour: "--xantholin" },
    ],
    selectable: ["resource"],
    indicators: ["metric.secondary-metal", "metric.beryllium-horizon"],
    phase: "phase-24",
  },
  {
    id: "layer.space",
    name: "Space",
    summary: "Orbital shells, Kalyra and Vesper, and the Belt.",
    datasets: ["space.json", "planet-physical.json"],
    // Space mode changes the camera envelope, so the layer declares it.
    view: "space",
    geometry: [{ kind: "orbit", source: "planet-physical.moons", colour: "--ice" }],
    selectable: ["space"],
    phase: "phase-23",
  },
];
