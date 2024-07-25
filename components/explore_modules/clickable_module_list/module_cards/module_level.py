from dash import dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import module_data 
from network_analysis.required_expertise_times import required_expertise_times


def module_level_icon(module_id):
  icons = []          
  icons.append(dbc.Badge(["Level "+ str((required_expertise_times(module_id)-1)//120+1)], 
                style = {"color":CHOP.black}, #badge text color
                color = CHOP.white,
                id=module_id+"_level_badge"
                #className="ms-1"
                ))
  icons.append(dbc.Popover(
              dbc.PopoverBody(dcc.Markdown(str(required_expertise_times(module_id))+" mins of prerequisites.")),
              target=module_id+"_level_badge",
              trigger="hover",
              placement="top"
              ))
  return icons
