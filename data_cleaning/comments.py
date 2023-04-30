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
    comments=pd.read_csv('../data/comments.csv')
    return comments


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    comments=read_data_from_csv()

    #Remove Unwanted columns
    
    comments.drop(columns=['posted date', 'emoji used', 'Hashtags used count'], axis=1, inplace=True)
    comments.rename(columns={'comment':'comment_text', 'User  id':'user_id','Photo id':'photo_id','created Timestamp':'created_at'}, inplace=True)
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	comment_text
    # 3.	user_id
    # 4.	photo_id
    # 5.	created_at
    
    #export cleaned Dataset to newcsv file named "comments_cleaned.csv"
    comments.to_csv('../data/cleaned_data/comments_cleaned.csv')
    return comments


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()