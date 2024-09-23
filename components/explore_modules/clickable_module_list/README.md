The `clickable_module_list` renders all modules that meet the criteria filtered for from the Left Hand Navigation Bar (stored in `hidden_filtered_modules`) and lets users interact with those modules.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Explore_Modules_Results.png?raw=true" alt="Search results showing matching modules." width="400px"/> 

Each module is displayed as a card:

<img src="https://github.com/arcus/module_discovery/blob/main/media/Module_Card.png?raw=true" alt="A Module Card." width="400px"/> 

These cards are further brokend down within the `module_cards` sub-directory into 
1. `module_cards/card_structure` which gives the layout of the card itself
2. `module_cards/modal_card_details` which defines the modal pop-up with more detailed information on each module, reached by clicking the card's "More Details" button.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Module_More_Details.png?raw=true" alt="More Details pop-up for Bash: Combining Commands Module." width="400px"/> 


3. `module_cards/module_level` which renders the Module Level popover.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Module_Level_Popover.png?raw=true" alt="Level popover shows approximately how many hours of prerequisites the module has." width="200px"/> 
