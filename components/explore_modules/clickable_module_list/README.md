The `clickable_module_list` renders all modules that meet the criteria filtered for from the Left Hand Navigation Bar (stored in `hidden_filtered_modules`) and lets users interact with those modules.

![Search results showing matching modules.](/media/Explore_Modules_Results.png)

Each module is displayed as a card:

![A Module Card.](/media/Module_Card.png)

These cards are further brokend down within the `module_cards` sub-directory into 
1. `module_cards/card_structure` which gives the layout of the card itself
2. `module_cards/modal_card_details` which defines the modal pop-up with more detailed information on each module, reached by clicking the card's "More Details" button.
![More Details pop-up for Bash: Combining Commands Module.](/media/Module_More_Details.png)
3. `module_cards/module_level` which renders the Module Level popover.
![Level popover shows approximately how many hours of prerequisites the module has.](/media/Module_Level_Popover.png)
