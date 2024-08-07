import pandas as pd
from src.data_loader import data_loader

file_id = '1Fhfx8KGJYvYxWUrmTxPGbzehi-BXatpe'
data = data_loader(file_id)

print(data)