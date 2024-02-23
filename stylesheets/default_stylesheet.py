from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

neutral_node_styling = {
        'color': "gray",
        "font-size": "20px",
        'width': "5px",
        'height': "5px",
        'opacity': .3,
        'label': " "
         }

neutral_edge_styling = {
        'color': "lightgray",
        'opacity': .4,
        'width': '2px',
        'mid-source-arrow-shape': 'vee',
        #'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        #'line-color': 'red'

         }

pathway_edge_styling = {
        'color': "blue",
        'opacity': .75,
        'width': '3px',
        'mid-source-arrow-shape': 'vee',
        #'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        'line-color': 'black'

         }

selected_styling = {
                'background-color': 'blue',
                #'label': 'data(title)',
                #'color': 'black',
                #"font-size": "12px",
                #'opacity': 1,
                #'width': "10px",
                #'height': "10px",
                #"text-wrap": "wrap",
                #"text-max-width": 80,
                # 'text-halign':'center',
                # 'text-valign':'center',
                # 'width':'label',
                # 'height':'label',
                # 'shape':'square'

                    }

unselected_styling = {
                   'background-color': 'lightgrey',
                    #'label': ' ',
                    #'opacity': .3,
                    'width': "7px",
                    'height': "7px",
                        }

active_node_styling = {
                   'background-color': 'black',
                    'label': 'data(title)',
                    'shape': 'star',
                    "font-size": "20px",
                    'opacity': 1,
                    'width': "30px",
                    'height': "30px",
                    "text-wrap": "wrap",
                    "text-max-width": 80
                        }


default_stylesheet = [
    # make all the nodes neutrally styled
    {'selector': 'node', 'style': neutral_node_styling},
    # make all the edges neutrally styled
    {'selector': 'edge', 'style': neutral_edge_styling},
    ]