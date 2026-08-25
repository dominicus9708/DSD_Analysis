# K_R-002 / Global Case 040

Status: first-pass analysis completed.

Topic: class/property vocabulary versus actual property assertion.

Primary question: in OWL 2, do class membership, property declaration, domain/range axioms, or property characteristics automatically generate a concrete property assertion for an individual?

Tests:
- declaration versus nonempty property extension;
- class membership plus domain versus concrete property assertion;
- range and functional constraints versus relation existence;
- reverse direction: actual property assertion plus domain/range can entail class membership.

DSD comparison target: property kind declared is distinct from application/value supplied.

Boundary: OWL class membership and property assertions are not identified with DSD axis applicability, property assignments, or operational channels.