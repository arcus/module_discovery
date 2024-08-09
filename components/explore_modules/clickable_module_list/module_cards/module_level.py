from dash import dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
from assets.levels import level_dictionary, module_level
from network_analysis.required_expertise_times import required_expertise_times


def module_level_icon(module_id):
  icons = []          
  icons.append(dbc.Badge(level_dictionary[module_level(module_id)]["level_name"], 
                style = {"color":CHOP.black}, #badge text color
                color = CHOP.white,
                id=module_id+"_level_badge"
                #className="ms-1"
                ))
  icons.append(dbc.Popover(
              dbc.PopoverBody(dcc.Markdown(level_dictionary[module_level(module_id)]["level_description"])),
              target=module_id+"_level_badge",
              trigger="hover",
              placement="top"
              ))
  return icons
