from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from stylesheets import default_stylesheet 
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
            neighborhood_cytoscape = [{'data': {'id': active_module, 'title': df.loc[active_module,'title'] }}]
            neighborhood_networkx = [active_module]
            # find all modules that precede the active node in the poset
            for neighbor in poset.poset.reverse().neighbors(active_module):
                neighborhood_cytoscape.append({'data': {'id': neighbor, 'title': df.loc[neighbor,'title'] }, 'classes':'precedes' })
                neighborhood_networkx.append(neighbor)
            # find all modules that immediately follow (cover) the active node in the poset
            for neighbor in poset.hasse.neighbors(active_module):
                neighborhood_cytoscape.append({'data': {'id': neighbor, 'title': df.loc[neighbor,'title'] }, 'classes':'covers' })
                neighborhood_networkx.append(neighbor)
            
            # Use networkx t build the subgraph from these preceding and covering nodes
            active_node_subgraph = poset.hasse.subgraph(neighborhood_networkx)

            # Add the edges to the cytoscape version of the graph
            for edge in active_node_subgraph.edges():
                neighborhood_cytoscape.append({'data': {'source': edge[1], 'target': edge[0]}})
            
            # Create the stylesheet
            new_stylesheet = [ {'selector': 'node', 'style': default_stylesheet.selected_styling}]
            new_stylesheet += [ {'selector': 'edge', 'style': default_stylesheet.neutral_edge_styling}]
            selector = str('[id *= "')+str(active_module)+str('" ]')
            new_stylesheet.append({'selector': selector, 'style': default_stylesheet.active_node_styling})
            
            return neighborhood_cytoscape, new_stylesheet
            
        else:
            return [], default_stylesheet.default_stylesheet
