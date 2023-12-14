import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#EDUCATION_MODULES

#read in metadata from education_modules repository, which is automatically updated each week via a github action
education_modules_df = pd.read_json("./assets/education_modules.json") 

#remove empty rows created by data processing
education_modules_df= education_modules_df.dropna(axis=0, how='all')

#set 'module_id' as the index
education_modules_df = education_modules_df.set_index('module_id')

# make estimated_time_in_minutes an integer instead of a float
education_modules_df['estimated_time_in_minutes'] = education_modules_df['estimated_time_in_minutes'].astype(int)

#CREATE THE DATAFRAME FOR APP USE
df=education_modules_df.astype('str').copy()

#print(df) 

# Create a networkx graph with module ids as its vertices
G = nx.DiGraph()
G.add_nodes_from(df.index)

# Add directed edges from depends_on_knowledge_in and sets_you_up_for
for module_id in df.index:
    for linked_module in df.index:
        if str(linked_module) in str(df.loc[module_id, "sets_you_up_for"]):
            G.add_edge(module_id, linked_module)
        if str(linked_module) in str(df.loc[module_id, "depends_on_knowledge_available_in"]):
            G.add_edge(linked_module, module_id)
print("Is G a directed acyclic graph?")
print(nx.is_directed_acyclic_graph(G))
poset = nx.transitive_closure(G)
hasse = nx.transitive_reduction(G)

P = poset
H = hasse

print(len(G.edges()))
print(len(P.edges()))
print(len(H.edges()))
print(nx.connected_components(G))
#nx.draw(H, pos=nx.spring_layout(H))
#plt.show()
