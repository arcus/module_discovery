from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary
from network_analysis.poset_processing import poset, hasse 

### General button structure for all rows:
def general_pathway_buttons(module):
    module_name_and_buttons = [dbc.Col([
            dbc.ButtonGroup([
            dbc.Button('\U00002191', color="light", n_clicks=0,id=module+"_move_up"),
            dbc.Button('\U00002193', color="light", n_clicks=0, id=module+"_go_down"),
            dbc.Button(module_data.df.loc[module,"title"], color="light", n_clicks=0, id=module+"_nutbot"),
        ]
    )], width=8),
    dbc.Col([dbc.Button("x", color="light", n_clicks=0, id=module+"_trash")],width=1), 
    dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)]
    return module_name_and_buttons


### If all of the immediate prerequisites to a module precede it in the pathway, its appears like this:
def prereqs_precede_row(hidden_pathway, module):
    build_buttons = [dbc.Col([],width=1)]+general_pathway_buttons(module)
    button_group = dbc.Row(build_buttons, justify="between")
    return button_group


### If any module that precedes it in the poset appears after it in the pathway, the modules appears like this:
def prereqs_follow_row(hidden_pathway, module):
    ## Create a list of the "offending" modules that belong before this one
    following_prereqs = list(set(poset.predecessors(module)).intersection(set(hidden_pathway[hidden_pathway.index(module):])))
    my_markdown_list="\n "
    for mod in following_prereqs:
        my_markdown_list = my_markdown_list + "\n - "+module_data.df.loc[mod,"title"]

    ## Create a popover badge
    badge = [dbc.Col([
        dbc.Badge("\U000023F9", color="danger", className="me-1", id="order_message_"+module),
                dbc.Popover(
                    dbc.PopoverBody([dcc.Markdown("**"+module_data.df.loc[module, "title"]+"** assumes knowledge you will learn later in the pathway. You can use the up/down buttons to reorder this module, or use the sort button to make sure the following modules precede it in the pathway:"+my_markdown_list)]),
                    target="order_message_"+module,
                    placement="left",
                    trigger="hover",
                    )],width=1)]
    build_buttons = badge+general_pathway_buttons(module)
    button_group = dbc.Row(build_buttons, justify="betweeen")
    return button_group

### Modules that are missing immediate prerequisites (i.e. the learner will be bringing prior knowledge to the module not in the pathway) look like this:
def prior_knowledge_required_row(hidden_pathway,module):
    # Create a list of presumed prior knowledge modules:
    following_prereqs = list(set(hasse.predecessors(module)).difference(set(hidden_pathway)))
    my_markdown_list="\n "
    for mod in following_prereqs:
        my_markdown_list = my_markdown_list + "\n - "+module_data.df.loc[mod,"title"]

    ## Create a popover badge
    badge = [dbc.Col([dbc.Badge("\U000023F8", color="warning", className="me-1", id="prereqs_precede_"+module),
            dbc.Popover(
                dbc.PopoverBody(dcc.Markdown("**"+module_data.df.loc[module, "title"]+"** depends on some prior knowledge not in your pathway. If you already have this knowledge, you are good to go! If not, consider adding these modules to your pathway:"+my_markdown_list)),
                target="prereqs_precede_"+module,
                placement="left",
                trigger="hover",
                )],width=1)]

    build_buttons = badge+general_pathway_buttons(module)
    button_group = dbc.Row(build_buttons, justify="betweeen")
    return button_group