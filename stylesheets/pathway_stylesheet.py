from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 


def pathway_node_styling_by_number(n):
    styling = {
                'content': n,
                'text-halign':'center',
                'text-valign':'center',
                'width':'label',
                'height':'label',
                'shape':'round-pentagon'
            }

pathway_node_styling = {
                #'background-color': 'red',
                #'label': 'data(title)',
                'color': 'black',
                "font-size": "9px",
                'opacity': 1,
                'width': "10px",
                'height': "10px",
                #"text-wrap": "wrap",
                #"text-max-width": 80,
                "border-width": 3,
                "border-style": 'solid', # solid, dotted, dashed, or double.
                "border-color": "purple",
                # 'text-halign':'center',
                # 'text-valign':'center',
                # 'width':'label',
                # 'height':'label',
                # 'shape':'square'

                    }
pathway_node_styling_red = {
                #'background-color': 'red',
                'label': 'data(title)',
                'color': 'black',
                "font-size": "9px",
                'opacity': 1,
                'width': "20px",
                'height': "20px",
                "text-wrap": "wrap",
                "text-max-width": 80,
                "border-width": 3,
                "border-style": 'double', # solid, dotted, dashed, or double.
                "border-color": "red",
                    }
pathway_node_styling_yellow = {
                #'background-color': 'red',
                'label': 'data(title)',
                'color': 'black',
                "font-size": "9px",
                'opacity': 1,
                'width': "20px",
                'height': "20px",
                "text-wrap": "wrap",
                "text-max-width": 80,
                "border-width": 3,
                "border-style": 'double', # solid, dotted, dashed, or double.
                "border-color": "yellow",
                    }

pathway_node_styling_green = {
                #'background-color': 'red',
                #'label': 'data(title)',
                'color': 'black',
                "font-size": "9px",
                'opacity': 1,
                'width': "20px",
                'height': "20px",
                "text-wrap": "wrap",
                "text-max-width": 80,
                "border-width": 3,
                "border-style": 'double', # solid, dotted, dashed, or double.
                "border-color": "green",
                    }

non_pathway_edge_styling = { # These are edges of hasse that are not being used in the pathway itself.
        #'color': "blue",
        'opacity': .25,
        'width': '3px',
        'mid-source-arrow-shape': 'vee',
        'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        'line-color': 'black'

         }

non_pathway_node_styling = { # These are nodes that are not in the user's pathway.
                #'background-color': 'red',
                #'label': 'data(title)',
                'color': 'black',
                "font-size": "5px",
                'opacity': .75,
                'width': "10px",
                'height': "10px",
                #"text-wrap": "wrap",
                #"text-max-width": 80,
                # 'text-halign':'center',
                # 'text-valign':'center',
                # 'width':'label',
                # 'height':'label',
                # 'shape':'square'

                    }
