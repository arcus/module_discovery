from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from stylesheets import default_stylesheet, pathway_stylesheet
from network_analysis import poset_processing as poset
from network_analysis import pathway_order_relations as p_order
import ast

df = module_data.df

def show_pathway_visually(app):
    @app.callback(Output('pathway_visualization', 'elements'),
                Output('pathway_visualization', 'stylesheet'),
                #Output('debugger', 'children'),
                Input('hidden_pathway','children'),
                State('hidden_active_module', 'children'),
                State('module_visualization','elements'),
                prevent_initial_call=True) 
    def update_pathway_graph(hidden_pathway, active_node, raw_element_data):
        ### import all nodes and position data from the module_visualization
        element_data = ast.literal_eval(str(raw_element_data))

        ### Set up the subgraph created by the pathway
        pathway_subgraph = poset.hasse.subgraph(hidden_pathway)

        # The elements of the graph display are the nodes and the edges:
        elements=element_data
        
        ### Create a new stylesheet for this induced pathway subgraph
        # Initialize the non-pathway styling for all nodes and edges
        new_stylesheet = [ {'selector': 'edge', 'style': pathway_stylesheet.non_pathway_edge_styling}]
        new_stylesheet += [ {'selector': 'node', 'style': pathway_stylesheet.non_pathway_node_styling}]
        

        # Node styling is that all of them are selected GET UX HELP TO FIGURE OUT IF THIS MAKES SENSE
        for module_id in pathway_subgraph.nodes():
            selector = str('[id *= "')+str(module_id)+str('" ]')
            # all nodes in the pathway should be labeled
            new_stylesheet += [{'selector': selector, 'style': pathway_stylesheet.pathway_node_styling}]
            
            # # if a node's predecessors are in the pathway before it, color it green
            # if p_order.prereqs_precede(hidden_pathway, module_id):
            #     new_stylesheet += [{'selector': selector, 'style': pathway_stylesheet.pathway_node_styling_green}]
            # # if a node's predecessors follow it in the pathway, color that node red
            # elif p_order.prereqs_follow(hidden_pathway, module_id):
            #     new_stylesheet += [{'selector': selector, 'style': pathway_stylesheet.pathway_node_styling_red}]
            # # if a node's predecessors are not in the pathway, but not before it, color it yellow (learner is starting here and bringing some knowledge to their pathway)
            # else:
            #     new_stylesheet += [{'selector': selector, 'style': pathway_stylesheet.pathway_node_styling_yellow}]

            # the active node should be distinguishable
            if module_id == active_node:
                new_stylesheet +=[{'selector': selector, 'style': default_stylesheet.active_node_styling}]

        return elements, new_stylesheet