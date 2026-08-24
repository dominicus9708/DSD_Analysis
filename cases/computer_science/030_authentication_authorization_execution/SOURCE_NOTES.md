# Source Notes — CS-002 / Global Case 030

## 1. NIST SP 800-63-4 — digital identity

NIST distinguishes digital authentication from authorization.

- Digital authentication establishes confidence in digitally presented user identities.
- `authorize` is a decision to grant access, typically by evaluating subject attributes.

Source: NIST SP 800-63-4 and glossary, https://pages.nist.gov/800-63-4/sp800-63.html

Immediate pressure: authentication success does not by definition entail access authorization.

## 2. NIST SP 800-162 — Attribute Based Access Control

ABAC determines authorization to perform operations by evaluating attributes of the subject, object, requested operation, and sometimes environment conditions against policy/rules/relationships.

Source: NIST SP 800-162, https://csrc.nist.gov/pubs/sp/800/162/upd2/final

Immediate pressure:

`subject identity alone != authorization state`.

The same subject can receive different decisions for different objects, operations, or environmental conditions.

## 3. OAuth 2.0 / Bearer Token Usage

RFC 6749 requires a resource server to validate an access token, check expiry, and ensure that its scope covers the requested resource.

RFC 6750 distinguishes at least:

- invalid token;
- insufficient scope.

An access token therefore represents bounded authorization rather than universal access. Possession/presentation of a token does not imply adequate scope for a particular resource.

Sources:

- RFC 6749, https://www.rfc-editor.org/rfc/rfc6749.html
- RFC 6750, https://www.rfc-editor.org/rfc/rfc6750.html

Immediate pressure:

`credential/token present != token valid for request != sufficient scope != resource access`.

## 4. Kubernetes API access-control pipeline

Kubernetes documentation separates request handling into authentication, authorization, and—after authorization for relevant requests—admission control.

Authentication associates identity attributes with the request. Authorization evaluates whether the request is allowed. Admission control can still reject or modify requests after an allow authorization decision.

Sources:

- Authentication: https://kubernetes.io/docs/reference/access-authn-authz/authentication/
- Authorization: https://kubernetes.io/docs/reference/access-authn-authz/authorization/
- Extension/access pipeline: https://kubernetes.io/docs/concepts/extend-kubernetes/

Immediate pressure:

`authenticated != authorized != admitted != successful effect`.

Kubernetes also states that authentication-supplied values gain significance for access decisions when interpreted by an authorizer, supporting separation between identity assignment and permission semantics.

## Source-family independence

NIST digital identity gives identity/authentication semantics; NIST ABAC gives relational policy semantics; OAuth gives delegated and scoped authorization semantics; Kubernetes gives a concrete multi-stage API access pipeline. These are not treated as four proofs of one theorem but as independent pressure on the proposed totalizations.
