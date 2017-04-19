'''
##Build a Linear Regression Model

You are provided with a dataset `data/loansData.csv`. Build a linear regression
model that identifies the key drivers of interest rate for individual loans.
Perform exploratory data analysis of the relationship between the features and
relationship of the features with the response. Select your features and
use `statsmodels` to build a linear regression model.

You do not have to use all the variables. Focus on building the simplest model
that explains interest rate. Justify the features you have or have not included
in your model.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from pandas.tools.plotting import scatter_matrix
import statsmodels.api as sms

df=pd.read_csv('data/loansData.csv')



#remove fico_range for now because it is in string format. Go back and convert when I have time.

dffico_unique=df['fico_range'].unique()
dffico_unique.sort()
d2={}

for i,x in enumerate(dffico_unique):
    d2[x]=i

df['fico_category'] = df["fico_range"].map(d2)
f=list(df.columns)
f.remove('fico_range')
t=f.pop(0)
print(df.head())
print(f)
print(t)


def ols(df, target, features):
    '''
    Input
        df : pandas dataframe with all columns
        target: string with the column name to be used for the target (Y)
        features: list of strings of column names to be infestigated as features
    '''
    y_target=df[target]
    x_var=df[features]
    x_var = sm.add_constant(x_var)
    model = sms.OLS(y_target, x_var).fit()
    summary = model.summary()
    return summary


'''                    OLS Regression Results
==============================================================================
Dep. Variable:          interest_rate   R-squared:                       0.746
Model:                            OLS   Adj. R-squared:                  0.746
Method:                 Least Squares   F-statistic:                     1834.
Date:                Tue, 18 Apr 2017   Prob (F-statistic):               0.00
Time:                        10:10:24   Log-Likelihood:                -5402.2
No. Observations:                2498   AIC:                         1.081e+04
Df Residuals:                    2493   BIC:                         1.084e+04
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================================
                                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
----------------------------------------------------------------------------------------------
const                         11.4733      0.196     58.463      0.000        11.088    11.858
amount_requested             6.78e-05   2.23e-05      3.045      0.002      2.41e-05     0.000
amount_funded_by_investors  7.361e-05   2.23e-05      3.295      0.001      2.98e-05     0.000
loan_length                    0.1368      0.005     29.358      0.000         0.128     0.146
fico_category                 -0.4383      0.006    -72.485      0.000        -0.450    -0.426
==============================================================================
Omnibus:                      153.829   Durbin-Watson:                   1.952
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              247.864
Skew:                           0.490   Prob(JB):                     1.50e-54
Kurtosis:                       4.192   Cond. No.                     9.52e+04
=============================================================================='''

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:          interest_rate   R-squared:                       0.503
Model:                            OLS   Adj. R-squared:                  0.503
Method:                 Least Squares   F-statistic:                     2527.
Date:                Tue, 18 Apr 2017   Prob (F-statistic):               0.00
Time:                        10:07:22   Log-Likelihood:                -6242.3
No. Observations:                2498   AIC:                         1.249e+04
Df Residuals:                    2496   BIC:                         1.250e+04
Df Model:                           1
Covariance Type:            nonrobust
=================================================================================
                    coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------
const            18.6484      0.126    148.421      0.000        18.402    18.895
fico_category    -0.4235      0.008    -50.269      0.000        -0.440    -0.407
==============================================================================
Omnibus:                      129.175   Durbin-Watson:                   1.991
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              149.000
Skew:                           0.596   Prob(JB):                     4.42e-33
Kurtosis:                       2.903   Cond. No.                         31.9
==============================================================================
'''

'''
==============================================================================
Dep. Variable:          interest_rate   R-squared:                       0.690
Model:                            OLS   Adj. R-squared:                  0.690
Method:                 Least Squares   F-statistic:                     2779.
Date:                Tue, 18 Apr 2017   Prob (F-statistic):               0.00
Time:                        10:09:07   Log-Likelihood:                -5652.1
No. Observations:                2498   AIC:                         1.131e+04
Df Residuals:                    2495   BIC:                         1.133e+04
Df Model:                           2
Covariance Type:            nonrobust
=================================================================================
                    coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------
const            11.1836      0.216     51.684      0.000        10.759    11.608
fico_category    -0.4268      0.007    -64.142      0.000        -0.440    -0.414
loan_length       0.1819      0.005     38.820      0.000         0.173     0.191
==============================================================================
Omnibus:                       94.386   Durbin-Watson:                   1.968
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              108.105
Skew:                           0.454   Prob(JB):                     3.35e-24
Kurtosis:                       3.461   Cond. No.                         206.
=============================================================================='''


#I choose fico_category, loan_length
'''
              OLS Regression Results
==============================================================================
Dep. Variable:          interest_rate   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.745
Method:                 Least Squares   F-statistic:                     2435.
Date:                Tue, 18 Apr 2017   Prob (F-statistic):               0.00
Time:                        10:11:23   Log-Likelihood:                -5406.8
No. Observations:                2498   AIC:                         1.082e+04
Df Residuals:                    2494   BIC:                         1.084e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================================
                                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
----------------------------------------------------------------------------------------------
const                         11.4669      0.197     58.337      0.000        11.081    11.852
fico_category                 -0.4374      0.006    -72.303      0.000        -0.449    -0.426
loan_length                    0.1380      0.005     29.666      0.000         0.129     0.147
amount_funded_by_investors     0.0001   5.98e-06     23.265      0.000         0.000     0.000
==============================================================================
Omnibus:                      149.913   Durbin-Watson:                   1.953
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              239.488
Skew:                           0.483   Prob(JB):                     9.90e-53
Kurtosis:                       4.169   Cond. No.                     6.66e+04
=============================================================================='''

'''
                  OLS Regression Results
==============================================================================
Dep. Variable:          interest_rate   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.745
Method:                 Least Squares   F-statistic:                     2432.
Date:                Tue, 18 Apr 2017   Prob (F-statistic):               0.00
Time:                        10:14:07   Log-Likelihood:                -5407.6
No. Observations:                2498   AIC:                         1.082e+04
Df Residuals:                    2494   BIC:                         1.085e+04
Df Model:                           3
Covariance Type:            nonrobust
====================================================================================
                       coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------------
const               11.4692      0.197     58.328      0.000        11.084    11.855
fico_category       -0.4388      0.006    -72.454      0.000        -0.451    -0.427
loan_length          0.1372      0.005     29.404      0.000         0.128     0.146
amount_requested     0.0001   5.96e-06     23.224      0.000         0.000     0.000
==============================================================================
Omnibus:                      152.912   Durbin-Watson:                   1.953
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              241.247
Skew:                           0.495   Prob(JB):                     4.11e-53
Kurtosis:                       4.157   Cond. No.                     6.83e+04
==============================================================================
'''

#linreg_m= 11.1836 + -0.4268*x['fico_category'] + 0.1819*x['loan_length']
#linreg_m2= 11.4692 + -0.4388*x['fico_category'] + 0.1372*x['loan_length'] +0.0001*x['amount_requested ']

def plot_residuals(df,target):
    y_meany= df.apply(lambda x: x[target]-df[target].mean(), axis=1)
    y_modely=df.apply(lambda x: 11.4692 + -0.4388*x['fico_category'] + 0.1372*x['loan_length'] +0.0001*x['amount_requested'],axis=1)
    fig=plt.figure()
    ax =fig.add_subplot(111)
    ax.scatter(y_modely,y_meany)
