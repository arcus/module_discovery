from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 


pathway_edge_styling = {
        #'color': "blue",
        'opacity': .75,
        'width': '3px',
        'mid-source-arrow-shape': 'vee',
        'mid-source-arrow-color': 'black',
        #'source-arrow-shape': 'triangle',
        'line-color': 'black'

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
