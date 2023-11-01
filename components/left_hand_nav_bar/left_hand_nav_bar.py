from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
from .search_panel import search_panel as search_panel

left_hand_nav_bar = dbc.Col([dcc.Markdown("Search by keyword or filter modules by what you want to learn about:"),
    
    # SEARCH DOESN'T YET HAVE A SUBMIT BUTTON

    search_panel,
    html.Br(),
    dbc.Button("Clear all selections", id="clear_all_selections",color="dark", outline=True, size="sm", className="me-1"),
    html.Br(),
    html.Br(),
    # GENERAL OPTIONS

    dbc.Button(
    "General Options",
    id="general_options_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="general_options_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("A **good first modules** will give you a good idea of the flavor of these educational resources. These modules are frequently introductions to broader topics and have no prerequisites or coding requirements. \n\n You can also filter for modules that do not require any hands on coding, or modules that are primarily hands on exercises.")),
            target="general_options_info_button",
            trigger="click",
        ),
    dbc.Collapse(dcc.Checklist(
           options=[
       {'label': ' Good first module', 'value': 'good_first_module'},
       {'label': ' Doesn\'t require coding', 'value': 'no_coding_required'},
       {'label': ' Hands on exercise', 'value': 'exercise'}
       ],
          value=['good_first_module'],
          id='general_options_checklist'),
          id='general_options_collapse_checklist',
    is_open=True),

    html.Br(),
    html.Br(),
    
    # COLLECTION

    dbc.Button(
        "Collection",
        id="collection_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="collection_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("**Demystifying** modules focus on giving an overview of a topic and are often have a special focus on reducing anxiety about a potentially daunting topic or tool, and cutting through the hype to helping novices to determine whether or not this is something they should learn to do. \n \n **Infrastructure and Technology** modules focus on software or tools, especially setup and systems. Things like how to install software, or understanding what software and/or languages to use for what tasks. \n \n **Introduction to Data Science** modules teach skills for learners new to data science, including how to troubleshoot and best practices for reproducible methods. \n \n **Learn to Code** modules are primarily focused on teaching coding skills \n \n **Machine Learning** includes all modules about machine learning and AI. \n \n **Statistics** includes both applied data analysis (e.g. here's how to do this test in R) and a more theoretical understanding of statistics and the underlying math ")),
            target="collection_info_button",
            trigger="click",
        ),
    dbc.Collapse([
    dbc.Col( 
    dcc.RadioItems(
        options=[
        {'label': ' Demystifying', 'value': 'demystifying'},
        {'label': ' Infrastructure and Technology', 'value': 'infrastructure_and_technology'},
        {'label': ' Introduction to Data Science', 'value': 'intro_to_data_science'},
        {'label': ' Learn to Code', 'value': 'learn_to_code'},
        {'label': ' Machine Learning', 'value': 'machine_learning'},
        {'label': ' Statistics', 'value': 'statistics'},
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', }, ## This empty value helps with the callbacks
        ],
        id='collection_checklist'
        )
        ),],
    id='collection_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    html.Br(),


    # CODING LANGUAGE

    dbc.Button(
        "Coding Language",
        id="coding_language_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="coding_language_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("Some modules either use or refer to more than one coding language. Modules will be shown when any one of their coding languages is selected.")),
            target="coding_language_info_button",
            trigger="click",
        ),
    dbc.Collapse([
    dbc.Col( 
    dcc.RadioItems(
        options=[
        {'label': ' Bash', 'value': 'bash'},
        {'label': ' Python', 'value': 'python'},
        {'label': ' R', 'value': 'r'},
        {'label': ' SQL', 'value': 'sql'},
        {'label': ' Git', 'value': 'git'},
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', }, ## This empty value helps with the callbacks
        ],
        id='coding_language_checklist'
        )
        ),],
    id='coding_language_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    html.Br(),

    # CODING LEVEL

    dbc.Button(
    "Coding Level",
    id="coding_level_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
        dbc.Badge("?", id="coding_level_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("**Getting Started:** These modules are primarily about getting a platform set up. \n\n **Basic:** These modules require little or no previous exposure to coding. \n\n **Intermediate** These modules require some previous coding exposure. \n\n **Advanced:** These modules focus on particularly difficult or specialized tasks.")),
            target="coding_level_info_button",
            trigger="click",
        ),
        dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[
        {'label': ' Get started', 'value': 'getting_started'},
        {'label': ' Basic', 'value': 'basic'},
        {'label': ' Intermediate', 'value': 'intermediate'},
        {'label': ' Advanced', 'value': 'advanced'},
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', },
        ],
        id='coding_level_checklist')
    ],)],
    id='coding_level_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    html.Br(),

    # DATA TASK

    dbc.Button(
    "Data Task",
    id="data_task_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="data_task_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("**Data Visualization:** Creating representations of data such as plots, graphs, maps, etc.\n\n **Data Management:** Organizing and storing data, including database structures, data sharing, cloud vs. local storage, and metadata. \n\n **Data Wrangling:** Data processing steps in preparation for analysis and visualization, including cleaning, transforming, and reshaping data.\n\n **Data Analysis:** Identifying and quantifying patterns in the data, including exploratory analysis, descriptive statistics, and more formal modeling.")),
            target="data_task_info_button",
            trigger="click",
        ),
    dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[
        {'label': ' Data Visualization', 'value': 'data_visualization'},
        {'label': ' Data Management', 'value': 'data_management'},
        {'label': ' Data Wrangling', 'value': 'data_wrangling'},
        {'label': ' Data Analysis', 'value': 'data_analysis'},
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', },
        ],
        id='data_task_checklist')
    ],)],
    id='data_task_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    html.Br(),

    # DATA DOMAIN

    dbc.Button(
    "Data Domain",
    id="data_domain_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="data_domain_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("Some modules focus on particular types of data. These modules might introduce be focused on getting learners used to working with a particular type of data, or they might be focused on other tasks but use examples from a specific domain like geospatial (location) data, Electronic Health Records, etc.")),
            target="data_domain_info_button",
            trigger="click",
        ),
        dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[
        {'label': ' Omics', 'value': 'omics'},
        {'label': ' Electronic Health Records', 'value': 'ehr'},
        {'label': ' Geospatial Data', 'value': 'geospatial'},
        {'label': ' Text', 'value': 'text'},
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', },
        ],
        id='data_domain_checklist')
    ],)],
    id='data_domain_collapse_checklist',
    is_open=False,
    ),
], xs = 12, lg = 4, xl = 2, style={'background-color': '#ADD8E6'})

