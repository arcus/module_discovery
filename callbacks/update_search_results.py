### The update_search_results function takes the checklist and radio buttons from the left_hand_nav_bar and returns a list of all modules that match the given filters.
from dash import Input, Output
import module_data 
from components.explore_modules.left_hand_nav_bar import search_panel 
from assets.levels import module_level
search_results = search_panel.search_results

def update_search_results(general_options_value, coding_language_value, coding_level_value,level_value, data_task_value, data_domain_value, search_term, collection_value):
    matching_modules = list(module_data.df.index).copy()
    non_matching_modules = []
    for module in module_data.df.index:
        tracker = 1
        if general_options_value and 'good_first_module' in general_options_value:
            if "true" not in str(module_data.df.loc[module, "good_first_module"]).lower():# allow for True, true, or trailing spaces in data entry.
                tracker = tracker*0
        if general_options_value and 'no_coding_required' in general_options_value:
            if "true" in str(module_data.df.loc[module, "coding_required"]).lower():
                tracker = tracker*0
        if general_options_value and 'exercise' in general_options_value:
            if "exercise" not in str(module_data.df.loc[module, "module_type"]).lower():
                tracker = tracker*0
        if coding_language_value:
          if coding_language_value.lower() not in str(module_data.df.loc[module,'coding_language']).lower(): # coding language is a radio button, so the output is a string, not a list of strings
                tracker = tracker*0
        if coding_level_value: # coding level is a radio button, so the output is a string, not a list of strings
            if coding_level_value not in str(module_data.df.loc[module,'coding_level']).lower():
                tracker = tracker*0
        if level_value: # level is a radio button, so the output is a string, not a list of strings
            if not level_value == module_level(module):
                tracker = tracker*0
        if data_task_value: # coding level is a radio button, so the output is a string, not a list of strings
            if data_task_value not in str(module_data.df.loc[module,'data_task']).lower():
                tracker = tracker*0
        if data_domain_value: # coding level is a radio button, so the output is a string, not a list of strings
            if data_domain_value not in str(module_data.df.loc[module,'data_domain']).lower():
                tracker = tracker*0
        if search_term and module not in search_results(search_term):
            tracker = tracker*0
        if collection_value: # coding level is a radio button, so the output is a string, not a list of strings
            if collection_value not in str(module_data.df.loc[module,'collection']).lower():
                tracker = tracker*0
        if tracker == 0:
            matching_modules.remove(module)
            non_matching_modules.append(module)
    return matching_modules, non_matching_modules
            

def update_hidden_filtered_modules(app):
    @app.callback(Output('hidden_filtered_modules_list', 'children'),
                Input('general_options_checklist', 'value'),
                Input('coding_language_checklist', 'value'),
                Input('coding_level_checklist', 'value'),
                Input('level_checklist', 'value'),
                Input('data_task_checklist', 'value'),
                Input('data_domain_checklist', 'value'),
                Input('search_input', 'value'),
                Input('collection_checklist', 'value')
                )
    def filtering(value, coding_language_value, coding_level_value, level_value, data_task_value, data_domain_value, search_value, collection_value):
        return update_search_results(value, coding_language_value, coding_level_value, level_value, data_task_value, data_domain_value, search_value, collection_value)[0]
