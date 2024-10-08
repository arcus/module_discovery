from dash import html, dcc
import dash_bootstrap_components as dbc
from .search_panel import search_panel as search_panel
from assets.collections import collection_symbols_dict, collection_descriptions_dict, collection_names_dict
from assets.levels import level_dictionary
import assets.CHOP_colors as CHOP

def collections_popover():
    popover_body = ""
    for collection in ["demystifying", "infrastructure_and_technology","intro_to_data_science", "learn_to_code", "machine_learning", "statistics"]:
        popover_body += collection_symbols_dict[collection]
        popover_body += " **"
        popover_body += collection_names_dict[collection]
        popover_body += "** "
        popover_body += collection_descriptions_dict[collection]
        popover_body +="\n \n"
    return dbc.Popover(
                dbc.PopoverBody(dcc.Markdown(popover_body)),
            target="collection_info_button",
            trigger="hover",
        )

def level_popover():
    popover_body = ""
    for level in level_dictionary.keys():
        popover_body += "**"+level_dictionary[level]["level_name"]+"**: "
        popover_body += level_dictionary[level]["level_description"]
        popover_body += "\n \n"
    return dbc.Popover(
                dbc.PopoverBody(dcc.Markdown(popover_body)),
            target="level_info_button",
            trigger="hover",
        )

filtering_options= [
                                       
    # GENERAL OPTIONS

    dbc.Button(
    "General Options",
    id="general_options_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
    dbc.Badge("?", id="general_options_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("A **good first module** will give you a good idea of the flavor of these educational resources. These modules are frequently introductions to broader topics and have no prerequisites or coding requirements. \n\n You can also filter for modules that **do not require any hands on coding**, or modules that are **primarily hands on exercises**.")),
            target="general_options_info_button",
            trigger="hover",
        ),
    dbc.Collapse(dcc.Checklist(
           options=[
       {'label': ' Good first module', 'value': 'good_first_module'},
       {'label': ' Doesn\'t require coding', 'value': 'no_coding_required'},
       {'label': ' Hands on exercise', 'value': 'exercise'}
       ],
          value=[],
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
    collections_popover(),
    dbc.Collapse([
    dbc.Col( 
    dcc.RadioItems(
        options=[
        {'label': ' Demystifying '+collection_symbols_dict['demystifying'], 'value': 'demystifying'},
        {'label': ' Infrastructure and Technology '+collection_symbols_dict['infrastructure_and_technology'], 'value': 'infrastructure_and_technology'},
        {'label': ' Introduction to Data Science '+collection_symbols_dict['intro_to_data_science'], 'value': 'intro_to_data_science'},
        {'label': ' Learn to Code '+collection_symbols_dict['learn_to_code'], 'value': 'learn_to_code'},
        {'label': ' Machine Learning '+collection_symbols_dict['machine_learning'], 'value': 'machine_learning'},
        {'label': ' Statistics '+collection_symbols_dict['statistics'], 'value': 'statistics'},
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

    # LEVEL

    dbc.Button(
    "Level",
    id="level_collapse_button", color="dark", outline=True, size="sm", className="me-1"),
        dbc.Badge("?", id="level_info_button", pill=True,  color="light", text_color="dark"),
    level_popover(),
    dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[{'label': " "+level_dictionary[key]["level_description"], 'value': key} for key in level_dictionary.keys()]+[
        {'label': html.A(' Clear selection', style={'color': 'grey'}), 'value': '', },
        ],
        id='level_checklist')
    ],)],
    id='level_collapse_checklist',
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
            trigger="hover",
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
            trigger="hover",
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
            trigger="hover",
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
            trigger="hover",
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
    html.Br(),
    html.Br(),
]#, style={'background-color': CHOP.light_blue_tint[1], "maxHeight": "725px", "overflow": "scroll"}, fluid=True, className="w-100")


left_hand_nav_bar = dbc.Container([
    html.Br(),
    
    ### This is the button that appears when the screen is extra small to allow users to collapse the navigation bar.
    
    dbc.Button("Show/hide search options",id="filtering_collapse_button",color="dark", outline=True, size="sm", style={"background-color":CHOP.dark_blue_tint[2]}, class_name="d-block d-sm-none"),
    html.Br(className="d-block d-sm-none"),
    #html.Br(className="d-block d-sm-none"),

    ## The whole nav bar is collapsible, but the button to do so is only visible on smaller screens
    
    dbc.Collapse([
    dcc.Markdown("Search by keyword or filter modules by what you want to learn about:"),
    
    # SEARCH DOESN'T YET HAVE A SUBMIT BUTTON

    search_panel,
    html.Br(),
    dbc.Button("Clear all selections", id="clear_all_selections",color="dark", outline=True, size="sm", className="me-1", style={"background-color":CHOP.dark_blue_tint[2]}),
    html.Br(),
    html.Br(),]
    + filtering_options,
        id='filtering_collapse',
        is_open=True,
        ),
    
    ## This button is hidden unless the menu is collapsed and the window is big
    dbc.Button("Show search options",id="filtering_expand_button",color="dark", outline=True, size="sm", style={"background-color":CHOP.dark_blue_tint[2]}, class_name="d-none", )
])