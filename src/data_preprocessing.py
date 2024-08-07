import pandas as pd


def clean_column_names(data):
    # 
    data.columns = (data.columns
                        .str.lower()
                        .str.strip()
                        .str.replace(' ', '_')
                        .str.replace('[^a-z0-9_]', '', regex=True))
    return data

def preprocess_data(data):
    clean_columns_df = clean_column_names(data)
    dropped_duplicates_df = clean_columns_df.drop_duplicates().reset_index(drop=True)
    ## If we proceed deleting null values the we will just loose 12.09% of the total data   
    preprocessed_df = dropped_duplicates_df.dropna().reset_index(drop=True)
    return preprocessed_df
