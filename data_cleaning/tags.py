import pandas as pd
import numpy as np
import warnings
import os
warnings.filterwarnings("ignore")

# Current working directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Change working directory
os.chdir(dir_path)

def read_data_from_csv():
    tags=pd.read_csv('../data/tags.csv')
    return tags


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    tags=read_data_from_csv()

    #Remove Unwanted columns
    tags.drop(columns=['location'], axis=1, inplace=True)
    tags.rename(columns={'tag text':'tag_name', 'created time':'created_at'}, inplace=True)
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	tag_name
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "tags_cleaned.csv"
    tags.to_csv('../data/cleaned_data/tags_cleaned.csv')
    return tags


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()