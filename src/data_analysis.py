
def data_analysis(data):
    '''This function will receive a dataframe to be analized, 
    showing to the following variables:
    - General info about the DataFrame (data types, count, etc.)
    - Column Names
    - Number of duplicated rows
    - Number of null rows
    - Percentage of rows with null values
    '''

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

