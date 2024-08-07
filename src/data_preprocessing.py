import pandas as pd


def clean_column_names(data):
    # 
    data.columns = (data.columns
                        .str.lower()
                        .str.strip()
                        .str.replace(' ', '_')
                        .str.replace('[^a-z0-9_]', '', regex=True))
    return data

def check_values(data):
    # Filtrar por no obj
    for column in data.columns:
        print(f'Values for {column}',end='\n')
        print(data[column].value_counts())
        print('----------')
