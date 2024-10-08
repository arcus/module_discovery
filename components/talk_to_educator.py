from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP


talk_to_educator_text = html.Div(children=[
                html.Br(),
                dbc.Container([dcc.Markdown("## Want to talk to a person? \n \n  Arcus Education offers free Educational Consultations to members of the CHOP community. We can help you navigate these resources, build a pathway with you, and connect you to additional synchronous offerings.  \n \n "),
                html.Br(),
                html.A("Use your CHOP log-in to "),
                html.A("book your Educational Consultation", href = "https://outlook.office365.com/owa/calendar/BKG-StandardArcusEducationOfficeHours@chop.edu/bookings/s/T6CE7Ve6Ck-saLar2e1xYw2", target="_blank", style={"color":CHOP.dark_blue}),
                html.A(", or "),
                html.A("check out our full bookings page.", href = "https://outlook.office365.com/book/BKG-StandardArcusEducationOfficeHours@chop.edu/", target="_blank", style={"color":CHOP.dark_blue})
                ])])