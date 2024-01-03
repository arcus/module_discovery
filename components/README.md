# Visible Components

Each visible app Component has its own short README with information about its functional role.

## Layout

The way that the Components are assembled into the app is defined by `app.layout` in `app.py`. Depending on the size of the browser window the app will appear with one of the following layouts 

TODO: add annotated screenshots

Responsive layouts: 

![XXL layout](image/here)

![MD layout](image/here)

![SM layout](image/here)

![XS layout](image/here)


## Hidden Components

There are hidden Components which must be loaded into the page in order for callbacks to work, but which are not displayed to users. Each is set to `style= {'display': 'none'}` for use, but can be changed to `style= {'display': 'block'}` to display for development and debugging.

- `hidden_active_module.py` contains the current active module, which can be selected by a user from any of the buttons containing a module's name, or by clicking on a node in the visualization_panel component.
- `hidden_filtered_modules.py` contains a list of modules that meet the current selection criteria as defined in the left_hand_nav_bar.
- `hidden_pathway.py` contains the ordered list of modules that the user has selected and ordered as their pathway.



