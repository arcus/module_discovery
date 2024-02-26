from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

user_visualization_options = dbc.Row([
    dbc.Col([
        dcc.Checklist(
            options=[
                {'label': ' Highlight your search results', 'value': 'show_search_results'},
                {'label': ' Highlight your pathway', 'value': 'show_pathway'},
                ],
                    value=['show_search_results',"show_pathway" ],
                    id='visualization_checklist')]),
    dbc.Col([
        dcc.Checklist(
            options=[
                {'label': ' Show search result module titles', 'value': 'show_search_results_titles'},
                {'label': ' Show pathway module titles', 'value': 'show_pathway_titles'},
                ],
                    value=[],
                    id='visualization_titles_checklist')
          ])
          ])