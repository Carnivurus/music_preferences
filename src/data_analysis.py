import pandas as pd

def data_analysis(data):

    duplicated_rows = data.duplicated().sum()
    null_rows = data.isnull().any(axis=1).sum()
    print('-----------------------------')
    print('Data info')
    print(data.info(), end='\n')
    print('-----------------------------')
    print(f'Columns:{data.columns}')
    print(f'Duplicated Rows:{duplicated_rows}')
    print(f'Null Rows:{null_rows}', end='\n')
    print(f'Null share: {(null_rows/data.shape[0]*100):.2f}%')
    # data.sample(10)

