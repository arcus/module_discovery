from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


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
                dbc.Container([dcc.Markdown("## Learn more about..."),
                html.Br(),
                dcc.Markdown(modules_text),
                html.Br(),
                dcc.Markdown(GitHub_link),
                html.Br()
                ])])
# \n \n #### The DART Program \n \n \n \n  #### How this webpage was built \n \n #### The knowledge graph of the modules. "