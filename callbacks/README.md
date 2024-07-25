# Callbacks

This is where the callbacks that update the hidden components.

## Pathway
The component `hidden_pathway` consists of the current ordered list of modules that make up a user's pathway.

- `update_pathway.py` takes input from the "add to my list" and "remove from my list" buttons and updates the pathway. It also controls the re-ordering of the pathway via the up and down buttons and sort button.


## Search Results

The component `hidden_filtered_modules` consists of all of the modules that match the user's search and filtering criteria as entered in the `left_hand_nav_bar`.

- `update_search_results.py` takes the information the user has entered, and returns the matching modules as a list of module ids. 

