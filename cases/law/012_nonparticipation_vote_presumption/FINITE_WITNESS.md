# Finite state witness

This witness is intentionally non-computational. It records the minimum finite distinctions needed for the analysis.

## Meeting vote states

| State | Present | Vote in domain | Value |
|---|---:|---:|---|
| absent | 0 | 0 | — |
| present-abstain | 1 | 0 | — |
| present-no | 1 | 1 | NO |
| present-yes | 1 | 1 | YES |

No function preserving both presence and vote-domain status can identify all three of `absent`, `present-abstain`, and `present-no` without losing information.

## Ballot states

| State | Eligible | Ballot in domain | Valid |
|---|---:|---:|---:|
| non-exercise | 1 | 0 | — |
| submitted-invalid | 1 | 1 | 0 |
| submitted-valid | 1 | 1 | 1 |

Hence non-exercise and invalid submission are disjoint by domain membership before any vote value is examined.

## Criminal-procedure states

| State | Charged | Proof condition met | Guilty judgment permitted by modeled rule |
|---|---:|---:|---:|
| uncharged | 0 | — | 0 |
| charged-unproved | 1 | 0 | 0 |
| charged-proved | 1 | 1 | 1 |

The final column encodes the cited legal rule; it is not derived from DSD. DSD is used only to preserve the distinction among the columns and to block an unstated promotion from the first or second column to the third.

## Information-loss test

The following collapses are non-injective:

- `absent -> NO` together with actual `NO -> NO`;
- `non-exercise -> invalid` together with submitted-invalid -> invalid;
- `charged-unproved -> guilty` together with charged-proved -> guilty.

A non-injective collapse can be adopted as an explicit institutional convention, but the original state cannot then be recovered from the collapsed label alone.
