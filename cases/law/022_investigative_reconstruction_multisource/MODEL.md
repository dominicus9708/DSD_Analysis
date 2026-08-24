# LAW-011 Model — Past Event, Source State, Reconstruction, and Institutional Finding

Status: revised model after first counterpressure pass.

## 1. Do not use an omniscient analyst state

Let `H*` denote an ideal complete description of the historical event only as a comparison ideal.

Do **not** treat `H*` as a state actually possessed by investigators, witnesses, victims, suspects, courts, or the DSD analyst in real cases.

For a real source `i`, distinguish at least:

`O_i` — contemporaneous perception/observation state;

`M_i(t)` — later memory state at time `t`;

`A_i(t)` — account/statement produced at time `t`;

`P_i` — provenance/exposure/interview conditions;

`D_i` — dependence relation to other sources or later information;

`U_i` — uncertainty/specificity state.

For a physical or digital trace `j`, distinguish:

`T_j` — trace/material state;

`C_j` — collection/preservation/contamination state;

`I_j` — interpretation/model used to connect the trace to candidate histories.

## 2. Candidate-history space

Let `H_k` denote the set or structured family of candidate historical reconstructions at investigative step `k`.

A naive triangulation model would use:

`H_(k+1) = H_k intersection Constraint(E_k)`.

This is too strong as a universal model.

If a source is later shown to be contaminated, dependent, misunderstood, or misrecorded, hypotheses previously excluded may need to be reconsidered.

Therefore the update should be written more generally:

`H_(k+1) = U(H_k, E_k, Gamma_k)`

where `Gamma_k` includes source provenance, dependence, reliability/validity rules, procedural status, and any revision of earlier source assessments.

The update can narrow, preserve, reorder, or reopen candidate reconstructions.

Thus investigation need not be monotone.

## 3. Source-count versus independent-information count

Let `n_report` be the number of reports and `n_independent` the number of independently informative source streams.

In general:

`n_report != n_independent`.

If witnesses exchange information, receive common feedback, view the same media report, or are questioned through a common leading frame, several later accounts may share one post-event source.

Agreement therefore does not by itself prove independent corroboration.

## 4. Institutional finding remains distinct

Let `J_t` denote the institutional factual determination at procedural time `t` under governing rules `R_J`.

Then:

`H* != H_k != J_t`.

The institutional finding can depend on legal proof thresholds, admissibility rules, burden allocation, presumptions, review/finality, and procedural constraints.

A `not guilty` or non-liability result does not uniquely select one historical reconstruction.

## 5. Triangulation analogy — retained only in a narrow form

The analogy survives as:

**different source streams can constrain the space of plausible reconstructions, and cross-source comparison can expose incompatibilities or dependencies that one source alone cannot reveal.**

The analogy is rejected if read as:

- all sources are independent sensors;
- all constraints are exact;
- every source update monotonically narrows the solution;
- enough sources guarantee a unique true reconstruction;
- agreement count directly measures truth.

## 6. DSD application bridge

A typed application record may contain:

`(source, role, modality, event-time relation, observation state, later-memory state, account/trace, provenance, dependence, uncertainty, procedural-use status, candidate-history relation, governing rule, time, regime)`.

Formation can help preserve distinct typed records and not-yet-formed statuses.

But:

- `historical truth != Formation complete descriptor`;
- `witness memory != DSD observer state by identity`;
- `source reliability != Static Aggregation weight`;
- `investigative update != Formation stage chain`;
- `memory change != DSD Dynamics law`.

If investigative change over time is modeled, use separate time-indexed descriptors and an external update relation.

## 7. Main boundary

The main DSD-compatible rule is not `investigation converges to truth`.

It is:

**do not collapse historical event, observation, memory, record, provenance/dependence, reconstruction, and institutional finding into one state, and do not infer one from another without the external evidentiary, cognitive, forensic, or legal rule that supplies the bridge.**
