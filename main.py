import pandas as pd
from src.data_loader import data_loader
from src.data_analysis import data_analysis
from src.data_preprocessing import preprocess_data
from src.eda_report import eda_report, check_values, top_ten

file_id = '1Fhfx8KGJYvYxWUrmTxPGbzehi-BXatpe'

# Loading data
data = data_loader(file_id)

# Analyzing data
data_analysis(data)

# Preprocessing
preprocessed_df = preprocess_data(data)

# EDA
cols = ['day', 'city']
eda_report(preprocessed_df,cols)


# data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S').dt.time
# data.select_dtypes(exclude='number')


# Hypothesis

# pd.pivot_table(data,values='track',index='city', columns='day', aggfunc='count')



