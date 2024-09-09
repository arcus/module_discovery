from dash import Input, Output, dcc 
import module_data 

total_modules = len(module_data.df.index)

def create_clickable_module_list(app):
   @app.callback([Output("mini_card_"+module_id, 'style') for module_id in module_data.df.index],
               Input('hidden_filtered_modules_list', 'children'),
               prevent_initial_callback=True)
   def show_matches(filtered_modules):
      
      # Only show the modules that match the filters
      output_styles = []
      for module_id in module_data.df.index:
         if module_id in filtered_modules:
            output_styles.append({"width":"375px", "display":"block"})
         else:
            output_styles.append({"width":"375px", "display":"none"})
      return output_styles
       
      # Message describing the matching modules
   @app.callback(Output("search_results_message", 'children'),
         Input('hidden_filtered_modules_list', 'children'),
         prevent_initial_callback=True)
   def message(filtered_modules):
      number_of_matches = len(filtered_modules)
      if number_of_matches == total_modules:
         message = dcc.Markdown("Explore all "+str(total_modules)+" modules or use the filters and search bar to find modules that interest you.", style={'background-color': ''})
      elif number_of_matches == 0:
         message = dcc.Markdown("No modules match your current filters and search terms. Try modifying your search or use the **Clear all selections** button to start over.", style={'background-color': ''})
      elif number_of_matches == 1:
         message = dcc.Markdown("There is one module that matches your filters and search terms:", style={'background-color': ''})
      else:
         message = dcc.Markdown("There are "+str(number_of_matches)+" modules that match your filters and search terms:", style={'background-color': ''})
      return message
