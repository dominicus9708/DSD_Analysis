# LAW-007 Finite Witnesses

## Witness A — right exists before present exercisability

UNIDROIT Chapter 10 notes that an obligation/right may exist even though performance cannot yet be required and the right is not yet exercisable.

Therefore:

`right exists`

`!= right presently exercisable`.

## Witness B — right exists and is exercisable but has not been exercised

Under UNIDROIT Article 7.3.2, a party may have the right to terminate, but the right is exercised by notice.

Before notice:

`right exists`

and potentially

`right is exercisable`,

while

`exercise event has not occurred`.

## Witness C — exercise event changes downstream effect

Once the required notice is received under the governing rules, the termination right is exercised and downstream termination consequences can follow.

Thus:

`right`

`!= notice/exercise event`

`!= downstream effect`.

## Witness D — limitation bars enforcement without extinguishing the right

UNIDROIT Article 10.9 states that expiration of the limitation period does not extinguish the right and that its effect depends on the obligor asserting the limitation defence.

Therefore:

`right continues to exist`

while

`enforcement can become barred`.

A single `HAS_RIGHT/NO_RIGHT` bit loses the distinction.

## Witness E — entity capacity versus actor authority

VCLT Article 6 gives every State capacity to conclude treaties.

Article 7 separately determines when a person is authorized to represent the State for treaty acts.

Therefore:

`State has treaty capacity`

`!= this actor is authorized for this treaty act`.

## Witness F — act exists but lacks legal effect until confirmation

VCLT Article 8 allows an unauthorized treaty-related act to exist as an event while declaring it without legal effect unless later confirmed by the State.

Therefore:

`exercise event occurred`

`!= effective exercise`.

Later confirmation can alter the effect without deleting the historical event.

## Witness G — recognized legal capacity and support for exercise

CRPD Article 12(2) recognizes equal legal capacity; Article 12(3)-(4) separately regulates support and safeguards for the exercise of legal capacity.

Therefore a model that encodes a need for support as absence of legal capacity is source-incompatible.

## Finite compression obstruction

Take five source states:

1. right/capacity recognized but not yet exercisable;
2. right exercisable but not exercised;
3. right exercised and effective;
4. right remains but enforcement is barred;
5. exercise event occurred but effect is withheld pending confirmation.

No single binary `POWER = {YES,NO}` assignment preserves all five distinctions.
