# Callbacks

Callbacks are what provide interactivity with the app.  When users click on interactive elements like buttons, nodes, drop-down menus, etc., callbacks are triggered.  Callbacks take inputs (what was interacted with that is triggering a new action) and outputs (what will next change in our layout).

It is helpful to document what happens when a user interacts with the app... what callbacks are triggered and under what circumstances?

E.g. (and I'm probably wrong):

* [active_node_in.py](active_node_in.py) is triggered when a user clicks on a node in the displayed graph which represents an asset or a button that is displaying the name of an asset.  The input could be ... or ..., and the outputs...

* add each callback here, consider adding screenshots even of the elements that are inputs and/or outputs.