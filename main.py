from src.data_loader import data_loader
from src.data_analysis import data_analysis
from src.data_preprocessing import preprocess_data
from src.eda_report import eda_report
from src.hypothesis_testing import test_hypothesis_one, test_hypothesis_two, test_hypothesis_three

file_id = '1Fhfx8KGJYvYxWUrmTxPGbzehi-BXatpe'

# Loading data
data = data_loader(file_id)
data.sample(10)

# Analyzing data
data_analysis(data)

# Preprocessing
preprocessed_df = preprocess_data(data)

#EDA
cols = ['day', 'city']
eda_report(preprocessed_df,cols)

#Hypothesis
test_hypothesis_one(preprocessed_df)
test_hypothesis_two(preprocessed_df)
test_hypothesis_three(preprocessed_df)


