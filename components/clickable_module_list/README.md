This is the list of all modules that meet the criteria filtered for from the left-hand nav bar.

Each module is displayed as a card, which is created by the functions in the `module_cards` sub-directory:
- `card_structure` gives the layout of the card itself
- `modal_card_details` defines the modal pop-up with more detailed information on each module.
- `module_level` computes each module's "level" based on the sum total estimate time in minutes of all modules that precede it.
