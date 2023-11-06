from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
from assets import default_stylesheet 

df = module_data.df

nodes = [
    {
        'data': {
            'id': row, 
            'title': df.loc[row,'title'], 
            },
    }
    for row in df.index 
]

edges = []
# for row in df.index:
#     for linked_module in df.loc[row, 'Linked Courses']:
#         edges.append({'data': {'source': linked_module, 'target': row, 'relationship': 'internal_link'}})
for row in df.index:
    for linked_module in df.index:
        if str(linked_module) in str(df.loc[row,"sets_you_up_for"]):
            edges.append({'data': {'source': row, 'target': linked_module, 'relationship': 'directed_edge'}})
        if str(row) in str(df.loc[linked_module, "depends_on_knowledge_available_in"]):
            edges.append({'data': {'source': linked_module, 'target': row, 'relationship': 'directed_edge'}})


default_stylesheet = default_stylesheet.default_stylesheet

visualization_panel = dbc.Col(
                    children=[
                    html.Br(),
                    dcc.Markdown("##### Interact with this graph \n * Click on a node to learn more about it in the Module Details section. \n * Drag the nodes around to see how they are interconnected.", style={'background-color': '#FFFFFF'}),
                    dbc.Row(cyto.Cytoscape(
                        id='module_visualization',
                        layout={'name': 'cose', 
                                #'nodeDimensionsIncludeLabels': 'true',
                                #'avoidOverlap':'true'
                                },
                        elements=edges+nodes,
                        stylesheet=default_stylesheet,
                        #style={'width': '100%', 'height':'450px%'},
                        userZoomingEnabled=False
                        ), justify="center"),
                     ],
                )
