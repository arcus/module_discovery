from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

user_visualization_options = dbc.Row([
dcc.Checklist(
           options=[
       {'label': ' Highlight your search results', 'value': 'show_search_results'},
       {'label': ' Highlight your pathway', 'value': 'show_pathway'},
       {'label': ' Display module titles', 'value': 'show_titles'}
       ],
          value=['show_search_results',"show_pathway" ],
          id='visualization_checklist')])