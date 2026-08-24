# Scope — CS-002 / Global Case 030

## Included

- distinction between authentication and authorization;
- authorization as a request-specific policy relation;
- scoped/delegated authorization credentials;
- post-authorization admission gates;
- finite witness separating authentication success, authorization denial, admission rejection, and successful effect;
- DSD mapping/nonmapping audit.

## Excluded

- password cracking, credential theft, exploit development, or offensive security technique;
- temporal revocation races and check-time/use-time bugs (reserved for a later case);
- cryptographic proof strength comparison;
- implementation-specific vulnerability enumeration;
- claim that all systems implement NIST ABAC, OAuth, or Kubernetes pipelines;
- claim that authorization is itself a DSD axis property;
- universal mapping from HTTP status codes or security errors to DSD statuses.

## Generalization discipline

The case establishes a cross-source structural distinction, not a universal security architecture. Each external framework retains its own terminology and state machine.

The valid generalization is only that identity/authentication evidence alone does not justify collapsing request-specific authorization, scope, admission, and effect when the source system distinguishes them.
