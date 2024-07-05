from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
from .module_cards import card_structure
import module_data 

total_modules = len(module_data.df.index)

def create_clickable_module_list(app):
   @app.callback(Output('clickable_module_links', 'children'),
               Output("search_results_message", 'children'),
               Input('hidden_filtered_modules_list', 'children'))
   def create_module_links(matching_modules):
      matches = []
      for module_id in module_data.df.index:
         title = module_data.df.loc[module_id, 'title']
         button_id = str(module_id)+"_button"
         if module_id in matching_modules:
            button = dbc.Col(card_structure.module_card(module_id), width=4)#dbc.Button(title, id=button_id, n_clicks=0, color="dark", outline=True, size="sm",)
            matches.append(button)
         else:
            button = html.Button(module_id, id=button_id, n_clicks=0, style = dict(display='none'))
            matches.append(button)
      number_of_matches = len(matching_modules)
      if number_of_matches == total_modules:
         message = dcc.Markdown("Explore all "+str(total_modules)+" modules or use the filters and search bar to find modules that interest you.", style={'background-color': ''})
      elif number_of_matches == 0:
         message = dcc.Markdown("No modules match your current filters and search terms. Try modifying your search or use the **Clear all selections** button to start over.", style={'background-color': ''})
      else:
         message = dcc.Markdown("There are "+str(number_of_matches)+" modules that match your filters and search terms:", style={'background-color': ''})
      return html.Div(matches, className="d-xxl-flex flex-xxl-wrap"), message
