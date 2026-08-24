# Administration, Organization, and Directive Structures

This domain tests DSD Analysis against operational organizations rather than positive-law doctrine.

Primary targets include:

- directives, orders, objectives, assignments, and approvals;
- organizational communication and acknowledgement;
- role/authority/reporting interfaces;
- delegated discretion and local initiative;
- review, escalation, feedback, and revision;
- distributed responsibility for organizational outcomes.

## Method

Use the same post-law discipline:

`external source structure -> strong candidate -> active counterpressure -> independent witness families -> DSD mapping -> contradiction audit -> generalization status`.

Do not import the legal-domain result as proof. The point of this domain is to test whether similar constraints recur independently.

## ADMIN-001 / Global Case 026

Topic: instruction, interpretation, execution, and outcome.

Witness families:

- U.S. Army mission command;
- FAA air-traffic clearance/readback/clarification procedures;
- FEMA/NIMS Incident Command System.

Surviving candidate:

`intent != wording != receipt != acknowledgement != interpretation != authorized discretion != execution != outcome`.

Strong forms rejected:

- more detailed instruction is always better;
- issue = receive = understand = execute;
- acknowledgement proves understanding;
- discretion is always a defect;
- multiple directives merely add information;
- successful outcome proves instruction adequacy;
- failed outcome proves subordinate execution fault.

New cross-domain boundary:

**clarity of purpose, precision of safety-critical coordinates, degree of method specification, feedback closure, and permitted discretion are distinct design variables.**

## ADMIN-002 / Global Case 027

Topic: delegation, escalation, approval, and authority.

Witness families:

- U.S. Army ADP 6-0 delegation and retained responsibility;
- FEMA/NIMS delegation-of-authority and transfer-of-command procedures;
- NASA Programmatic Authority, Technical Authority, independent review, risk-acceptance authority, and dissent/escalation processes.

Surviving candidate:

`rank != delegated authority != retained responsibility != review/technical authority != escalation right != implementation authority`.

Strong forms rejected:

- higher rank always determines operative decision authority;
- delegated authority automatically transfers responsibility in the same way;
- one organization has one simple authority chain;
- dissent/escalation is disobedience by identity;
- transfer of command deletes prior organizational state;
- review/concurrence authority is the same as implementation authority;
- delegated authority is unbounded unless revoked.

Useful abstract representation:

`G_A = (V, E_delegate, E_report, E_review, E_escalate, E_transfer, E_execute)`.

New cross-domain boundary:

**organizational hierarchy alone is not sufficient evidence for one authority ordering, one responsibility ordering, or a realized DSD axis.**

## ADMIN-003 / Global Case 028

Topic: review, revision, reopening, resumption, and error correction under changing information.

Witness families:

- U.S. Army FRAGORD modification of existing OPORDs;
- FAA amended clearances, readback correction, revised instructions, and resumption procedures;
- FEMA/NIMS Incident Action Planning execute/evaluate/revise cycles;
- NASA configuration/change control and corrective-action tracking.

Surviving candidate:

`review != approval != amendment != correction != implementation != verification != release != closure != resumption`.

Additional surviving constraints:

- `revision != total replacement`;
- `same final outcome != same organizational path`.

Strong forms rejected:

- approval is organizational immutability;
- any revision invalidates the entire predecessor directive;
- correction and substantive change are identical;
- problem discovery itself authorizes implementation;
- review/approval is implementation;
- implementation is verification/release/closure;
- resumption is an untyped continuation of the earlier state;
- equal final outcomes imply equal change history.

Useful abstract representation:

`G_R = (V, E_review, E_amend, E_correct, E_hold, E_resume, E_supersede, E_implement, E_verify, E_release, E_close)`.

New cross-domain boundary:

**organizational revision is typed and lineage-sensitive; before mapping change into DSD, preserve whichever identity, status, authority, and predecessor/successor distinctions the source organization itself recognizes.**

## Cumulative result after ADMIN-001~003

The first three cases independently separate three organizational interfaces:

1. **instruction-interface failure** — intent, encoding, receipt, interpretation, verification, discretion, execution, feedback;
2. **authority-interface failure** — role, delegation, reporting, retained responsibility, review, escalation, transfer, implementation;
3. **revision/lineage-interface failure** — review, validation, amendment, correction, hold/resume, supersession, implementation, verification, release, closure.

Do not collapse them merely because they occur in one chain of command or contribute to one final outcome.

## Next candidate

The next administration case should be chosen only after checking whether a fourth independent interface adds new pressure rather than repeating ADMIN-001~003. A likely candidate is **reporting/feedback latency and asynchronous information state**, but it remains uncommitted until source families are selected.
