# Callbacks

This is where inter-component callbacks live, particularly the callbacks that update the hidden components.

## Active Node
The component `hidden_active_node` contains the module id for the currently active node.

- `update_active_node.py` takes input from different components and updates the `hidden_active_node`
- `render_active_node.py` updates the main visualization of the active node, `components/visualization_panels/active_module_visualization.py`

## Pathway
The component `hidden_pathway` consists of the current ordered list of modules that make up a user's pathway.

- `update_pathway.py` takes input from the "add to my list" and "remove from my list" buttons and updates the pathway. It also controls the re-ordering of the pathway via the up and down buttons and sort button.
- `render_pathway.py` updates the main pathway visualization, `components/visualization_panels/pathway_visualization.py`

## Search Results

The component `hidden_filtered_modules` consists of all of the modules that match the user's search and filtering criteria as entered in the `left_hand_nav_bar`.

- `update_search_results.py` takes the information the user has entered, and returns the matching modules as a list of module ids. 
- `render_search_results.py` updates the search results visualization `components/visualization_panels/search_results_visualization.py`

## Combined Visualization

- `render_combined_visualization.py` updates `components/visualization_panels/combined_visualization_panel.py` using information from the Components `hidden_active_node`, `hidden_pathway`, and `hidden_filtered_modules`.