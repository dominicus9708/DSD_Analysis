# ADMIN-003 Source Notes

## Source discipline

This case treats organizational procedures as external evidence. DSD terminology is applied only after the source-domain distinctions have been recorded.

## 1. U.S. Army — fragmentary-order modification

### Source

U.S. Army training task report on issuing a fragmentary order (FRAGORD):

https://rdl.train.army.mil/catalog-ws/view/100.ATSC/497D69BD-075B-4144-9A87-3A9F8FE4BCDC-1661890760624/report.pdf

### Used claims

- A FRAGORD may change or modify an existing order or execute a branch/sequel.
- The modified higher order is referenced.
- Standard paragraph headings are retained and portions may explicitly state `No change`.

### Analytic implication

A revision need not destroy the identity or force complete restatement of every unaffected part of the prior order. The source preserves lineage to the higher/base order and distinguishes changed from unchanged portions.

## 2. FAA — amendments, corrections, and resumption

### Sources

FAA Order JO 7110.65, route or altitude amendments:

https://www.faa.gov/air_traffic/publications/atpubs/atc_html/chap4_section_2.html

FAA AIM, ATC clearances and amended clearances:

https://www.faa.gov/Air_traffic/publications/atpubs/aim_html/chap4_section_4.html

FAA AIM, pilot/controller roles and correction of readbacks:

https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap5_section_5.html

FAA Order JO 7110.65, use of `resume` and revised instructions:

https://www.faa.gov/air_traffic/publications/atpubs/atc_html/chap4_section_5.html

### Used claims

- A previously issued route may be amended by identifying only the changed portion and stating that the rest is unchanged.
- Applicable restrictions may need to be restated when an amendment is issued.
- The last ATC clearance takes precedence over the previous clearance.
- Pilots may request clarification or amendment when a clearance is not fully understood or cannot safely be accepted.
- Controllers correct incorrect, distorted, or incomplete readbacks.
- Revised instructions are issued when a clearance cannot be accepted.
- `Resume` phraseology is used in a defined procedural context rather than treating resumption as an untyped continuation.

### Analytic implication

Correction of a communication error, amendment of an operative clearance, and resumption/rejoining are not one undifferentiated operation.

## 3. FEMA/NIMS — iterative incident action planning

### Sources

FEMA Incident Action Planning Guide:

https://www.fema.gov/sites/default/files/2020-07/Incident_Action_Planning_Guide_Revision1_august2015.pdf

FEMA Incident Action Planning Process:

https://training.fema.gov/emiweb/is/icsresource/assets/incident%20action%20planning%20process.pdf

### Used claims

- Phase 5 is explicitly `Execute, Evaluate, and Revise the Plan`.
- Execution is evaluated in preparation for revision in the next operational period.
- After the initial operational period, incident objectives may be validated, modified, or replaced by new objectives.
- Planning meetings provide a final review/approval step before the upcoming operational period.

### Analytic implication

Review is not synonymous with change: it can validate the existing objective, modify it, or lead to a new objective. Organizational planning can be cyclic and revisable rather than a monotone approval chain.

## 4. NASA — controlled change and corrective action

### Sources

NASA Systems Engineering Handbook, Configuration Management:

https://www.nasa.gov/reference/6-5-configuration-management/

NASA Software Engineering Handbook, authorizing changes:

https://swehb.nasa.gov/spaces/7150/pages/16450445/SWE-082%2B-%2BAuthorizing%2BChanges

NASA Software Engineering Handbook, change request/problem report:

https://swehb.nasa.gov/spaces/7150/pages/16449697/SWE-113%2B-%2BSW%2BChange%2BRequest_Problem%2BReport

NASA Software Engineering Handbook, corrective action for inconsistencies:

https://swehb.nasa.gov/spaces/7150/pages/16449656/SWE-054%2B-%2BCorrective%2BAction%2Bfor%2BInconsistencies

### Used claims

- Configuration change management separates proposal, justification, evaluation, incorporation of approved changes, and verification of implementation.
- Changes are authorized before implementation.
- Change/problem reports can separately record discovery, analysis, disposition, corrective action, implementation, testing/verification, release, and closure status.
- Corrective actions are tracked to closure and can include review, implementation, escalation, and archival.
- A workaround may exist while a change is being developed or tested.

### Analytic implication

`problem discovered`, `change proposed`, `change approved`, `change implemented`, `change verified`, `release`, and `closure` are not interchangeable states.

## 5. DSD source interfaces used

### Formation Axiom System

Relevant distinctions:

- candidate/admitted/describable states are typed separately;
- undefined assignment, defined zero, channel absence, and defined zero-valued channel are distinct;
- a full descriptor retains candidate structures rather than only a reduced successful output;
- formation traces preserve witness history without making the history part of operational channel identity.

Used only as a discipline against collapsing statuses or provenance.

### Structural Reorganization Dynamics

Relevant sections and claims:

- Section 4: temporal lineage and state identity;
- Section 5: structural reorganization classes;
- Section 5.4: status/domain transitions;
- Section 5.5: channel- and formation-level transitions;
- Section 14: rank, closure, and regime transitions;
- a change to a coordinate belonging to inherited channel identity is not represented as value evolution of one unchanged channel;
- cross-time lineage is additional data when formation-level identity changes.

This is the strongest DSD-side correspondence for ADMIN-003.

### Channel-Indexed Static Aggregation

Relevant section:

- Section 11: support-tagged records and aggregate-level information loss.

Used to reject the inference that equal final aggregate/readout implies equal revision or correction history.

### Axis-Property System

No special axis-property mapping is required by this case. Hierarchy, version order, or approval order alone is not evidence of a realized DSD axis.
