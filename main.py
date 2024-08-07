import pandas as pd
from src.data_loader import data_loader
from src.data_analysis import data_analysis
from src.data_preprocessing import clean_column_names, check_values
from src.eda_report import eda_report

file_id = '1Fhfx8KGJYvYxWUrmTxPGbzehi-BXatpe'

# Loading data
data = data_loader(file_id)

# Analyzing data
data_analysis(data)
data.sample(10)

# Preprocessing
clean_column_names(data)
data = data.drop_duplicates()
print(data.sample(10))
data_analysis(data)
data = data.dropna()
data_analysis(data)

check_values(data)


# EDA
# cols = ['track', 'artist', 'genre', 'city', 'day']
cols = ['day', 'city']
eda_report(data,cols)


# If we proceed deleting null values the we will just loose 12.09% of the total data




# data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S').dt.time
# data.select_dtypes(exclude='number')