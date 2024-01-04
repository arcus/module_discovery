import networkx as nx
import pandas as pd
import module_data

from .poset_processing import poset, hasse

# poset = poset_processing.poset
# hasse = poset_processing.hasse

def prereqs_precede(pathway, module_id):
    if set(hasse.predecessors(module_id)).issubset(set(pathway[0:pathway.index(module_id)])):
        return True
    else:
        return False

def prereqs_follow(pathway, module_id):
    all_prereqs = set(poset.predecessors(module_id))
    if all_prereqs.intersection(set(pathway[pathway.index(module_id)])) != set():
        return True
    else:
        return False

def prereqs_absent(pathway, module_id):
    immediate_prereqs = set(hasse.predecessors(module_id)).issubset(set(pathway[0:pathway.index(module_id)]))
    if immediate_prereqs.issubset(set(pathway)):
        return False
    else:
        return True
