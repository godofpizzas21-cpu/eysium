# The Health System

**Document ID:** `health.system`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/health.json`
**Inherits:** `gov.constitution` (right 9, floors not ceilings; Biosecurity
portfolio), `gov.regions` (District delivery), `hist.demographics` (112-year
lives, mortality profile, multi-generational households), `ind.concentration`
(no significant private tier), `cult.languages` (41 registered languages)

All figures as of **EY 412, Calenth 16**.

---

## 1. Shape and Scale

| Indicator | Value |
|---|---|
| Health and care spending | **11.2% of GCP** (đ115.3 trillion) |
| Health and care workforce | 290 million (8.0% of the labour force) |
| Cost to a patient at the point of use | **Zero** |
| Private tier | Negligible — 0.8% of episodes, bound by the same standards |

| Tier | Count | Function |
|---|---|---|
| Commune health posts | 47,900 | First contact, prevention, home-care coordination, the named clinician |
| District clinics | 22,400 | Diagnostics, outpatient specialties, minor procedures |
| District hospitals | 3,800 | Inpatient, surgery, emergency, maternity |
| Regional specialist centres | 340 | Complex surgery, transplantation, rare disease, major trauma |
| Concord facilities | 41 | Biosecurity containment, orphan conditions, the reference laboratories |

Healthcare is a **District competence** delivered under a Concord floor, like
education. The Concord specifies entitlements, waiting-time maxima, and safety
standards, and does not specify how a District meets them.

**There is no meaningful private tier**, and this is a policy outcome rather than
a prohibition. Private practice is legal; it is bound by the same clinical
standards, the same waiting-time obligations, and the same publication
requirements, and it may not offer queue priority. What remains is 0.8% of
episodes, mostly cosmetic and elective. The decoupling this produces —
wealth cannot buy a better hospital (`ind.concentration` §5) — is one of the
Concord's own most-cited claims about itself.

**Language.** Right 13 applies to clinical care: a patient is treated in their
own language, not translated at. 99.1% of episodes are conducted in the patient's
first language, and where they are not, the reason is recorded and audited.

## 2. The Named Clinician

Every resident of the Concord has a **named generalist clinician** who is
accountable for their care across their life. This is the structural feature
Elysians identify first when asked what their health system is.

With median lifespans of 112 Elysian years, a clinician may follow the same
patient for fifty years, and often follows three or four generations of the same
household — a consequence of multi-generational living
(`hist.demographics` §4) that Elysian medicine treats as an asset rather than an
accident. The clinician holds the whole record, coordinates every specialist, and
is the person who says what the situation actually is.

**Handover is a formal event.** When a clinician retires, moves, or takes a
fallow year (`econ.markets` §3), the transfer of each patient is documented,
discussed with the patient, and — for patients with complex needs — conducted in
a joint consultation. Continuity is treated as a clinical intervention with its
own protocol, because the evidence on Elysium is that it behaves like one.

Panel sizes are capped: 1,400 patients per full-time generalist, lower where
frailty is concentrated.

## 3. Care Where People Live

Elysian hospitals are for what cannot be done anywhere else. **71% of episodes
that an Integration-era system would have hospitalised are managed at home or in
a Commune health post**, supported by visiting teams, remote monitoring, and the
household.

This works partly because of the household structure — a frail Elysian of 118 EY
usually lives with adult descendants — and partly because it is funded properly:
home care is not the cheap option in Concord budgeting, and District accounts
that show home care costing less than hospital care for equivalent acuity are
audited on suspicion.

Canon records the corresponding risk in §6: a system that leans on households
leans hardest on the people in them, and unpaid care is unevenly distributed.

## 4. Prevention, and Its Limits

Universal programmes cover immunisation, cardiovascular and metabolic screening,
sensory function, cognitive assessment from 70 EY, and occupational exposure
monitoring.

What distinguishes Elysian prevention is that **screening programmes are
reviewed adversarially and are discontinued when they cause net harm.** Every
programme is subject to a standing red grant (`res.system` §2), and the review
asks whether the programme improves outcomes rather than whether it finds
disease — a distinction Elysian public health treats as the central one.

**Three programmes have been discontinued** on that basis since EY 300, having
been found to generate more harm through over-diagnosis, anxiety, and unnecessary
intervention than they prevented. Discontinuation was politically difficult in
all three cases, because a screening programme has a visible constituency of
people who believe it saved them and an invisible one of people it harmed. The
Concord publishes the reasoning in full each time and does it anyway.

Occupational health is unusually strong. Shift work that violates the biphasic
sleep pattern is regulated as a hazard rather than an inconvenience
(`hist.demographics` §1), employers must justify it, and the health consequences
of the Stillness being broken are among the best-documented findings in Elysian
medicine.

## 5. Emergency Care

| Indicator | Value |
|---|---|
| Median urban response, medical emergency | 6 civil minutes |
| Median rural response | 19 civil minutes |
| Worst regional median (Northreach) | 74 civil minutes |
| Major trauma centres | 340 |
| Survival to discharge, major trauma | 81% |

The **Commune Response Teams** (`law.policing` §1) are the front door for a large
share of what an Earth system would route through emergency medicine: mental
health crisis, intoxication, falls, and welfare emergencies. They are health
staff, dispatched from the same number as police and ambulance, and their
existence is why Elysian emergency departments are comparatively quiet.

Rural response is the system's clearest inequality and canon does not soften it.
The Charter guarantees healthcare; it does not and cannot guarantee a response
time, and in Northreach, Austral Shore, and the outer Isles the difference is
measured in lives.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **The cost curve** | An old population with 112-year lifespans generates a spending trajectory that has risen faster than GCP for eighty years. Nobody has proposed a solution that survives contact with Charter right 9 |
| **Care workforce** | Vacancies run at 6.4% and higher in frailty-intensive roles; care work is the largest single labour shortage in the Concord |
| **Unpaid household care** | The home-first model rests on household capacity, which is unevenly distributed and falls disproportionately on women and on the least wealthy households. Recognised, partially compensated, not solved |
| **Rural response times** | A 74-minute median in Northreach against 6 in cities; the gap has narrowed only slightly in a century |
| **Over-diagnosis** | Three programmes discontinued, and the reviews consistently find the problem is larger than the discontinuations address |
| **Handover quality** | Continuity is protocolised and still degrades at transfer; outcomes worsen measurably in the two years after a named clinician changes |

## 7. Open Threads

- Geriatrics, mental health, genetics, end of life, epidemic response → `health.practice` (this phase)
- Biomedical research frontiers → `res.sciences`
- Disaster medicine and mass-casualty response → Phase 12
- Care work, wages, and labour shortage → `econ.markets`
- Health indicators → Phase 16
