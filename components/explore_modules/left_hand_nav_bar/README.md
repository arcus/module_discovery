The Left Hand Navigation Bar is how users can search or sort through the modules. User interactions in the Left Hand Navigation Bar update the list of `hidden_filtered_modules` via the callbacks in `callbacks/update_search_results.py`.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Left_Nav_Bar_Closed.png?raw=true" alt="Left Hand Navigation Bar in default state." height="400px"/> 

The file `left_hand_nav_bar` defines the section and options. The categories Level and Collection pull in definitions from `/assets/levels` and `/assests/collections` respectively, but most of the sections are hard coded into this file, including popver text explaining each section's options.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Left_Nav_Bar_Info_Popover.png?raw=true" alt="Information about the Data Task category is available via a popover from the question mark to the right of the Data Task button." height="300px"/>


Internal callbacks in `left_hand_nav_bar_callbacks.py` allow users to expand and collapse sections of the navigation bar by clicking on the section name, i.e. `Collection`.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Left_Nav_Bar_Exapnd.png?raw=true" alt="Left Hand Navigation Bar with Collection and Level sections expanded." height="300px"/>

The text entry box at the top is stored in `search_panel`:

<img src="https://github.com/arcus/module_discovery/blob/main/media/Left_Nav_Bar_Search.png?raw=true" alt="Search bar at the top of the Left Hand Navigation Bar." width="200px"/>

## Making changes to the Left Hand Navigation Bar

The selections in the navigation bar are used to update the search results. If a change is made to the navigation bar options, that change needs to be updated in several places in order to fully work:

1. Add new metadata category or metadata options to the layout in `left_hand_nav_bar`
2.  If new metadata category is added, there are several callbacks that need updating:
    - `left_hand_nav_bar_callbacks` to expand and collapse the category
    - `clear_all_selections` callback at the end of `left_hand_nav_bar_callbacks`
    - `/callbacks/update_search_results` so that it can be used to change search results
3. If a new metadata option is added to an existing category:
    - Adding the option to the collapsible checklist in `left_hand_nav_bar` shouldn't require any callbacks to be changed.
    - Don't forget to update the category's popover info text in `left_hand_nav_bar`

## Responsiveness

Two responsive elements appear in `left_hand_nav_bar`.

On phones, the left hand navigation bar takes up a lot of space requiring users to scroll quite far down to see their results. To mitigate this, the `filtering_collapse_button` appears on extra small screens to allow users to collapse the search options, bringing the list of modules up higher on the screen.

If a user collapses the navigation bar when their window is small and then expands the window, a second button, the `filtering_expand_button` will appear. Most users will never encounter this functionality.