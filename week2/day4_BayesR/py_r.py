import pandas as pd
import numpy as np
import statsmodels.api as sm
#% matplotlib inline
from pandas.tools.plotting import scatter_matrix

mtcars2 = sm.datasets.get_rdataset('mtcars')
df = pd.DataFrame(mtcars2.data)
df['liter/100_Kilometers']= df['mpg']/235.215
medianHP=df['hp'].median()
maxhp=df['hp'].max()
df['hp_class']=pd.cut(df['hp'], [0, medianHP, maxhp], labels=['low', 'high'])
print(df.head())
df.to_csv('dfmtcars2_pd.csv')
#scatter_matrix(df[[0,2,3,4,5]], alpha=0.3, figsize=(8, 8), diagonal='kde', marker='o');
