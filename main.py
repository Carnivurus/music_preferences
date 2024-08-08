import pandas as pd
from src.data_loader import data_loader
from src.data_analysis import data_analysis
from src.data_preprocessing import preprocess_data
from src.eda_report import eda_report, check_values, top_ten
from src.hypothesis_testing import test_hypotheses_one

file_id = '1Fhfx8KGJYvYxWUrmTxPGbzehi-BXatpe'

# Loading data
data = data_loader(file_id)
data.sample(10)

# Analyzing data
data_analysis(data)

# Preprocessing
preprocessed_df = preprocess_data(data)

# EDA
# cols = ['day', 'city']
# eda_report(preprocessed_df,cols)

# Hypothesis
uno, dos= test_hypotheses_one(preprocessed_df)

