from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import assets.CHOP_colors as CHOP


collection_symbols_dict = {"demystifying":"?",
                          "infrastructure_and_technology": "\u2692",
                          "intro_to_data_science":"\u2139",
                          "learn_to_code":"|>",
                          "machine_learning":"\u2699",
                          "statistics":"\u03BC"
}

collection_colors_dict = {"demystifying":CHOP.pink,
                          "infrastructure_and_technology": CHOP.brown,
                          "intro_to_data_science": CHOP.green,
                          "learn_to_code": CHOP.light_blue,
                          "machine_learning":CHOP.dark_blue,
                          "statistics": CHOP.light_blue
}

collection_text_colors_dict = {"demystifying":CHOP.white,
                          "infrastructure_and_technology": CHOP.white,
                          "intro_to_data_science":CHOP.white,
                          "learn_to_code": CHOP.black,
                          "machine_learning": CHOP.white,
                          "statistics": CHOP.black
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
                style = {"color":collection_text_colors_dict[collection]}, #badge text color
                color=collection_colors_dict[collection], #badge background color
                id=module_id+collection+"_badge"
                #className="ms-1"
                ))
            icons.append(dbc.Popover(
                dbc.PopoverBody(collection_names_dict[collection]),
                target=module_id+collection+"_badge",
                trigger="hover",
                placement="top"
                ),)
    return icons

