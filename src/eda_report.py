import math
import matplotlib.pyplot as plt
import seaborn as sns

def eda_report(data, cols):
    '''
    This function provides a quick overview of the values in each specified column of a DataFrame.
    You need to pass the DataFrame (data) and the columns (cols) to be analyzed.

    The output will be divided into three sections:

    - Checking Values: Displays the count of unique values for each specified column.
    - Plot Chart: Plots the distribution of values for the specified columns.
    - Top Ten Values: Shows the top ten most frequent values in each specified column.
    '''

    print('-----------------------------')
    print('CHECKING VALUES')
    check_values(data)
    data.describe()
    chart_plot(data, cols)
    print('-----------------------------')
    print('TOP TEN VALUES')
    top_ten(data.iloc[:,1:])

def check_values(data):
    '''
    This subfunction displays the count of unique values for each specified column.
    It takes the DataFrame (data) and a list of columns (cols) as input.
    '''
    # Filtrar por no obj
    for column in data.columns:
        print(f'Values for {column}',end='\n')
        print(data[column].value_counts())
        print('-----------------------------')

def top_ten(data):
    '''
    This subfunction shows the top ten most frequent values in each specified column.
    It takes the DataFrame (data) and a list of columns (cols) as input.
    '''
    for col in data.columns:
        result = data[col].value_counts().head(10)
        print('-----------------------------')
        print(result)

def chart_plot(data, cols):
    '''
    This subfunction plots the distribution of values for the specified columns.
    It takes the DataFrame (data) and a list of columns (cols) as input.
    '''
# Plotting categoric cols

    num_height = math.ceil(len(cols)/2)
    fig1, axes = plt.subplots(num_height, 2, figsize=(6,3))

    # for col, ax in zip(cols)

    for column, ax in zip(cols, axes.flatten()):
            sns.countplot(x=column,data=data,ax=ax)
            ax.set_title(f'Histogram of {column}', fontsize=16)
            ax.set_xlabel('Category')
            ax.set_ylabel('Frequency')
    fig1.tight_layout()
    fig1.show()