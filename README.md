# Module Discovery App

## Overview

The purpose of this app is to allow for easier discovery of the educational modules created as part of the DART program. Ultimately this will replace the current public-facing [list of all modules on the DART website](https://arcus.github.io/education_modules/list_of_modules).

This app will allow users to learn more about each module, investigate how the modules are connected, and search for particular topics or key words and build thier own pathways.

**NOTE:** This is a prototype that is in a phase of rapid development. All effort will be made to keep this README up to date, but some changes might slip by. If something isn't working as expected, please let us know by creating an issue.

## Public prototype

A public prototype of this app is hosted at [https://learn.arcus.chop.edu](https://learn.arcus.chop.edu).

## Development

### File structure

There are several top-level folders:
- `assets` contains the metadata for the educational modules that this app presents.
- `components` contains each of the panels/components of the app, both the visible and the hidden components. Any callbacks that are internal to a component, e.g. expanding and hiding the component or something within the component, is in the component's directory. 
- `callbacks` contains any callbacks that transmit information between different components, namely callbacks that update one of the app's hidden components.
- `network_analysis` is where the interconnections between modules are processed using the `networkx` package.

Two important python files are also at the top level:
- `app.py` is the python file which runs the app. It contains the visual layout of the components and calls all of the callbacks.
- `module_data.py` is where metadata from the assets folder is processed into a single pandas dataframe for the app to use.

#### Mini dataset for debugging
When developing new features it can be extremely helpful to work out bugs and callbacks on this smaller set of data. Uncomment the last line in `module_data.py` to get a mini dataset for this purpose.

## Testing

Clone or download this repository to run the app yourself!

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

## Accessibility 

### Features
All information and relationships represented in the network graphs are also communicated via buttons in the Module Details panel.

### Unknowns
This is a Dash/Plotly app which has not been tested with any accessibilty technologies. 

### Suggest improvements
If you have needs that are not being met, or ideas for how to test or improve the accessibility of this app, please [create an accessibility issue](https://github.com/arcus/module_discovery/issues/new) so we can work to address it!
