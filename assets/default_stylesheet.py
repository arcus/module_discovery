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
        'opacity': .2,
        'width': '1px',
        #'mid-source-arrow-shape': 'triangle',
        #'source-arrow-color': 'red',
        #'source-arrow-shape': 'triangle',
        #'line-color': 'red'

         }

selected_styling = {
                'background-color': 'blue',
                'label': 'data(title)',
                'opacity': 1,
                'width': "20px",
                'height': "20px",

                    }

unselected_styling = {
                   'background-color': 'lightgrey',
                    'label': ' ',
                    #'opacity': .3,
                    'width': "5px",
                    'height': "5px",
                        }

active_node_styling = {
                   'background-color': 'black',
                    'label': 'data(title)',
                    "font-size": "20px",
                    'opacity': 1,
                    'width': "30px",
                    'height': "30px",
                        }


default_stylesheet = [
    # make all the nodes neutrally styled
    {'selector': 'node', 'style': neutral_node_styling},
    # make all the edges neutrally styled
    {'selector': 'edge', 'style': neutral_edge_styling},
    ]