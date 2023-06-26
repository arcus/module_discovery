# Module Discovery App

## File structure

There are three main folders, 
- `assets` for stylesheets and other visual settings, 
- `components` which contains each of the panels/components of the app. Any callbacks that are internal to a component, e.g. expanding and hiding the component or something within the component, is in the component's directory. For example `components/module_details_panel/` contains `module_details_panel.py` as well as `module_details_panelcallbacks.py`, but also smaller sub-components of that panel like the `title_link`, `tags`, and `pre_reqs`.
- `callbacks` for any callbacks that transmit information between different components. Note that these callbacks will filter through the hidden components of `hidden_active_module` and `hidden_filtered_modules`. In the future there may be a third hidden component (possibly visible) for `my_modules`.

## Module data

The script `process_data.sh` runs through all the modules and creates the `module_data.py` file which contains a pandas dataframe with some (soon to be all) of the metadata for each module. 
- NOTE: these scripts need to be run from the [education_modules repo](https://github.com/arcus/education_modules/tree/main)
- TODO: automate the data processing in the education_modules repo and have the `module_data` pull directly from that repo.


## Dockerization

The `Dockerfile`, `requirements.txt` are set up to allow this to run in a Docker container on a local computer. To run it, open Docker and a command line interface.

From the top level directory of this repository run:

```
docker build -t module_discovery_app .
```

This may take some a few minutes the first time you run it. Once it is completed, run:

```
docker run module_discovery_app
```

The output of this command will include `[INFO] Listening at: http://0.0.0.0:8050`. Open a web browser to http://0.0.0.0:8050 to see and interact with the app.

## Running the app locally

If all of the requirements (see `requirements.txt`) are correct on your machine, you can run the app locally without using dcoker at all with the command:

```
python app.py
```

This will open a port where you can see the app locally. To see error messages, callbacks, and for the app to live update as you develop, set `debug=True` in the last line of `app.py`.
