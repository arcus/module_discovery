from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 




def modal_my_module_list(hidden_pathway):
    # Create the copyable text version of the pathway
    copyable_markdown = ["["+module_data.df.loc[module,"title"]+"](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+module+"/"+module+".md#1) "+ module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes \n \n" for module in hidden_pathway]

    return dbc.Modal(
                    dbc.ModalBody(children=[
                        dcc.Markdown("**Copy these links and paste them into a document or email for future reference:**"),
                        dcc.Markdown([' '.join(copyable_markdown)], id="list_for_clipboard")
                        ], 
                        style={'width':'475px'}),
                    id="copy_my_modules_modal",
                    is_open=False
                    #trigger="click",
                    #style={"max-width":"500px"},                               
                )

def modal_copy_my_module_list(app):
    @app.callback(
        Output("copy_my_modules_modal", "is_open"),
        [Input("copy_my_modules", "n_clicks")],
        [State("copy_my_modules_modal", "is_open")],
        prevent_initial_call=True
    )
    def toggle_modal(n1, is_open):
        if n1:
            return not is_open
        return is_open