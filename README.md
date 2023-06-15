# Module Discovery App

## Running the app locally

If all of the requirements (see `requirements.txt`) are correct on your machine, you can run the app locally with the command:

```
python app.py
```

This will open a port where you can see the app locally. To see error messages, callbacks, and for the app to live update as you develop, set `debug=True` in the last line of `app.py`.

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
The `Dockerfile`, `docker-compose.yml`, and `requirements.txt` are not yet sufficient to run this app in Docker. If these are necessary for deploying the app, we will need to update them.