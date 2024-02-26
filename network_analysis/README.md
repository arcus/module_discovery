# Analyzing the network of modules 

## Initial network analysis in `poset_processing.py`

The linking metadata from the modules is processed here using the `networkx` package.

This can then be called all over the app to use the network (graph theoretic) properties of the interconnections, namely:

- `G` is the graph defined only by the explicit linking metadata from module_data.
- `poset` is the transitive closure of `G`, i.e. all of the relationships implied by the explicitly given relationships. These relationships are used for sorting or ordering modules.
- `hasse` is the transitive reduction of the poset, i.e. the [Hasse diagram](https://en.wikipedia.org/wiki/Hasse_diagram) of the poset. These are the edges that we actually want to show users to keep visualizations from getting too cluttered.

## Helper functions in `pathway_order_relations.py`

Functions return whether the prerequisites to a module are in the pathway, and in the right order relative to the module in question.

