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
    photo_tags=pd.read_csv('../data/photo_tags.csv')
    return photo_tags


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    photo_tags=read_data_from_csv()

    #Remove Unwanted columns
    
    photo_tags.drop(columns=['user id'], axis=1, inplace=True)
    photo_tags.rename(columns={'photo':'photo_id', 'tag ID':'tag_id'}, inplace=True)
    #rename columns, only these columns are allowed in the dataset
    # 1.	photo_id
    # 2.	tag_id
    
    #export cleaned Dataset to newcsv file named "photo_tags_cleaned.csv"
    photo_tags.to_csv('../data/cleaned_data/photo_tags_cleaned.csv')
    return photo_tags


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()