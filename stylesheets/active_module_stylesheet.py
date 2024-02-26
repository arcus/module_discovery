from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 


active_module_styling = {
                   'background-color': 'black',
                    'label': 'data(title)',
                    'shape': 'star',
                    "font-size": "15px",
                    'opacity': 1,
                    'width': "20px",
                    'height': "20px",
                    "text-wrap": "wrap",
                    "text-max-width": 70
                        }

next_module_styling = {
                    'background-color': 'blue',
                    'label': 'data(title)',
                    'color': 'black',
                    "font-size": "10px",
                    'opacity': 1,
                    'width': "20px",
                    'height': "20px",
                    "text-wrap": "wrap",
                    "text-max-width": 65,
                        }

preceding_module_styling = {
                    'background-color': 'green',
                    'label': 'data(title)',
                    'color': 'black',
                    "font-size": "8px",
                    'opacity': 1,
                    'width': "20px",
                    'height': "20px",
                    "text-wrap": "wrap",
                    "text-max-width": 55,
                        }

active_module_visualization_edge_styling = {
        #'color': "blue",
        'opacity': .35,
        'width': '3px',
        'mid-source-arrow-shape': 'vee',
        'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        'line-color': 'black'

         }
