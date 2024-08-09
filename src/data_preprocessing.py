import pandas as pd

def clean_column_names(data):
    '''Function created to perform a general clean of the column names
    from a DataFrame (lower, strip and replace)'''
    # 
    data.columns = (data.columns
                        .str.lower()
                        .str.strip()
                        .str.replace(' ', '_')
                        .str.replace('[^a-z0-9_]', '', regex=True))
    return data

def preprocess_data(data):
    '''This function will receive a DataFrame to perform a preprocessing, normalizing
    the column names, dropping duplicates and Null values, the output will be in a DataFrame format'''
    # Normalizing columns
    clean_columns_df = clean_column_names(data)
    # Dropping duplicates
    dropped_duplicates_df = clean_columns_df.drop_duplicates().reset_index(drop=True)
    # Dropping NA
    ## If we proceed deleting null values the we will just loose 12.09% of the total data   
    preprocessed_df = dropped_duplicates_df.dropna().reset_index(drop=True)
    preprocessed_df['time'] = pd.to_datetime(preprocessed_df['time'], format='%H:%M:%S')
    
    return preprocessed_df
