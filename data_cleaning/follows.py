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
    follows=pd.read_csv('../data/follows.csv')
    return follows


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    follows=read_data_from_csv()

    #Remove Unwanted columns
    
    follows.drop(columns=['is follower active', 'followee Acc status'], axis=1, inplace=True)
    follows.rename(columns={'follower':'follower_id', 'followee ':'followee_id', 'created time':'created_at'}, inplace=True)
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	follower_id
    # 2.	followee_id
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "follows_cleaned.csv"
    follows.to_csv('../data/cleaned_data/follows_cleaned.csv')
    return follows


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()