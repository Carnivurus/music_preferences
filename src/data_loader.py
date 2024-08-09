import pandas as pd

def data_loader(file_id):
    '''This function will import the DataFrame for the gsheet resource'''
    url = pd.read_csv(f'https://drive.google.com/uc?export=download&id={file_id}')
    return url