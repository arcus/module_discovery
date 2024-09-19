# Assets

## Education Modules 
This is where all of the metadata about educational resources is stored. 

- `education_modules.json` contains the metadata from the [education_modules repository](https://github.com/arcus/education_modules). 
    - This file is automatically updated once a week via the ["Update metadata from education_modules repository" action](https://github.com/arcus/module_discovery/actions/workflows/update_module_data.yml)
    - If this needs to be updated immediately, there is a workflow_dispatch event trigger to run it manually.

## Pre-Made Pathways
There are 5 pre-made pathways that users can select and then modify to meet their needs. The file `pathways.py` contains a dictionary describing the each pathway, and pointing to its icon in the `pathway_icons` folder.

## Collections
The attributres of the collections of modules, including their symbols, colors, and descriptions, are stored here.

## Levels
The way we calculate and describe module levels is stored here.

## CHOP assets
- `CHOP_colors.py` contains the color definitions that match Children's Hospital of Philadelphia branding standards.
- `chop-ri--arcuslogo.png` is the Research Insitute's logo with Arcus.
- `Rubrik-SemiBold.otf` is the CHOP font for the app title.

## Other assets

Other assets will be added as they are gathered (or created in the case of Arcus educational resources that do not belong in the education_modules repo) and cataloged. 