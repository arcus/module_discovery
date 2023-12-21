The linking metadata from the modules is processed here using the `networkx` package.

This can then be called all over the app to use the network (graph theoretic) properties of the interconnections, namely:

- `G` is the graph defined only by the explicit linking metadata from module_data.
- `poset` is the transitive closure of `G`, i.e. all of the relationships implied by the explicitly given relationships. These relationships are used for sorting or ordering modules.
- `hasse` is the transitive reduction of the poset, i.e. the (Hasse diagram)[https://en.wikipedia.org/wiki/Hasse_diagram] of the poset. These are the edges that we actually want to show users to keep visualizations from getting too cluttered.