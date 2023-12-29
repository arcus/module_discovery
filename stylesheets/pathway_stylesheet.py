from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 


pathway_edge_styling = {
        #'color': "blue",
        'opacity': .75,
        'width': '5px',
        'mid-source-arrow-shape': 'vee',
        'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        'line-color': 'blue'

         }

pathway_node_styling = {
                #'background-color': 'red',
                'label': 'data(title)',
                'shape': 'star',
                # 'outline-width' : '3px', 
                # 'outline-color' : "black",
                'color': 'black',
                "font-size": "12px",
                'opacity': 1,
                'width': "20px",
                'height': "20px",
                "text-wrap": "wrap",
                "text-max-width": 80,
                # 'text-halign':'center',
                # 'text-valign':'center',
                # 'width':'label',
                # 'height':'label',
                # 'shape':'square'

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
