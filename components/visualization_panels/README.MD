# Visualization panels

The visualization panels contain the graphical representations of the modules and their interconnections. 

These visualizations are implemented in [cytoscape](https://dash.plotly.com/cytoscape).

Right now there are different visualizations, one combining the active node, the user's pathway, and their search results, as well as a visualization focused on each of those individually.

## Node positioning

The combined visualization panel is determined using the `cose` layout.

The pathway visualization pulls the positions from the combined visualization panel and uses those node positions as `preset` in its layout.

This means that the layout will not be the same each time the page is refreshed, but will be internally consistent between the different visualizations for a user who loads it once and then moves around between panels.