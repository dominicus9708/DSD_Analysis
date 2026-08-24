# DSD Analysis Case Index

Cases remain stored by external domain. This index adds the analysis-purpose classification without moving historical case paths.

| Global case | Topic | Primary purpose | Secondary purpose |
|---|---|---|---|
| 001 | partial functions, undefined vs zero | coherence | predefinition/status fidelity |
| 002 | many-sorted logic, typed applicability | coherence | reinterpretation |
| 003 | Institution Theory, strict equivalence | coherence | reinterpretation |
| 004 | Free Logic, formation/existential import | predefinition | coherence |
| 005 | Strong Kleene K3, undefined-as-value | coherence | predefinition |
| 006 | Public Announcement Logic, observer update | coherence | predefinition / reinterpretation |
| 007 | Linear Logic, channel multiplicity | coherence | reinterpretation |
| 008 | Primitive PI direct attack | falsification | predefinition/signature boundary |
| 009 | Primitive PII direct attack | falsification | coherence boundary |
| 010 | integrated Formation + Axis countermodel search | falsification | coherence |
| 011 | Formation partiality, typing, and closure coherence | coherence | predefinition audit |
| 012 | meeting nonattendance, uncast/invalid ballots, presumption of innocence | reinterpretation | coherence / predefinition / explicit-default / burden-shift audit — **cross-jurisdiction revalidated** |
| 013 | responsibility-attribution multi-regime describability | reinterpretation | coherence / predefinition / regime-interface / office-function audit — **cross-jurisdiction revalidated** |
| 014 | agency, mandate, representation, authority, and attribution | reinterpretation | coherence / predefinition / role-authority-attribution audit — **cross-jurisdiction revalidated** |
| 015 | evidence submission, admissibility, probative weight, and factual finding | reinterpretation | coherence / predefinition / evidence-interface / proof-route audit — **cross-jurisdiction revalidated** |
| 016 | procedural formation, validity, defect consequence, effect, recognition/enforcement | reinterpretation | coherence / predefinition / universal-claim falsification — completed |
| 017 | obligation, permission, prohibition, exception/exemption, normative rule scope | reinterpretation | coherence / predefinition / rule-scope / universal-claim falsification — completed |
| 018 | legal status, capacity, power, exercisability, exercise, and effect | reinterpretation | coherence / predefinition / status-power / universal-claim falsification — completed |
| 019 | rule conflict, harmonization, exception, priority, invalidity | reinterpretation | coherence / predefinition / conflict-resolution / universal-claim falsification — completed |
| 020 | irreversibility, irreparable harm, uncertainty, finality, and procedural safeguards | reinterpretation | falsification / coherence / predefinition / temporal-preservation analysis — completed |
| 021 | responsibility, sanction, victim recovery, emotion, social cost, legal/practice status | reinterpretation | coherence / predefinition / post-responsibility / social-input analysis — completed |
| 022 | investigation, historical-event reconstruction, witness/trace provenance, source dependence | reinterpretation | falsification / coherence / predefinition / investigative-epistemic audit — **first-pass cross-jurisdiction complete** |
| 023 | distributed responsibility, command/superior control, individual liability, State attribution | reinterpretation | falsification / coherence / predefinition / distributed-responsibility audit — **first-pass cross-jurisdiction complete** |
| 024 | legal temporality: commencement, provisional application, retroactivity, repeal, termination, residual effects | reinterpretation | falsification / coherence / predefinition / temporal-rule audit — **first-pass cross-jurisdiction complete** |
| 025 | collective decision formation, voting, quorum, thresholds, veto/blocking, institutional attribution | reinterpretation | falsification / coherence / predefinition / collective-decision audit — **first-pass cross-jurisdiction complete** |
| 026 | organizational instruction, interpretation, verification, discretion, execution, feedback, outcome | reinterpretation | falsification / coherence / predefinition / instruction-interface audit — **first-pass cross-domain complete** |
| 027 | delegation, escalation, parallel authority, transfer of command, responsibility, implementation | reinterpretation | falsification / coherence / predefinition / multi-authority audit — **first-pass cross-domain complete** |
| 028 | review, revision, reopening, resumption, error correction, implementation, verification, closure | reinterpretation | falsification / coherence / predefinition / revision-lineage audit — **first-pass cross-domain complete** |
| 029 | static typing, construction, runtime validity, operation applicability, evaluation, result | reinterpretation | falsification / coherence / predefinition / operational-semantics audit — **first-pass cross-subfield complete** |
| 030 | authentication, authorization, scoped privilege/credential, admission, execution/effect | reinterpretation | falsification / coherence / predefinition / access-control audit — **first-pass cross-subfield complete** |

## Domain folders

- `logic/` — logic, formal semantics of logic, and direct axiom stress-test cases
- `law/` — law, institutions, authority, procedure, evidence, legal effect, normativity, capacity/power, rule conflict, irreversibility, sanction/remedy, social response, investigation, distributed responsibility, legal temporality, collective decisions, and decision structures
- `administration/` — administration, organizations, command/directive systems, reporting relationships, delegation, review, feedback, revision, and operational decision structures
- `computer_science/` — type systems, program semantics, runtime state, formal specification, software verification, access control, and security-oriented structural failure cases

The law-domain foundation and sequence are documented in:

- `law/FOUNDATIONAL_FRAMEWORK.md`
- `law/LAW_001_010_CROSS_CASE_SYNTHESIS.md`
- `law/LAW_001_014_FINAL_SYNTHESIS.md`
- `law/README.md`

The administration/organization sequence is documented in:

- `administration/README.md`
- `administration/ADMIN_001_003_FOUNDATIONAL_SYNTHESIS.md`

The computer-science sequence is documented in:

- `computer_science/README.md`
- `computer_science/029_type_construction_runtime_validity/`
- `computer_science/030_authentication_authorization_execution/`

## Cross-domain status

Legal foundation status: **closed for prerequisite cross-domain testing; falsification and specialized legal extensions remain open**.

Administration/organization foundation status: **ADMIN-001~003 first foundational series provisionally closed; active falsification and specialized extensions remain open**.

Computer science/type/program-semantics status: **CS-001~002 / Global Cases 029~030 first-pass analyses complete; broader campaign remains open**.

- CS-001 / Global Case 029: `cross-subfield computational non-totalization candidate; well-typed=terminating, declared=applicable, type-correct=normal-return, None/error=undefined, runtime-failure=typing-failure, and same-output=same-history identity models rejected; active falsification remains open`.
- CS-002 / Global Case 030: `cross-subfield access-control non-totalization candidate; authentication=authorization, identity=permission, valid-token=universal-access, authorization=admission/effect, denial=authentication-failure, and same-principal=same-permission models rejected; active falsification remains open`.

Witness families for CS-002:

- NIST SP 800-63-4 digital authentication/authorization terminology;
- NIST SP 800-162 ABAC;
- OAuth 2.0 scoped access tokens and resource-server validation;
- Kubernetes authentication, authorization, and admission pipeline.

## Purpose folders

- `../campaigns/falsification/`
- `../campaigns/coherence/`
- `../campaigns/predefinition/`
- `../campaigns/reinterpretation/`

## Rule

A case's physical folder answers **where the source problem belongs**. The campaign index answers **what the DSD analysis is trying to establish**. Do not duplicate case evidence into multiple campaign folders.

Cross-domain recurrence is not treated as proof by analogy. Each new domain must independently preserve its own source concepts and may falsify a DSD-style application assumption.

## Current phase

Completed legal foundation:

- LAW-001 through LAW-014 plus final legal-domain synthesis and closure audit.

Administration/organization:

- ADMIN-001~003 foundational series provisionally closed.

Computer science/type/program semantics:

- CS-001 / Global Case 029 first-pass analysis complete.
- CS-002 / Global Case 030 first-pass analysis complete.
- CS-002 surviving audit separation: `authentication status != authorization relation/decision != bounded privilege/credential != downstream admission != execution/effect`.
- CS-002 is independent from CS-001 because request-specific policy relations, scoped delegated authorization, and post-authorization admission are not reducible to the prior type/runtime/evaluation interface.
- The next strongest candidates are check-time/use-time state change, data/syntax reinterpretation, and illegal downstream state reachability; each requires overlap audit before opening.
