## Use networkx tools to analyze the network proprities of the graph of modules so that that data can be incorporated into later visualizations.

import networkx as nx 

# Import the module data as a dataframe
import module_data
df = module_data.df

# Create a networkx graph with module ids as its vertices
G = nx.DiGraph()
G.add_nodes_from(df.index)

# Add directed edges from depends_on_knowledge_in and sets_you_up_for
for module_id in df.index:
    for linked_module in df.index:
        if str(linked_module) in str(df.loc[module_id, "sets_you_up_for"]):
            G.add_edge(module_id, linked_module)
        #elif str(linked_module) in str(df.loc[module_id, "depends_on_knowledge_available_in"]):
        #    G.add_edge(linked_module, module_id)

print(G)
