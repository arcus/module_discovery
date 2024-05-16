import networkx as nx
import pandas as pd
import module_data

df = module_data.df

from .poset_processing import poset, hasse

def required_expertise_times(module_id):
    pre_req_time = 0
    for module in set(poset.reverse().neighbors(module_id)):
        pre_req_time += int(df.loc[module, 'estimated_time_in_minutes'])
    return pre_req_time
