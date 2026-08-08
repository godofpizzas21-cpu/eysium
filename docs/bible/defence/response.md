# Response: Disaster, Impact, and Cyber

**Document ID:** `mil.response`
**Status:** Proposed
**Version:** 1.2.0
**Authoritative data:** `data/defence.json`
**Inherits:** `mil.service`, `hist.timeline` (the Serrance Storm Failure,
the Cassian Incident, the Kessander Plague), `planet.climate` (hazards),
`energy.grid` (grid emergencies), `law.policing` (no bulk collection),
`planet.physical` (the Tyrran Belt)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Serrance Lesson

On the current disaster doctrine, everything traces to one failure.

In **EY 341** a cyclone made landfall at Cape Serrance. The forecast was correct,
issued in good time, and understood. **4,100 people died** because the forecast
did not become an evacuation: the warning reached an authority that had to decide
to act, the decision was deferred pending confirmation, and confirmation arrived
after the storm (`hist.timeline` §10).

The reform that followed inverted the default.

> **For harm, a human must authorise. For protection, a human must cancel.**

This asymmetry is the single most distinctive principle in Elysian emergency
doctrine, and it is deliberately the mirror image of the Cassian rule. Cassian
established that no system may escalate toward harm without a human deciding to
(`mil.service` §3). Serrance established that no system may *withhold* protection
while waiting for a human to decide.

In practice: when a monitored threshold is crossed — forecast wind speed, river
stage, ground acceleration, epidemiological signal, grid frequency — the
protective response **begins automatically**. Evacuation transport dispatches,
refuges open, reserves release, and alerts go out. A named accountable official
may stop it, must record why, and that record publishes. Since EY 341 protective
responses have been initiated 11,400 times and cancelled by human decision 1,340
times, of which 61 cancellations were subsequently found to have been wrong.

Canon records that the doctrine has costs. False activations are frequent,
expensive, and erode public patience; three Regions have measured declining
compliance with evacuation orders, which is exactly the failure mode a
cry-wolf system produces. The Concord's answer has been to publish activation and
cancellation statistics rather than to raise thresholds, and canon does not claim
this has fully worked.

## 2. Disaster Response in Practice

| Capability | Standing level |
|---|---|
| Response Corps strength | 4.1 million |
| Mobilisation | 10,000 responders anywhere on Elysium within 12 civil hours |
| Sustained deployment | 400,000 for 90 days without drawing on Regional capacity |
| District emergency housing | 4% of District population, exercised annually |
| Port disaster reception | Any major port receiving and distributing relief at scale on 48 hours' notice |
| Cyclone evacuation standard | 90% of exposed population moved within 36 civil hours |
| Full planetary exercise | Every 4 years, unannounced within a stated quarter |

Response is **layered like the grid** (`energy.grid` §1): Communes act first and
are expected to hold alone for 14 days, Districts reinforce, Regions coordinate,
and the Concord deploys only where regional capacity is exceeded. The Concord
tier has been the primary responder eleven times since EY 300.

**The Response Corps is not primarily a uniformed standing body.** 3.1 million of
its 4.1 million are trained reservists in ordinary employment — engineers,
clinicians, logisticians, and heavy-equipment operators — with a statutory right
to be released by their employer on activation, at full pay, with the cost borne
publicly. Elysians treat reserve service as a normal civic commitment, and
participation is a quiet marker of social standing.

## 3. Planetary Defence

Elysium sits inside a system with an active asteroid population shepherded by
the gas giant **Tyrran** (`planet.physical` §1b), so impacts are a real and
quantified hazard rather than a remote one.

| Indicator | Value |
|---|---|
| Objects above 100 m catalogued | 99.4% |
| Objects above 30 m catalogued | 94.1% |
| Objects below 30 m catalogued | Negligible |
| Warning time, typical catalogued threat | Decades |
| Deflection methods | Kinetic impactor; gravity tractor; ablation |
| Operational deflections performed | **1** |

**The Vesper Event, EY 268.** A 140-metre body was identified on an impacting
trajectory six years out. A gravity tractor was placed in EY 264 and a kinetic
impactor followed in EY 266; the object passed at 41,000 km in EY 268. It remains
the only operational deflection in Elysian history, is regarded as the
Concord's most complete institutional success, and is taught alongside the
Cassian Incident as the pair of events that define what the Concord thinks it is
for — one catastrophe averted by refusing to act, one by acting decades ahead.

**The uncatalogued small-body risk is unresolved.** An object of 20–30 metres
gives essentially no warning and would destroy a city district. The Concord's
survey capability has improved for two centuries and cannot close this gap with
any technology it possesses. Its answer is building standards and refuge capacity
rather than detection, which the Planetary Defence Directorate describes in its
own reports as *"an answer to the wrong question, offered because we have no
answer to the right one."*

## 4. Cyber Defence

The threat model is **non-state**, and canon is specific about why: there is no
hostile state to defend against, and the most damaging deliberate attack in
Elysian history — the Kessander Plague — was mounted by a non-state group
(`hist.timeline` §8).

Defence rests on resilience rather than perimeter:

- **Public infrastructure with published source.** Identity, payments, records,
  and grid control are publicly built and their source is public
  (`gov.administration` §6). Concord doctrine holds that a system whose security
  depends on its secrecy is a system nobody has checked.
- **Islanding and manual fallback.** Every critical system must function
  degraded. Grid Districts can be operated manually; ports and hospitals hold
  paper procedures; the physical dram exists precisely for this
  (`econ.money` §1). Full planetary exercises include a communications-denied
  scenario.
- **No offensive capability against civilian infrastructure.** The Concord
  maintains the ability to disable systems actively attacking it and has
  renounced anything further. The renunciation is unilateral, published, and
  — canon notes — untested, since there is no adversary state to reciprocate.

Significant incidents run at roughly 40 per year, overwhelmingly attempts against
financial and identity infrastructure, none of which has succeeded in disabling a
Concord-tier system since EY 366.

## 5. Intelligence

Elysian intelligence is unusually constrained, and the constraints are
constitutional rather than budgetary.

- **No bulk collection** (`law.policing` §4). Untargeted collection is prohibited
  outright, not regulated.
- **No secret agency.** The Service's Assessment Branch is a published
  organisation with a published budget. It issues an annual unclassified threat
  assessment and a classified annex that opens automatically after three years.
- **Targeted collection requires judicial warrant**, particularised, with
  notification of the subject once the operation ends.
- **No domestic political intelligence.** Collection against a person on the
  basis of lawful political, religious, or associational activity is a criminal
  offence, without exception.

**The honest cost:** the Concord's threat model is non-state actors building
things quietly, and its constitutional architecture is close to optimally bad at
detecting exactly that. The Assessment Branch says so in its own published
assessment, every year, in the same words: *"We would probably not see the next
Kessander before it was used."*

The Concord has considered relaxing the constraints three times — most recently
in EY 388 — and has refused each time, on the ground that a surveillance
apparatus capable of finding one group is capable of finding anyone, and that the
Concord would rather be vulnerable to a rare catastrophe than to a permanent one.
Canon records this as a deliberate, argued, and genuinely contested choice.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Cry-wolf erosion** | Automatic protective activation produces frequent false alarms; three Regions measure declining evacuation compliance, and raising thresholds is refused |
| **Small-body blindness** | Objects under 30 m are effectively undetectable and would destroy a city district; the Directorate calls its own mitigation an answer to the wrong question |
| **Intelligence cannot see the threat it fears** | The Assessment Branch publishes, annually, that it would probably not detect the next engineered-pathogen group before use |
| **Untested renunciation** | The offensive-cyber renunciation is unilateral and has never been tested against a capable adversary |
| **Reservist release is uneven** | Statutory release at full pay is honoured at 91%; small employers in small Regions honour it least |
| **Eleven Concord-tier responses in a century** | The Concord tier rarely leads, so its own operational competence is exercised mostly in drills |

## 7. Open Threads

- The Cassian officer and AI governance lineage → `ai.governance`
- Orbital defence, debris, and off-world rescue → `space.infrastructure`
- Epidemic response operations → `health.practice`
- Grid restoration doctrine → `energy.grid`
- Emergency housing and post-disaster reconstruction → `city.housing`
- Resilience and safety indicators → Phase 16
