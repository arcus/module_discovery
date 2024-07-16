from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import assets.CHOP_colors as CHOP

# structure = {"name" : "Pathway Name",
#              "id" : "pathway_id",
#              "module_list": [module_1, module_2],
#              "comment" : "A short description",
#              "description" : "Text Description of the pathway."
#              }

pathway_1 = {"name":"Getting started with biomedical data science",
             "id" : "pathway_1",
             "module_list": ["reproducibility"
                            ,"how_to_troubleshoot"
                            ,"learning_to_learn"
                            ,"demystifying_geospatial_data"
                            ,"omics_orientation"
                            ,"demystifying_sql"
                            ,"demystifying_machine_learning"
                            ,"demystifying_large_language_models"
                            ,"directories_and_file_paths"
                            ,"demystifying_command_line"
                            ,"demystifying_python"
                            ,"demystifying_regular_expressions"
                            ,"citizen_science"
                            ,"demystifying_containers"
                            ,"git_intro"
                            ,"data_management_basics"
                            ],
                "comment": "This popular pathway is designed with new data scientists in mind. You might be early in your research career, or you might have years of experience but just trying out data science techniques for the first time.",
                "description": "This popular pathway is designed with new data scientists in mind. You might be early in your research career, or you might have years of experience but just trying out data science techniques for the first time. \n \n This pathway provides a practical overview of what skills you’ll need to do reproducible, rigorous data science research in biomedical and health fields. We’ll touch on a lot of the hot topic techniques you may have heard about (what exactly are large language models?) and help you cut through the hype to figure out whether those are tools you want to invest time in learning. \n \n If you’re at the point where you know you’re interested in biomedical data science but aren’t sure where to start, this is the pathway for you!"               
                }

pathway_2 = {"name" : "Focus on omics",
             "id" : "pathway_2",
            "module_list": ["reproducibility"
                            ,"how_to_troubleshoot"
                            ,"directories_and_file_paths"
                            ,"data_management_basics"
                            ,"demystifying_command_line"
                            ,"bash_command_line_101"
                            ,"bash_command_line_102"
                            ,"bash_conditionals_loops"
                            ,"bash_103_combining_commands"
                            ,"bash_scripts"
                            ,"git_intro"
                            ,"git_setup_mac_and_linux"
                            ,"git_setup_windows"
                            ,"git_creation_and_tracking"
                            ,"git_history_of_project"
                            ,"omics_orientation"
                            ,"genomics_setup"
                            ,"genomics_quality_control"
                            ,"demystifying_containers"
                            ,"docker_101"
                            ],
            "comment": "This pathway is for people who want to start working with molecular data.",
            "description" : "This pathway is for people who want to start working with molecular data. It will bring you up to speed in the computing tools you’ll need to get started with genomics research, including using the command line, version control, and containerization. No computing background is assumed; we’ll start from the basics! Note that if you’re already actively working on genomics analysis, this material will likely be too basic for you."
            }

pathway_3 = {"name" : "Big data, big questions",
             "id" : "pathway_3",
             "module_list": ["reproducibility"
                            ,"data_management_basics"
                            ,"demystifying_sql"
                            ,"database_normalization"
                            ,"sql_basics"
                            ,"sql_intermediate"
                            ,"sql_joins"
                            ,"demystifying_geospatial_data"
                            ,"geocode_lat_long"
                            ,"elements_of_maps"
                            ,"demystifying_regular_expressions"
                            ,"regular_expressions_basics"
                            ,"regular_expressions_groups"
                            ,"regular_expressions_boundaries_anchors"
                            ,"regular_expressions_lookaheads"
                            ,"demystifying_large_language_models"
                            ,"demystifying_machine_learning"
                            ,"citizen_science"
                            ],
            "comment":"This pathway is for people primarily interested in analysis of the rich, complex data in the electronic health record (EHR) and other big databases.",
             "description" : "This pathway is for people primarily interested in analysis of the rich, complex data in the electronic health record (EHR) and other big databases. If you’re interested in social determinants of health, retrospective analysis of clinical data, or connecting data from multiple sources, this is the pathway for you! This pathway includes a gentle but thorough introduction to SQL, the programming language you’ll need to be able to work with databases, as well as information about working with geospatial data, text data, and more."
             }

pathway_4 = {"name" : "Analysis in R",
             "id" : "pathway_4",
             "module_list": ["reproducibility"
                            ,"tidy_data"
                            ,"how_to_troubleshoot"
                            ,"r_basics_introduction"
                            ,"r_basics_visualize_data"
                            ,"r_basics_transform_data"
                            ,"directories_and_file_paths"
                            ,"r_basics_practice"
                            ,"r_reshape_long_wide"
                            ,"r_missing_values"
                            ,"r_summary_stats"
                            ,"data_visualization_in_open_source_software"
                            ,"data_visualization_in_ggplot2"
                            ,"intro_to_nhst"
                            ,"statistical_tests"
                            ,"r_practice"
                            ,"demystifying_machine_learning"
                            ,"bias_variance_tradeoff"
                            ],
            "comment" : "This pathway is focuses on the skills and techniques you’ll need to leverage the popular statistical programming language R.",
             "description" : "This pathway is focuses on the skills and techniques you’ll need to leverage the popular statistical programming language R. We’ll start from zero and walk you through everything you need to start analyzing data in R, including lots of opportunities for hands-on practice. \n \n This is designed to be welcoming to folks with no coding experience, so if R will be your first programming language you’ll fit right in!"
             }

pathway_5 = {"name" : "Analysis in Python",
             "id" : "pathway_5",
             "module_list": ["reproducibility"
                            ,"tidy_data"
                            ,"how_to_troubleshoot"
                            ,"learning_to_learn"
                            ,"directories_and_file_paths"
                            ,"demystifying_command_line"
                            ,"demystifying_python"
                            ,"python_basics_variables_functions_methods"
                            ,"python_basics_lists_dictionaries"
                            ,"python_basics_loops_conditionals"
                            ,"python_basics_exercise"
                            ,"pandas_transform"
                            ,"data_visualization_in_open_source_software"
                            ,"data_visualization_in_seaborn"
                            ,"intro_to_nhst"
                            ,"statistical_tests"
                            ,"python_practice"
                            ,"demystifying_machine_learning"
                            ,"bias_variance_tradeoff"
                            ],
            "comment" : "If you’re looking to learn Python to do things like clean and analyze data, and create data visualizations, this pathway is for you.",
             "description" : "Python is a powerful open source programming language with tons of great tools for data science. If you’re looking to learn Python to do things like clean and analyze data, and create data visualizations, this pathway is for you. We’ll start from zero and walk you through everything you need to start analyzing data in Python, including lots of opportunities for hands-on practice. \n \n This is designed to be welcoming to folks with no coding experience, so if Python will be your first programming language you’ll fit right in!"
             }

pathway_list = [pathway_1, pathway_2, pathway_3, pathway_4, pathway_5]