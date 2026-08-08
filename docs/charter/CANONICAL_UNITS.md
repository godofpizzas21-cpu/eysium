# Canonical Units & Conventions

**Document ID:** `charter.canonical-units`
**Status:** Canon
**Version:** 1.2.0

This document defines the units, formats, and epochs used everywhere in Project
Elysium — Bible prose, JSON data, and application code. It defines *conventions*
now; domain-specific values (the exact length of Elysium's day, the currency's
name) are canonized by the phases that own them, and this file is updated in
those phases per `CANON_RULES.md` §6.

---

## 1. Measurement System

- **SI metric units, exclusively.** Metres, kilograms, seconds, kelvin/°C,
  watts, joules, pascals, hectares (10,000 m²) for land area where clearer.
- Large quantities use SI prefixes (GW, PJ, Mt), never regional idioms
  ("billions of tons" → "X Gt").
- In JSON data, units are **never embedded in values**. Every dataset declares
  units in its schema; values are plain numbers. Example: `"elevationM": 412`,
  with the schema documenting metres.
- Coordinates: decimal degrees, WGS84-analogue spherical convention for Elysium
  — latitude −90…+90, longitude −180…+180, longitude 0 defined by the planetary
  prime meridian (canonized in Phase 2).

## 2. Time and the Elysian Calendar

- **Canonized in Phase 2A** (`planet.physical`): the Elysian solar day is
  **25.9 hours**; the solar year is **384.24 Elysian days**.
- **Canonized in Phase 3A** (`hist.calendar`): the full civil calendar. The
  civil year is **12 months of 32 days = 48 weeks of 8 days = 384 days**, plus
  the intercalary **Thresholdday** every 4th year except centennial years. The
  calendar is **perpetual**: every date falls on the same weekday in every year.
  The civil day divides into **26 hours of 60 minutes of 60 beats**; civil units
  are fractions of the solar day and do **not** equal SI units (1 civil
  hour = 3,586.15 s; 1 civil minute = 59.769 s; 1 beat = 0.99615 s).
- **Physical vs civil time:** SI seconds govern all science, engineering, and
  law. Civil units govern dates and clocks. The two are related by the published
  constants above, never by patching one into the other.
- **Epoch:** Elysian years are counted from the founding of the Concord,
  written **EY** (Elysian Year). Years before the founding: **BE** (Before
  the Era), counting backward (1 BE precedes EY 1; there is no year 0).
- **Date format (prose):** `EY 412, Calenth 16` — year, month name, day.
- **Date format (data/code):** ISO-like ordinal form `EY-0412-M08-D16`
  (zero-padded year, month index, day index) so dates sort lexicographically.
  Thresholdday is written `EY-0412-TH`.
- **"Present day" of the project — the reference date:** the Bible describes the
  Concord as of **EY 412, Calenth 16** (`EY-0412-M08-D16`). All statistics in
  every phase are "as of" this date unless explicitly historical.
- Durations in engineering contexts use SI seconds/hours/days; "day" and "year"
  unqualified always mean *Elysian* day and year.

## 3. Currency

- The Concord's currency (name, symbol, structure) is owned by **Phase 6**.
- Convention fixed now: amounts in data are integers of the **minor unit**
  (like cents), field names suffixed with the currency code once defined.
- No real-world currencies ever appear in canon.

## 4. Numbers and Formatting

- Decimal separator: `.` — thousands separator in prose: thin space or comma,
  consistently comma in this project ("2,400,000"). JSON: raw numbers only.
- Percentages: `%` with one decimal max in prose unless precision matters.
- Ranges: en dash ("40–60 km").
- Uncertainty, where canon deliberately models it, is written "value ± tolerance".

## 5. Geospatial Conventions for the Atlas

- Planet radius normalized to **1.0 render unit** in Three.js; all altitudes and
  orbits expressed as multiples of planetary radius in render space, converted
  from metres via constants in `data/planet-physical.json` (created Phase 2).
- Angles in data: degrees. Angles in code: radians at the Three.js boundary,
  converted by utility functions only — never ad hoc.
