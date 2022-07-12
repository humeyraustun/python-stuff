import pandas as pd 
import numpy as np 

data  = pd.read_csv(r'20220503.csv' )
data.read_table('20220503.csv', sep= ',')

print ("biddi!")