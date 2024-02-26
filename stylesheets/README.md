# Stylesheets

Stylesheets for the cytoscape visualizations live here.
See the [Dash Cytoscape style documentation](https://dash.plotly.com/cytoscape/styling) or the more extensive (but possibly not fully implemented in Dash) [Cytoscape.js style documentation](https://js.cytoscape.org/#style).


Possible scheme for how different nodes are differentiated:

## Active node - Shape and size

The active node is distinguished visually by being star-shaped and bigger than the other nodes around it.

## Pathway nodes - Border

Modules on a user's pathway are distinguished visually by having a brightly colored border in addition to whatever other styling they take on.

## Pathway edges - Color and line-style

Edges denoting the pathway's route through the modules are thicker than other edges.

- Solid blue edge from A to B: module B immediately depends on knowledge delivered in module A
- Dashed blue edge from A to B: module B does not immediately depend on knowledge delivered in module A, but neither does module A depend on knowledged delivered in module B. In these cases modules A and B may be unrelated, or there may be a missing module that should be between them (TODO check for this, suggest adding addition modules to a pathway, etc.)
- Dashed red edge from A to B: modules A and B are in the wrong order relative to each other! Module A depends on knowledge available in module B.

TODO: these edge colors only help with the edges created by the pathway, if A depends on knowledge in B, but the pathway goes A->C->B, there won't be a red edge because A->C and C->B are both okay. Possible solutions: 
- color vertices or borders based on "okayness" in the pathway: red for there are things this module depends on later in the pathway, yellow for there are things this module depends on that aren't in the pathway at all, green for everything this module depends on is in the pathway? 
- consider the "ragged start" being yellow, only making a module that color if it _immediately_ depends on knowledge available in modules not in the pathway (i.e. check covering relations from Hasse diagram, not full poset relationships)

## Search Results - Color

Modules that match the user's search results are distinguished by color - they are blue rather than gray or black.