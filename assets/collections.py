import dash_bootstrap_components as dbc
import module_data 
import assets.CHOP_colors as CHOP

collection_descriptions_dict = {
                            "demystifying":"modules focus on giving an overview of a topic and are often have a special focus on reducing anxiety about a potentially daunting topic or tool, and cutting through the hype to helping novices to determine whether or not this is something they should learn to do.",
                            "infrastructure_and_technology": "modules focus on software or tools, especially setup and systems. Things like how to install software, or understanding what software and/or languages to use for what tasks.",
                            "intro_to_data_science":"modules teach skills for learners new to data science, including how to troubleshoot and best practices for reproducible methods.",
                            "learn_to_code":"modules are primarily focused on teaching coding skills.",
                            "machine_learning":"includes all modules about machine learning and AI.",
                            "statistics":"includes both applied data analysis (e.g. here's how to do this test in R) and a more theoretical understanding of statistics and the underlying math."
}

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

