This component contains the list of a user's modules. It renders the data stored in the `hidden_pathway` component with the function in `my_modules_callbacks`.

![Your Learning Pathway tab](/media/Your_Learning_Pathway.png)

## Update the pathway

The internal callbacks allowing a user to re-order the modules in that list are also here.

The line for each module in the pathway is built by `pathway_buttons`.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Pathway_Buttons.png?raw=true" alt="The three ways a module's row could appear in the pathway." width="400px"/> 



Every module's row contains 4 buttons: 
- **Up** moves the module up one in the pathway
- **Down** moves the module down one in the pathway 
- **Module Name** button opens a popover with the module details created in `/componenets/explore_modules/clickable_module_list/module_cards/modal_card_details`
- **X** removes the module from the pathway

Depending on the current order of the pathway there may also be a red or yellow icon to the left of the row, indicating that the module is out of order, or has prerequisites not included in this pathway.

<img src="https://github.com/arcus/module_discovery/blob/main/media/Pathway_Out_Of_Order.png?raw=true" alt="A red icon opens a helpful message letting the user know which modules that are currently after this module in the pathway should precede it." width="300px"/> 


<img src="https://github.com/arcus/module_discovery/blob/main/media/Pathway_Missing_Prereq.png?raw=true" alt="A yellow icon opens a helpful message letting the user know which prerequisite modules are not yet in their pathway." width="300px"/> 


To resolve all red icon warnings at once, users can click the "Order pathway by module dependencies" button at the top of their pathway. 

All of these buttons used to change the order or contents of the pathway update the `hidden_pathway` component via `/callbacks/update_pathway`.

## Copy the pathway

The copyable version of the pathway is built by `modal_save_pathway` and accessed with the "Get a copyable version of your pathway" button:

<img src="https://github.com/arcus/module_discovery/blob/main/media/Pathway_Copyable.png?raw=true" alt="Copyable pathway links." width="400px"/> 
