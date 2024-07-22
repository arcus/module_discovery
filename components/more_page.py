from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
from components.visualization_panels.knowledge_graph import combined_visualization_panel

modules_text = '''
### The Modules
The educational modules linked to on this webpage were built using [LiaScript](https://liascript.github.io) as part of the [Data and Analytics for Research Training (DART)](https://arcus.github.io/education_modules/).

The DART program provides free, open source educational materials to help working biomedical researchers gain the data science knowledge to expand and improve upon the work they are already doing.The program consists of instructional modules which teach data science and related skills to researchers, in alignment with the NIH emphasis on improving research reproducibility, transparency, and rigor.

The [educational materials created for the DART program are publicly available on GitHub](https://github.com/arcus/education_modules) for you to use, re-use, and re-mix under CC-BY-SA-4.0 license.
'''

GitHub_link = '''
### How this Webpage was Built 
This webpage is an open source project, built as a [Dash Application](https://dash.plotly.com). See the [source code on GitHub](https://github.com/arcus/module_discovery?tab=readme-ov-file#module-discovery-app).

Much of the current design was influenced by University of Michigan School of Information students.

The inner workings of this website depend on the rich metadata we keep on the educational modules, including the [knowledge graph of how all modules are interrelated](show the graph!!!).
'''
more_text = html.Div(children=[
                html.Br(),
                dbc.Container([
                html.H2("Learn more about..."),
                html.Br(),
                html.H3("The Modules"),
                html.A("The educational modules linked to on this webpage were built using "),
                html.A("LiaScript", href="https://liascript.github.io", target="_blank", style={"color":CHOP.dark_blue}),
                html.A(" as part of the "),
                html.A("Data and Analytics for Research Training (DART)", href="https://arcus.github.io/education_modules/", target="_blank", style={"color":CHOP.dark_blue}),
                html.A("."),
                html.Br(),
                html.Br(),
                html.A("The DART program provides free, open source educational materials to help working biomedical researchers gain the data science knowledge to expand and improve upon the work they are already doing.The program consists of instructional modules which teach data science and related skills to researchers, in alignment with the NIH emphasis on improving research reproducibility, transparency, and rigor."),
                html.Br(),
                html.Br(),
                html.A("The educational materials created for the DART program are publicly available on GitHub", href="https://github.com/arcus/education_modules", target="_blank", style={"color":CHOP.dark_blue}),
                html.A(" for you to use, re-use, and re-mix under CC-BY-SA-4.0 license."),
                html.Br(),
                html.Br(),
                html.H3("This Webpage"),
                html.A("This webpage is an open source project, and you can see the "),
                html.A("source code on GitHub.", href="https://github.com/arcus/module_discovery?tab=readme-ov-file#module-discovery-app", target="_blank", style={"color":CHOP.dark_blue}),
                html.Br(),
                html.Br(),
                html.A("The inner workings of this website depend on the rich metadata we keep on the educational modules, including the "),
                dbc.Button("knowledge graph", id="knowledge_graph", n_clicks=0, style={"background-color":CHOP.light_blue_tint[2], "color":CHOP.dark_blue}),
                html.A(" of how all modules are interrelated."),
                dbc.Modal([
                    dbc.ModalHeader(dcc.Markdown("### Knowledge graph")),
                    dbc.ModalBody([dcc.Markdown("Zoom in and move modules around to see how they are connected to each other. "), combined_visualization_panel])],
                            id="network_graph_modal",
                            size="lg",
                            scrollable=False,
                            is_open=False,),
                ])])

def show_network_graph(app):
    @app.callback(
        Output("network_graph_modal", "is_open"),
        Input("knowledge_graph", "n_clicks"),
        State("network_graph_modal", "is_open"),
        prevent_initial_call=True
    )
    def toggle_modal(n1, is_open):
        if n1:
            return not is_open
        return is_open