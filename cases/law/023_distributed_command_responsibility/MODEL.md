# LAW-012 Model — Multi-Route Responsibility and Attribution

## 1. Do not use one responsibility scalar

A source-faithful record may need:

`(event, direct_actor, direct_conduct, superior, formal_role, effective_control, knowledge_state, omission_or_order, individual_liability_mode, public_capacity, attribution_rule, attributed_entity, entity_or_state_responsibility, time, regime)`.

Not every source system uses every coordinate.

## 2. Distinctions

`direct perpetration != ordering != superior omission`.

`formal command != effective control`.

`influence != effective control`.

`individual liability != attribution of conduct to State/entity`.

`State attribution != proof of the individual's criminal guilt`.

`ultra vires conduct != automatic private conduct`.

`same event != same responsibility basis for every actor/entity`.

## 3. Graph representation

Use a source-indexed graph rather than a chain:

`G_R = (V, E_R)`.

Possible vertices include direct conduct, superior relation, knowledge state, control state, attribution state and responsibility state.

Each edge must come from a source rule, e.g.:

- direct participation rule;
- ordering/inducement rule;
- command/superior responsibility rule;
- State-organ attribution rule;
- ultra vires attribution rule;
- instruction/direction/control attribution rule.

No universal edge is assumed merely because two vertices belong to the same event.

## 4. Important non-collapse

Multiple responsibility states may coexist without identity.

`A != B` does not imply that only one can be true.

The same historical conduct can support different source-defined responsibility or attribution relations at different legal levels.
