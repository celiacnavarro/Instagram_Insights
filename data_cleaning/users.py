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
    users=pd.read_csv('../data/users.csv')
    return users


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    users=read_data_from_csv()

    #Remove Unwanted columns
    users.drop(columns=['private/public', 'post count', 'Verified status'], axis=1, inplace=True)
    users.rename(columns={'name':'username', 'created time':'created_at'}, inplace=True)
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	username
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "users_cleaned.csv"
    users.to_csv('../data/cleaned_data/users_cleaned.csv')
    return users


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()