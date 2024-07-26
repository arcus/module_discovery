# Components

## Visible Components

There is a component in this directory corresponding to each of the five tabs, and a sixth for the app's title.

## Hidden Components

There are hidden Components which must be loaded into the page in order for callbacks to work, but which are not displayed to users. Each is set to `style= {'display': 'none'}` for use, but can be changed to `style= {'display': 'block'}` to display for development and debugging.

- `hidden_filtered_modules.py` contains a list of modules that meet the current selection criteria as defined in the left_hand_nav_bar.
- `hidden_pathway.py` contains the ordered list of modules that the user has selected and ordered as their pathway.



