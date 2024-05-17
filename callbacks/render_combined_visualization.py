### Eventually this will be folded into a single callback that incorporates filtered_modules, active_node, and then spits out the approriate stylesheet for the visualization panel.

from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from stylesheets import default_stylesheet, pathway_stylesheet
import module_data


def turn_nodes_on_off(app):
    @app.callback(Output('module_visualization', 'stylesheet'),
                Input('hidden_filtered_modules_list','children'),
                Input('hidden_active_module', 'children'),
                Input('hidden_pathway', 'children'),
                Input('visualization_checklist', 'value'),
                Input('visualization_titles_checklist', 'value'), 
                )
    def update_stylesheet(filtered_module_list,active_node,pathway,visualization_checklist, visualization_titles_checklist):
        ## Edges need to be restyled each time
        new_stylesheet = [ {'selector': 'edge', 'style': default_stylesheet.neutral_edge_styling}]
        ## Modules need to be restyled each time. These styles stack on top of the default style for nodes:
        new_stylesheet +=[{'selector': 'node',
                                'style': default_stylesheet.unselected_styling
                                    }]
        for module_id in module_data.df.index:
            selector = str('[id *= "')+str(module_id)+str('" ]')
                  
            if module_id in pathway and "show_pathway" in visualization_checklist:
                new_stylesheet +=[{'selector': selector,
                                'style': pathway_stylesheet.pathway_node_styling
                                    }]
            if module_id in pathway and "show_pathway_titles" in visualization_titles_checklist:
                new_stylesheet +=[{'selector':selector,
                                'style':{'label': 'data(title)',
                                "font-size": "9px",
                                "text-wrap": "wrap",
                                "text-max-width": 50,}}]
            
            if module_id in filtered_module_list and "show_search_results" in visualization_checklist:
                new_stylesheet += [{'selector': selector,
                                'style': default_stylesheet.selected_styling
                                    }]
            if module_id in filtered_module_list and "show_search_results_titles" in visualization_titles_checklist:
                new_stylesheet +=[{'selector':selector,
                                'style':{'label': 'data(title)',
                                "font-size": "9px",
                                "text-wrap": "wrap",
                                "text-max-width": 50,}}]

            if module_id == active_node:
                new_stylesheet +=[{'selector': selector, 'style': default_stylesheet.active_node_styling}]        
      
        return new_stylesheet

