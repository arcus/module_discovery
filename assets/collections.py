from dash import Dash, html, Input, Output, dcc, ctx, State
import module_data 


collection_symbols_dict = {"demystifying":"?",
                          "infrastructure_and_technology": "\u2692",
                          "intro_to_data_science":"\u2139",
                          "learn_to_code":"|>",
                          "machine_learning":"\u2699",
                          "statistics":"\u03BC"
}

def collections_icons(module_id):
    collections_list = str(module_data.df.loc[module_id,'collection']).replace(" ", "").split(",")
    icons = []
    for collection in collections_list:
        if collection in collection_symbols_dict.keys():            
            icons.append(collection_symbols_dict[collection])
    return icons

