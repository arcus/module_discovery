from dash import Dash, html, Input, Output, dcc, ctx, State
from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc
import module_data 


collection_symbols_dict = {"demystifying":"?",
                          "infrastructure_and_technology": "\u2692",
                          "intro_to_data_science":"\u2139",
                          "learn_to_code":"|>",
                          "machine_learning":"\u2699",
                          "statistics":"\u03BC"
}

collection_colors_dict = {"demystifying":"#41B6E6",
                          "infrastructure_and_technology": "#786452",
                          "intro_to_data_science":"#91a01e",
                          "learn_to_code":"#ed1f7f",
                          "machine_learning":"#005587",
                          "statistics":"#41b6e6"
}

collection_names_dict = {"demystifying":"Demystifying",
                          "infrastructure_and_technology": "Infrastructure and Technology",
                          "intro_to_data_science":"Introduction to Data Science",
                          "learn_to_code":"Learn to Code",
                          "machine_learning":"Machine Learning",
                          "statistics":"Statistics"
}


def collections_icons(module_id):
    collections_list = str(module_data.df.loc[module_id,'collection']).replace(" ", "").split(",")
    icons = []
    for collection in collections_list:
        if collection in collection_symbols_dict.keys():            
            icons.append(dbc.Badge(collection_symbols_dict[collection], 
                color=collection_colors_dict[collection], 
                text_color="black",
                id=module_id+collection+"_badge"
                #className="ms-1"
                ))
            icons.append(dbc.Popover(
                dbc.PopoverBody(collection_names_dict[collection]),
                target=module_id+collection+"_badge",
                trigger="click",
                placement="top"
                ),)
    return icons

