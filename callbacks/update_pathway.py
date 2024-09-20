### Take input from the "Add to my list" buttons and update the pathway list
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import network_analysis.poset_processing
import assets.pre_made_pathways.pathways as pathways
pathway_list = pathways.pathway_list

### Module sorting algorithm:
def correctly_ordered(a,b):
    if (a,b) in network_analysis.poset_processing.poset.edges(): ### This ONLY checks if module a precedes module b in the poset of all modules. It does not mean that related modules will be grouped together ?YET?
        return True
    else:
        return False

### If any add_to_my_modules buttons are pressed, that module should be added to the list of my_modules
def update_pathway(app):
    @app.callback(Output('hidden_pathway', 'children'),
                State("hidden_pathway", 'children'),
                State("hidden_filtered_modules_list", 'children'),
                Input("sort_my_modules","n_clicks"),
                Input("add_filtered_to_my_modules", 'n_clicks'),
                Input("remove_filtered_from_my_modules", 'n_clicks'),   
                [Input("add_to_my_modules_"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are add_to_my_modules buttons shown on the module details panel
                #[Input("remove_my_modules_"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are remove_my_modules buttons shown on the module details panel
                [Input(module_id+"_move_up", 'n_clicks') for module_id in module_data.df.index], #these buttons are for moving a module up in the pathway
                [Input(module_id+"_go_down", 'n_clicks') for module_id in module_data.df.index], #these buttons are for moving a module down in the pathway
                [Input(module_id+"_trash",'n_clicks') for module_id in module_data.df.index], #these buttons are for users to remove individual modules from their pathway
                [Input("use_"+pathway["id"],'n_clicks') for pathway in pathway_list], #these buttons are for users to remove individual modules from their pathway
                prevent_initial_call=True)
    def activate(current_pathway,hidden_filtered_modules_list,*args):
        new_pathway = current_pathway.copy()
        
        ## Sort the current pathway list
        if ctx.triggered_id == "sort_my_modules":
            sorted_pathway = current_pathway.copy()[0:1]
            for module in current_pathway[1:]:
                stopper = False
                index = 0
                while stopper == False and index < len(sorted_pathway):
                    if correctly_ordered(module,sorted_pathway[index]): ### The sort condition is defined above
                        sorted_pathway = sorted_pathway[:index] + [module] + sorted_pathway[index:]
                        stopper = True
                    else:
                        index += 1
                if index == len(sorted_pathway):
                    sorted_pathway.append(module)

            new_pathway = sorted_pathway

            
        ## Add a batch of modules all at once
        elif ctx.triggered_id == "add_filtered_to_my_modules":
            for module in list(hidden_filtered_modules_list):
                if module not in new_pathway:
                    new_pathway.append(module)

        ## Remove a batch of modules all at once
        elif ctx.triggered_id == "remove_filtered_from_my_modules":
            for module in list(hidden_filtered_modules_list):
                if module in new_pathway:
                    new_pathway.remove(module)
        
        ## add a whole pathway
        ## This bit of code depends on having numbered pathways, stored in the pathway_list in order
        elif ctx.triggered_id[:4] == "use_":
            pathway_index = int(ctx.triggered_id[12:])-1
            new_pathway = pathway_list[pathway_index]["module_list"] 

        ## Change the location of a single module in the pathway

        elif ctx.triggered[0]['value'] and ctx.triggered[0]['value'] > 0:

            # Adds the module to the end of the list
            if ctx.triggered_id[:6] == "add_to":
                module_to_add = ctx.triggered_id[18:]
                if module_to_add not in new_pathway:
                    new_pathway.append(module_to_add)

            # Removes the module from the list
            elif ctx.triggered_id[:6] == "remove":
                module_to_remove = ctx.triggered_id[18:]
                if module_to_remove in new_pathway:
                    new_pathway.remove(module_to_remove)
            
            elif ctx.triggered_id[-6:] == "_trash":
                module_to_remove = ctx.triggered_id[:-6]
                new_pathway.remove(module_to_remove)
            
            # Moves the module up one spot in the list
            elif ctx.triggered_id[-8:] == "_move_up":
                module_to_move_up = ctx.triggered_id[:-8]
                module_index = current_pathway.index(module_to_move_up)
                if module_index > 0:
                    start = current_pathway[0:module_index - 1].copy()
                    start.append(module_to_move_up)
                    start.append(current_pathway[module_index - 1])
                    end = current_pathway[module_index + 1:].copy()
                    new_pathway = start + end
            
            # Moves the module down one spot in the list
            elif ctx.triggered_id[-8:] == "_go_down":
                module_to_go_down = ctx.triggered_id[:-8]
                module_index = current_pathway.index(module_to_go_down)
                if module_index < len(current_pathway)-1:
                    start = current_pathway[0:module_index].copy()
                    start.append(current_pathway[module_index + 1])
                    start.append(module_to_go_down)
                    end = current_pathway[module_index + 2:].copy()
                    new_pathway = start + end
        

        
        return new_pathway

## When a user chooses a pathway from the predetermined list, they should change tabs to see that their selection was actually selected:

def add_pathway_chage_tab(app):
    @app.callback(Output('navigation_tabs', 'active_tab'),
                  [Input("use_"+pathway["id"],'n_clicks') for pathway in pathway_list], #these buttons are for users to remove individual modules from their pathway
                prevent_initial_call=True)
    def switch_to_pathway_tab(*args):
        if ctx.triggered_id:
            return "your_learning_pathway_tab"