import numpy as np
import pandas as pd
import scipy.stats as scs

data = []
# make observed data table
columns = ['race','yes', 'no','totals']
data.append(['black', 45,85,130])
data.append(['white', 14,218,232])
data.append(['total', 59,303,362])
df = pd.DataFrame(data = data, columns = columns)
df.set_index(df['race'],inplace = True)
del df['race']
print("Observed data")
print(df)


print("\nFinding expected values")
nrow, ncol = df.shape[0], df.shape[1] # number of rows and columns
GT = df.sum().sum()
df_row_tot = sum(df.iloc[:,i] for i in range(nrow))
df_col_tot = sum(df.iloc[i,:] for i in range(ncol))
print("\nrow totals:")
print(df_row_tot)
print("\ncolumn totals:")
print(df_col_tot)

GT = df.sum().sum()
E = np.zeros((nrow, ncol))
for i in range(nrow):
    for j in range(ncol):
        E[i,j] = round(df_row_tot[i]*df_col_tot[j] / GT, 2)
print('\nExpected values\n{0}'.format(E))

chi2 = 0
for i in range(nrow):
    for j in range(ncol):
        chi2 += ((df.iloc[i,j] - E[i,j])**2/E[i, j])
print("\nThe chi-square value is {0:0.2f}".format(chi2))

ddof = (nrow-1) * (ncol - 1)
print("\nThe degrees of freedom are {0}".format(ddof))

'''
for this data
The chi-square value is 49.88

The degrees of freedom are 4
so p-value is much less than 0.001 and we reject the null hypothesis that there is not effect of race on
penalty sentencing
'''
print(1 - scs.chi2.cdf(chi2, ddof))
