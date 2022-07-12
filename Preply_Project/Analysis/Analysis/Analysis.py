import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv(r'20220430.csv')
data.shape
data.columns
data.head()
data=data.rename(columns = {"tutorPrice" : "tutorPrice(USD)"})
data["tutorPrice(GBP)"] = (data["tutorPrice(USD)"])/(1.18)
cheaptutors=data[data["tutorPrice(USD)"]<=10]
modesttutors=data[(data["tutorPrice(USD)"]> 11) & (data["tutorPrice(USD)"]<20)]
expensivetutors=data[data["tutorPrice(USD)"]>=20]
data.mean()
data["tutorPrice(USD)"].mean()
data["totalIncome"].mean()
data.mean()
data.info()
data.describe()
print("biddi!")
