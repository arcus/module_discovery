from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from stylesheets import default_stylesheet, active_module_stylesheet
from network_analysis import poset_processing as poset

df = module_data.df

### Whatever the ACTIVE NODE is, it will be visually displayed with modules connected to it.
def active_node_out(app):
    @app.callback(Output('active_module_visualization', 'elements'),
                Output('active_module_visualization', 'stylesheet'),
                Input('hidden_active_module', 'children')
                )
    def active_node_output(active_module):
        if str(active_module) in df.index:
            # Build the graph as both a cytoscape and networkx object
            neighborhood_cytoscape = [{'data': {'id': active_module, 'title': df.loc[active_module,'title'] }, 'position': {'x': 0, 'y': 0} }]
            neighborhood_networkx = [active_module]
     
            # break the preceding modules into levels based on max distance from the active module
            level_dict = {}
            for neighbor in poset.poset.reverse().neighbors(active_module):
                level = max([len(path) for path in nx.all_simple_paths(poset.hasse, neighbor, active_module)])
                level_dict[neighbor] = level

            # Add the preceding modules by level in specific positions
            if level_dict != {}:
                top_level = max(level_dict.values())
                for i in range(1,top_level+1):
                    n_at_level = list(level_dict.values()).count(i)
                    n_at_level_index = - n_at_level/2 +.5 # index to make sure the covering modules are evenly spaced out
                    for neighbor in poset.poset.reverse().neighbors(active_module):
                        if level_dict[neighbor] == i:
                            neighborhood_cytoscape.append({'data': {'id': neighbor, 'title': df.loc[neighbor,'title'] }, 'classes':'precedes', 'position': {'x': 90*n_at_level_index, 'y': -50*i} })
                            neighborhood_networkx.append(neighbor)
                            n_at_level_index +=1
            
            # find all modules that immediately follow (cover) the active node in the poset
            n_covers = len(list(poset.hasse.neighbors(active_module)))
            cover_index = - n_covers / 2 +.5 # index to make sure the covering modules are evenly spaced out
            for neighbor in poset.hasse.neighbors(active_module):
                neighborhood_cytoscape.append({'data': {'id': neighbor, 'title': df.loc[neighbor,'title'] }, 'classes':'covers' , 'position': {'x': 90*cover_index, 'y': 75}})
                neighborhood_networkx.append(neighbor)
                cover_index = cover_index + 1
            
            # Use networkx t build the subgraph from these preceding and covering nodes
            active_node_subgraph = poset.hasse.subgraph(neighborhood_networkx)

            # Add the edges to the cytoscape version of the graph
            for edge in active_node_subgraph.edges():
                neighborhood_cytoscape.append({'data': {'source': edge[1], 'target': edge[0]}})
            
            # Create the stylesheet
            new_stylesheet = [ {'selector': '.covers', 'style': active_module_stylesheet.next_module_styling}]
            new_stylesheet +=[ {'selector': '.precedes', 'style': active_module_stylesheet.preceding_module_styling}]
            new_stylesheet += [ {'selector': 'edge', 'style': active_module_stylesheet.active_module_visualization_edge_styling}]
            selector = str('[id *= "')+str(active_module)+str('" ]')
            new_stylesheet.append({'selector': selector, 'style': active_module_stylesheet.active_module_styling})
            
            return neighborhood_cytoscape, new_stylesheet
            
        else:
            return [], default_stylesheet.default_stylesheet
