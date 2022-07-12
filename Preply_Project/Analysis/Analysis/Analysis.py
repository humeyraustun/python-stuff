import pandas as pd
import numpy as np

data = pd.read_csv(r'20220430.csv')
data.head()
data.columns
data.shape
data[data["tutorPrice"]>10]
data[data["tutorPrice"]<10]
data["totalIncome"] = data["tutorPrice"]*data["tutorLessons"]

print("biddi!")
