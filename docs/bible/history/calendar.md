# The Elysian Calendar and Timekeeping

**Document ID:** `hist.calendar`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/calendar.json`
**Inherits:** `planet.physical` (solar day 25.9 h, solar year 384.24 dE),
`charter.canonical-units` (EY/BE notation)

---

## 1. Two Kinds of Time

The Concord keeps two time systems and never confuses them.

**Physical time** uses the SI second, defined atomically, for all science,
engineering, navigation, and law. Nothing in this document alters the SI second.

**Civil time** is tied to the planet: the day, the year, the seasons. Civil units
are defined *as fractions of the solar day* and therefore do not equal SI units.
Every civil unit's SI value is fixed in law and published, so conversion is exact
rather than approximate.

Earth-style leap seconds — inserting a physical unit into a civil count to keep
them married — is precisely the confusion Elysian practice avoids. The two
systems are related by a published constant, not by patching.

## 2. The Civil Day

The Elysian solar day is **25.9 hours = 93,240 SI seconds** (`planet.physical`).
It divides into:

| Civil unit | Definition | SI equivalent |
|---|---|---|
| Day | 1 solar day | 93,240 s |
| **Hour** | 1/26 day | 3,586.15 s (59.77 min) |
| **Minute** | 1/60 hour | 59.769 s |
| **Beat** | 1/60 minute | 0.99615 s |

The choice of **26 hours** is not arbitrary. It is the divisor that makes the
Elysian civil hour and minute land within 0.4% of the intuitive human-scale
units a 24-hour world would produce, so the Elysian day feels neither rushed nor
stretched — it simply has two more hours in it than an Earth day would.

Those two extra hours are the most quietly consequential fact in Elysian daily
life. They appear again in the structure of the working day (Phase 6), in
sleep-health policy (Phase 9), and in the long, unhurried Elysian evening that
so much of the culture is built around (Phase 14).

Clock notation: `H:MM` on a 26-hour cycle, midnight at `0:00`, midday at `13:00`.

## 3. The Year

The solar year is **384.24 days**, and 384 factors perfectly:

```
384 days = 12 months × 32 days
32 days  =  4 weeks  ×  8 days
384 days = 48 weeks exactly
```

Because 384 divides evenly into weeks, **every date falls on the same weekday in
every year, forever**. The Elysian calendar is perpetual. There is no
"what day does the 14th fall on this year" — Ostreth 14 is Seldan, permanently,
and has been since EY 1.

This is the single most-loved feature of the calendar and quietly enormous in
its effects: schedules, rotations, festivals, court terms, school years, and
transport timetables are all structurally stable, and Elysians find the Earth
practice of a drifting weekday genuinely baffling when it is explained to them.

### The intercalary day

The remaining 0.24 day is absorbed by **Thresholdday**, an intercalary day
inserted at the end of the year in leap years. Thresholdday belongs to no week
and no month; it is a day outside the count. This is what preserves the
perpetual alignment — the week cycle never absorbs the leap, so it never drifts.

**Leap rule:** Thresholdday occurs every 4th year, *except* in years divisible
by 100. That gives 24 intercalary days per century against a required 24.0, for
a mean civil year of 384.24 days — exact to the precision of the orbit itself.
The next correction is not expected to be required for roughly 40,000 years,
and the constitutional procedure for making it exists anyway (Phase 4).

Culturally, Thresholdday is a day without obligations: no work, no courts, no
markets, no scheduled governance. It is the Concord's only universal holiday
(other festivals are regional — Phase 14).

## 4. Months

| # | Month | Character in the northern hemisphere |
|---|---|---|
| 1 | **Verane** | Early spring; the year begins at the northward equinox |
| 2 | **Kelith** | Spring |
| 3 | **Ostreth** | Late spring |
| 4 | **Sarien** | Early summer; northern solstice falls in Sarien |
| 5 | **Thelen** | High summer |
| 6 | **Iridan** | Late summer |
| 7 | **Aumar** | Early autumn; southward equinox |
| 8 | **Calenth** | Autumn |
| 9 | **Nerith** | Late autumn |
| 10 | **Tavric** | Early winter; northern winter solstice |
| 11 | **Solmis** | Deep winter |
| 12 | **Yvenne** | Late winter; the year closes |

Month names are neutral rather than seasonal in meaning, because Elysium's
calendar is planetary and its seasons are inverted between hemispheres. A
Veydran reads Verane as the start of autumn and finds nothing strange in it.
This was a deliberate and contested choice at the founding: the Meridian
Convention rejected the northern-seasonal names that had dominated the
industrial era precisely because a planetary civilization cannot encode one
hemisphere's weather into everyone's dates.

**Year start** is fixed at the **northward equinox**, an astronomical event, not
a cultural one.

## 5. The Week

Eight days. The last two are the customary rest days across most of the
Concord, though working patterns are a matter of labour law (Phase 6), not
calendar law.

| # | Day | Named for |
|---|---|---|
| 1 | **Heldan** | Helia, the star |
| 2 | **Kaldan** | Kalyra, the major moon |
| 3 | **Vesdan** | Vesper, the minor moon |
| 4 | **Mardan** | The sea |
| 5 | **Tordan** | The mountain |
| 6 | **Irdan** | The field |
| 7 | **Seldan** | The hearth — first rest day |
| 8 | **Ovdan** | The open — second rest day |

The eight-day week is older than the Concord: it descends from the Alcyon
agricultural cycle of the classical era (`hist.timeline`), one of the few
pre-founding structures the Convention chose to keep rather than redesign.

## 6. Date Notation

**Prose:** `EY 412, Calenth 16` — year, month, day.
**Data and code:** `EY-0412-M08-D16` (zero-padded year, month index, day index),
which sorts lexicographically, as required by `charter.canonical-units` §2.
**Intercalary:** `EY-0412-TH` for Thresholdday.
**Pre-founding:** `BE-0087-M03-D02`, counting years backward; there is no year 0.

## 7. The Reference Date

The Civilization Bible describes the Elysian Concord as it stands on:

> **EY 412, Calenth 16** — `EY-0412-M08-D16`

Every population figure, economic statistic, institutional description, and
metric in every later phase is "as of" this date unless explicitly historical.
When a later phase needs a number to change over time, it supplies a time series
in data rather than contradicting this document.

## 8. Older Calendars

Regional calendars from before the founding survive culturally and are used for
festivals, liturgy, and heritage (Phase 14). The three of note — the **Alcyon
agricultural reckoning**, the **Thalassari tidal calendar**, and the **Aurorian
dark-count** — are all still published alongside the civil calendar in their
regions. The Concord's practice is to preserve them, not replace them: the
civil calendar governs the state, and nothing else.
