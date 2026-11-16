# Model parameters

All values as used in the model (`main.nlogox` and the `.nls` files). Scale: 1 patch = 1 m, 1 tick = 1 s.
**Source** says where a value comes from: the proposal, the literature, or an assumption we made (marked
`ASSUMPTION` in the code, in the `set-...-parameters` procedures, so they are easy to find and change).
`*` = independent variable in the experiments.

## Interface (sliders and choosers)

| Parameter | Values (default) | Source / motivation |
|---|---|---|
| number-of-evacuees | 50-300 (150) | Proposal, Table 1 |
| number-of-helpers * | 0, 2, 4, 8 (0) | Proposal, Table 1 |
| alarm-type * | none, slow whoop, voice (slow whoop) | Proposal; Proulx & Sime (1991) |
| proportion-trained * | 0, 0.5, 1 (0) | Proposal, Table 1 |
| cognitive-strategy * | arousal-based; all rational / familiar / follower / panic | Proposal, Experiment 2 |
| panic-threshold | 0.5-1 (0.75) | Proposal, Table 1 |
| vision-radius | 1-20 m (10 m, less in smoke) | Proposal, Table 1 |
| companion-probability | 0-1 (0.3) | Proposal, Table 1; Mawson (2005) |
| helper-range | 1-10 m (5 m) | Proposal, Table 1 |
| helper-capacity | 1-10 per second (3) | Proposal (capacity named, value assumed) |
| max-duration | 100-1800 ticks (900) | Proposal, Table 1 |
| fire-location | random desk, north-west office, north classroom, auditorium (random desk) | Scenario control |
| fire-seed | 0-1000 (0 = new fire every run) | Same fire across conditions (common random numbers) |
| wall-fire-resistance | 1-60 min (30) | Fire-rated interior walls hold 30-60 min (Dutch building code, WBDBO) |
| doors-open-at-start | 0-1 (0.5) | Share of the inner doors open at the start (chosen with the fire's random numbers) |
| close-doors? | on / off (on) | People may close a door behind them; fire-safety advice to do so |

## Evacuees (`set-evacuee-parameters`, evacuees.nls)

| Parameter | Value | Source / motivation |
|---|---|---|
| walking speed | N(1.34, 0.26) m/s, at least 0.5 | Proposal, Table 1 |
| starting (resting) arousal | U(0.1, 0.3); trained x 0.5 | ASSUMPTION; proposal: trained start lower |
| follower-threshold | 0.40 | Proposal |
| pre-movement delay | log-normal, mean 60 s (whoop, self-noticed) / 30 s (voice), SD = mean / 2 | Proposal (Proulx & Sime, 1991); SD assumed |
| whoop-arousal-increase | +0.1 once | Proposal (Deng et al., 2022: alarm without cause raises fear) |
| voice-arousal-decrease | -0.1 once | ASSUMPTION; proposal: "arousal is lowered" |
| flame-arousal-gain | +0.02 per s while flames are in sight | ASSUMPTION; flames > smoke (Deng et al., 2022) |
| smoke-arousal-gain | +0.01 per s while in smoke | ASSUMPTION |
| crowd-arousal-gain | +0.005 per s with 5+ people around | ASSUMPTION; nervousness in crowds (Helbing et al., 2000) |
| contagion-rate | 5% of the difference with the people in sight per s | ASSUMPTION; emotional contagion (Bosse et al., 2013) |
| arousal-decay | -0.005 per s while walking with no threat, down to resting arousal | ASSUMPTION; panic (0.75) to calm (0.40) in ~70 s |
| trained-gain-factor | 0.5 | ASSUMPTION; proposal: trained gain arousal "at a lower rate" |
| panic speed factor | U(1, 1.5), drawn once per person | Proposal: "up to 1.5x faster" |
| panic-vision-factor | 0.5 | ASSUMPTION; high arousal narrows attention (Easterbrook, 1959) |
| panic-randomness | 0.3 of the steps go the wrong way | ASSUMPTION |
| panic-clog-chance | 0.3 per step in a crowd | ASSUMPTION; "faster-is-slower" (Helbing et al., 2000) |
| base-randomness | 0.1 of the steps are random | ASSUMPTION |
| smoke-notice-level | 0.1 | ASSUMPTION |
| companion-search-time | 30 s | ASSUMPTION |
| fire-damage | 50 health per s on a burning patch | ASSUMPTION (2 s in the fire is deadly) |
| smoke-dose-rate | toxic dose (FED) + smoke / 90 per s: collapse after 90 s in the thickest smoke | ASSUMPTION; Fractional Effective Dose (Purser & McAllister, 2016; ISO 13571) |
| lethal-dose | death at FED 2 (collapse at FED 1) | ASSUMPTION; about twice the incapacitating dose |
| toxic-confusion | up to 0.5 of the steps confused at FED 1 | ASSUMPTION; carbon monoxide impairs judgment |
| toxic-weakness | up to 30% slower at FED 1 | ASSUMPTION; dizziness and weakness |
| heat dose | + 1 / (60 x 5e7 x temperature^-3.4) per s: collapse at 1, death at 2 (about 4 min at 120 C, 45 s at 200 C) | Purser & McAllister (2016); ISO 13571 (convective heat only) |
| smoke-speed-loss | up to 50% slower in the thickest smoke | Jin (1978); Fridolf et al. (2013) |

## Helpers (`set-helper-parameters`, helpers.nls)

| Parameter | Value | Source / motivation |
|---|---|---|
| helper-walking-speed | 1.34 m/s | Mean walking speed, Table 1 |
| helper-speed-factor | helped evacuees walk 1.2x faster | ASSUMPTION |
| helped-randomness-factor | 0.5 (half as many random steps) | ASSUMPTION |
| helper-calming | -0.05 arousal per second of help | ASSUMPTION |

## Doors (`set-door-parameters`, doors.nls)

| Parameter | Value | Source / motivation |
|---|---|---|
| trained-door-closing | 0.8 chance to close a door behind you | ASSUMPTION; training teaches to close doors (fire service advice) |
| untrained-door-closing | 0.3 | ASSUMPTION; most people leave doors open |
| helper-door-closing | 1 (helpers close every door they pass) | ASSUMPTION; trained staff (fire wardens) |
| panicking evacuees | never close a door | ASSUMPTION |
| door-holding-distance | 2 m: nobody closes a door while someone else is this close to it | ASSUMPTION |
| exit doors | always open | ASSUMPTION; people stream out through them |

## Fire and smoke (`set-fire-parameters`, fire.nls) and alarm (alarm-and-fire.nls)

| Parameter | Value | Source / motivation |
|---|---|---|
| fuel | desks (581 m2), doors, and carpet in the furnished rooms (1218 m2); room contents burn after flashover | Level-0 floor plan |
| fire-growth-time | 75 s to full strength (1 MW per desk) | "Ultra-fast" t-squared fire class (NFPA 92; BS PD 7974-1): desks with paper, plastic and computers |
| ignition-temperature | 300 C: fuel under smoke this hot catches fire | Paper and wood ignite at ~250-350 C (Drysdale, 2011) |
| hot-catch-chance | 0.1 per s (~10 s in smoke that hot) | ASSUMPTION |
| fire-burn-time | 1800 s | Office fire load ~420 MJ/m2 at ~250 kW/m2 (Eurocode EN 1991-1-2) |
| fire-reach | 2 m (heat radiation), never through walls | ASSUMPTION |
| desk-catch-chance | 0.02 per s from one fully burning patch | ASSUMPTION (~1 min to the next desk) |
| door-catch-chance | 0.002 per s, open doors only (closed doors burn through instead) | ASSUMPTION (doors resist 10x longer) |
| carpet-catch-chance | 0.002 per s, from burning furniture or doors (not from other carpet), or under hot smoke | ASSUMPTION; floor coverings need strong radiant heat to keep burning (EN 13501-1) |
| carpet-power | 250 kW per burning m2 | ASSUMPTION (a quarter of a desk) |
| desk-power | 1 MW per burning patch | Workstations burn at 1-3 MW |
| flashover power | 7.8 x surface area + 378 x open door area x sqrt(door height) kW (1.4-6.7 MW per room with its doors open) | Thomas (1981) |
| flame-reach | 2 m: after flashover, flames come this far out of an open doorway (corridor floors themselves do not burn) | ASSUMPTION; the fuel that cannot burn inside burns outside the room |
| air-power | a room fire is at most 1500 kW x open door area x sqrt(door height): 4.6 MW per open 1 m door, 0.2 MW closed | Kawagoe (1958) |
| door-leakage | the gaps around a closed door count as 4% of the doorway | ASSUMPTION (~1 cm around, ~2 cm under the door) |
| door-fire-resistance | 10 min: a closed door next to a fully burning patch then burns through | ASSUMPTION; ordinary doors 5-20 min, fire doors 30+ min (EN 1634-1) |
| ceiling / door height | 3 m / 2.1 m | ASSUMPTION |
| max-flashover-area | 500 m2 (the central hall never flashes over) | ASSUMPTION |
| smoke-flow-speed | 1 m/s near the fire, slower beyond 10 m (x 10 / distance) | ASSUMPTION; ceiling jet (Alpert, 1972) |
| smoke-production / smoke-spread / smoke-spread-steps | 0.25 / 0.8 / 4 | ASSUMPTION; tuned: fire room smoky after 2-3 min |
| ambient-temperature | 20 C | ASSUMPTION |
| flame-heat | burning patches are ambient + 800 C (x fire strength) | Flames and flashed-over rooms ~800-900 C (Drysdale, 2011) |
| heat-loss | hot smoke loses 10% of its heat per s; it travels with the smoke | ASSUMPTION; tuned: ~300 C next to a flashed-over room, ~100 C at 10 m |
| detector-spacing | 7 m, and at least one detector in every room | ASSUMPTION (one detector per ~50 m2); full coverage as in NEN 2535 |
| detector-smoke-level | 0.05 | ASSUMPTION; alarm after 36-204 s |
