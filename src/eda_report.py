import os
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def eda_report(data, cols):
    print('-----------------------------')
    print('CHECKING VALUES')
    check_values(data)
    chart_plot(data, cols)
    print('-----------------------------')
    print('TOP TEN VALUES')
    top_ten(data.iloc[:,1:])

def check_values(data):
    # Filtrar por no obj
    for column in data.columns:
        print(f'Values for {column}',end='\n')
        print(data[column].value_counts())
        print('-----------------------------')

def top_ten(data):
    for col in data.columns:
        result = data[col].value_counts().head(10)
        print('-----------------------------')
        print(result)



def chart_plot(data, cols):
    
    eda_path = './data/eda_results/'

    data.describe()

# Creating the path if not exists
    if not os.path.exists(eda_path):
        os.makedirs(eda_path)

# Plotting categoric cols

    num_height = math.ceil(len(cols)/2)
    fig1, axes = plt.subplots(num_height, 2, figsize=(6,3))

    # for col, ax in zip(cols)

    for column, ax in zip(cols, axes.flatten()):
            sns.countplot(x=column,data=data,ax=ax)
            ax.set_title(f'Histogram of {column}', fontsize=16)
            ax.set_xlabel('Category')
            ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()