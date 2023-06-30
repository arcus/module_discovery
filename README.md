# Module Discovery App

## Overview

The purpose of this app is to allow for easier discovery of the educational modules created as part of the DART program. Ultimately this will replace the current public-facing [list of all modules on the DART website](https://arcus.github.io/education_modules/list_of_modules).

This app will allow users to learn more about each module, investigate how the modules are connected, and search for particular topics or key words.

![The module discovery app.](media/example_screenshot.png)

**NOTE:** This is a prototype. Not all modules are currently included in the app, and only half of those included have complete metadata. 


## Development
### File structure

There are three main folders, 
- `assets` for stylesheets and other visual settings, 
- `components` which contains each of the panels/components of the app. Any callbacks that are internal to a component, e.g. expanding and hiding the component or something within the component, is in the component's directory. For example `components/module_details_panel/` contains `module_details_panel.py` as well as `module_details_panelcallbacks.py`, but also smaller sub-components of that panel like the `title_link`, `tags`, and `pre_reqs`.
- `callbacks` for any callbacks that transmit information between different components. Note that these callbacks will filter through the hidden components of `hidden_active_module` and `hidden_filtered_modules`. In the future there may be a third hidden component (possibly visible) for `my_modules`.

### Module data

The script `process_data.sh` runs through all the modules and creates the `module_data.py` file which contains a pandas dataframe with some (soon to be all) of the metadata for each module. 
- NOTE: these scripts need to be run from the [education_modules repo](https://github.com/arcus/education_modules/tree/main)
- TODO: automate the data processing in the education_modules repo and have the `module_data` pull directly from that repo.

## Testing

### Dockerization

The `Dockerfile`, `requirements.txt` are set up to allow this to run in a Docker container on a local computer. To run it, open Docker and a command line interface.

From the top level directory of this repository run:

```
docker build -t module_discovery_app .
```

This may take some a minute the first time you run it. Once it is completed, run:

```
docker run -d -p 8050:8050 module_discovery_app
```

Open a web browser to http://0.0.0.0:8050 to see and interact with the app.

### Running the app locally

If all of the requirements (see `requirements.txt`) are correct on your machine, you can run the app locally without using docker at all with the command:

```
python app.py
```

This will open a port where you can see the app locally. To see error messages, callbacks, and for the app to live update as you develop, set `debug=True` in the last line of `app.py`.

**NOTE:** There will be one error on loading. You can ignore it completely.
