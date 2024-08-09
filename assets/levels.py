from network_analysis.required_expertise_times import required_expertise_times

level_dictionary = {0: {"level_name": "Intro",
                        "level_description": "No prerequisites",
                        },
                    1: {"level_name": "Level 1",
                        "level_description": "Less than 2 hours of prerequisites"
                        },
                    2: {"level_name": "Level 2",
                        "level_description": "2 to 4 hours of prerequisites"
                        },
                    3: {"level_name": "Level 3",
                        "level_description": "4 to 6 hours of prerequisites"
                        },
                    4: {"level_name": "Level 4",
                        "level_description": "6 to 8 hours of prerequisites"
                        },
                    5: {"level_name": "Level 5",
                        "level_description": "More than 8 hours of prerequisites"
                        },
                    }

def module_level(module_id):
    return (required_expertise_times(module_id)-1)//120 + 1


