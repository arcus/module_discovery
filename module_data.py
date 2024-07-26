import pandas as pd

#EDUCATION_MODULES

#read in metadata from education_modules repository, which is automatically updated each week via a github action
education_modules_df = pd.read_json("assets/education_modules.json") 

#remove empty rows created by data processing
education_modules_df= education_modules_df.dropna(axis=0, how='all')

#set 'module_id' as the index
education_modules_df = education_modules_df.set_index('module_id')

# make estimated_time_in_minutes an integer instead of a float
education_modules_df['estimated_time_in_minutes'] = education_modules_df['estimated_time_in_minutes'].astype(int)

#ARCUS_RESOURCES
# go here
# when ready
# :)

#CREATE THE DATAFRAME FOR APP USE
df=education_modules_df.astype('str').copy()

#TRUNCATE THE DATAFRAME FOR DEBUGGING WITH BELOW CODE: 
#df = df.head(5)