from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
import network_analysis.required_expertise_times


required_expertise_styling = {
                   'background-color': 'black',
                    'label': 'data(title)',
                    #'shape': 'star',
                    "font-size": "15px",
                    'opacity': 'data(expertise_required)',
                    'width': "20px",
                    'height': "20px",
                    "text-wrap": "wrap",
                    "text-max-width": 70
                        }

required_expertise_stylesheet = [
    # make all the nodes neutrally styled
    {'selector': 'node', 'style': required_expertise_styling},
    # make all the edges neutrally styled
    #{'selector': 'edge', 'style': neutral_edge_styling},
    ]