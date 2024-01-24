from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary


### If all of the immediate prerequisites to a module precede it in the pathway, its appears like this:
def prereqs_precede_row(hidden_pathway, module):
    button_group = dbc.Row([dbc.Col([
            dbc.Badge("\U000023F5", color="success", pill=True,  id="order_message_"+module),
            dbc.Popover(
                dbc.PopoverBody(dcc.Markdown("This pathway will teach you what you need to know for **"+module_data.df.loc[module, "title"]+"** before you get to it.")),
                target="order_message_"+module,
                placement="left",
                trigger="hover",
                )],width=1),
            dbc.Col([
            dbc.ButtonGroup([
            dbc.Button('\U00002191', color="light", n_clicks=0,id=module+"_move_up"),
            dbc.Button('\U00002193', color="light", n_clicks=0, id=module+"_go_down"),
            dbc.Button(module_data.df.loc[module,"title"], color="light", n_clicks=0, id=module+"_nutbot"),
        ]
    )], width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
    return button_group


### If any module that precedes it in the poset appears after it in the pathway, the modules appears like this:
def prereqs_follow_row(hidden_pathway, module):
    button_group = dbc.Row([dbc.Col([
        dbc.Badge("\U000023F9", color="danger", className="me-1", id="order_message_"+module),
                dbc.Popover(
                    dbc.PopoverBody(dcc.Markdown("**"+module_data.df.loc[module, "title"]+"** assumes knowledge you will learn later in the pathway. You can use the up/down buttons to reorder this module, or use the sort button to make sure the following modules precede it in the pathway:")),
                    target="order_message_"+module,
                    placement="left",
                    trigger="hover",
                    )],width=1),
        dbc.Col([
        dbc.ButtonGroup([
                dbc.Button('\U00002191', color="light", n_clicks=0,id=module+"_move_up"),
                dbc.Button('\U00002193', color="light", n_clicks=0, id=module+"_go_down"),
                dbc.Button(module_data.df.loc[module,"title"], color="light", n_clicks=0, id=module+"_nutbot"),
            ]
        )], width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
    return button_group

### Modules that are missing immediate prerequisites (i.e. the learner will be bringing prior knowledge to the module not in the pathway) look like this:
def prior_knowledge_required_row(hidden_pathway,module):
    button_group = dbc.Row([dbc.Col([ 
        dbc.Badge("\U000023F8", color="warning", className="me-1", id="prereqs_precede_"+module),
            dbc.Popover(
                dbc.PopoverBody(dcc.Markdown("**"+module_data.df.loc[module, "title"]+"** depends on some prior knowledge not in your pathway. If you already have this knowledge, you are good to go! If not, consider adding these modules to your pathway:")),
                target="prereqs_precede_"+module,
                placement="left",
                trigger="hover",
                )],width=1),
        dbc.Col([
        dbc.ButtonGroup([                               
            dbc.Button('\U00002191', color="light", n_clicks=0,id=module+"_move_up"),
            dbc.Button('\U00002193', color="light", n_clicks=0, id=module+"_go_down"),
            dbc.Button(module_data.df.loc[module,"title"], color="light", n_clicks=0, id=module+"_nutbot"),
        ]
    )], width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
    return button_group