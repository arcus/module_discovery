import pandas as pd

#EDUCATION_MODULES

#read in metadata from education_modules repository, at some point this should be coming from a local copy of the json file, once it works I'll get the action set up.
education_modules_df = pd.read_json("assets/education_modules.json") 

#remove empty rows created by data processing
education_modules_df= education_modules_df.dropna(axis=0, how='all')

#set 'module_id' as the index
education_modules_df = education_modules_df.set_index('module_id')

df=education_modules_df.copy()