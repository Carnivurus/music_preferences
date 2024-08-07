import os
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def eda_report(data, cols):
    
    eda_path = './data/eda_results/'

    data.describe()

# Creating the path if not exists
    if not os.path.exists(eda_path):
        os.makedirs(eda_path)

# Plotting categoric cols

    num_height = math.ceil(len(cols)/2)
    fig1, axes = plt.subplots(num_height, 2, figsize=(12,12))

    # for col, ax in zip(cols)

    for column, ax in zip(cols, axes.flatten()):
            sns.countplot(x=column,data=data,ax=ax)
            ax.set_title(f'Histogram of {column}', fontsize=16)
            ax.set_xlabel('Category')
            ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.show()