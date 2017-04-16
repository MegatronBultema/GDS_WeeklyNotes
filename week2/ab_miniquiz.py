'''

|                | Visitors  | Registrations | Purchases |
|----------------|-----------|---------------|-----------|
| Landing Page 1 | 998,832   | 331,912       | 18,255    |
| Landing Page 2 | 1,012,285 | 349,643       | 18,531    |
| Landing Page 3 | 995,750   | 320,432       | 18,585    |
>>>st.norm.ppf(.975)
1.959963984540054
>>>st.norm.ppf(.025)
-1.960063984540054
'''
import scipy.stats as scs
import pandas as pd
import math
data = []
# make observed data table
columns = ['Page','Visitors', 'Registrations','avg.Registration', 'Purchases', 'avg.Purchases']
#columns = ['Landing_Page_1', 'Landing_Page_2','Landing_Page_3']
data.append(['Landing_Page_1', 998832, 331912, float(331912)/998832,18255,float(18255)/998832])
data.append(['Landing_Page_2', 1012285, 349643,float(349643)/1012285, 18531, float(18531)/1012285])
data.append(['Landing_Page_3', 995750, 320432, float(320432)/995750, 18585, float(18585)/995750])
df = pd.DataFrame(data = data, columns = columns)
print(df)


conf = 0.95
comparisons = 6
alpha = conf

for page in df['Page']:
    print(page)
    for metric in df.iloc[:,2:]:
        print(page, metric)

ab.z_test(df.loc[0,'avg.Registration'], df.loc[1,'avg.Registration'], df.loc[0,'Visitors'], df.loc[1,'Visitors'])

def z_test(ctr_old, ctr_new, nobs_old, nobs_new,
           effect_size=0., two_tailed=True, alpha=.05):
    """Perform z-test to compare two proprtions (e.g., click through rates (ctr)).

        Note: if you set two_tailed=False, z_test assumes H_A is that the effect is
        non-negative, so the p-value is computed based on the weight in the upper tail.

        Arguments:
            ctr_old (float):    baseline proportion (ctr)
            ctr_new (float):    new proportion
            nobs_old (int):     number of observations in baseline sample
            nobs_new (int):     number of observations in new sample
            effect_size (float):    size of effect
            two_tailed (bool):  True to use two-tailed test; False to use one-sided test
                                where alternative hypothesis if that effect_size is non-negative
            alpha (float):      significance level

        Returns:
            z-score, p-value, and whether to reject the null hypothesis
    """
    conversion = (ctr_old * nobs_old + ctr_new * nobs_new) / \
                 (nobs_old + nobs_new)

    se = math.sqrt(conversion * (1 - conversion) * (1 / nobs_old + 1 / nobs_new))

    z_score = (ctr_new - ctr_old - effect_size) / se

    if two_tailed:
        p_val = (1 - scs.norm.cdf(abs(z_score))) * 2
    else:
        # Because H_A: estimated effect_size > effect_size
        p_val = 1 - scs.norm.cdf(z_score)

    reject_null = p_val < alpha
    print 'z-score: %s, p-value: %s, reject null: %s' % (z_score, p_val, reject_null)
    return z_score, p_val, reject_null






'''
def plot_t_test(group_1_name, group_2_name):
    fig = plt.figure()
    group_1_mean_reg = 331,912/998,832
    group_2_mean_reg = 349,643/1,012,285
    group_3_mean_reg = 320,432/995,750

    group_1_stddev = (331912 - 998832)**2 + (666920-998832)**2
    group_2_stddev = (349,643 - 1,012,285)**2 + (1,012,285 - 349,643)**2
    group_3_stddev = ()

    group_1_dist = scs.norm(loc=group_1_mean)
    group_2_dist = scs.norm(loc=group_2_mean)
    group_3_dist = scs.norm(loc=group_3_mean)

    print '%s Mean CTR: %s' % (group_1_name, group_1_mean)
    print '%s Mean CTR: %s' % (group_2_name, group_2_mean)
    print '%s Mean CTR: %s' % (group_3_name, group_3_mean)
    print '%s diff in mean: %s', abs('group_2_mean-group_1_mean', group_2_mean-group_1_mean)
    print '%s diff in mean: %s', abs('group_2_mean-group_1_mean',group_2_mean-group_1_mean)
    p_val = stats.ttest_ind(group_1_dist, group_2_dist, equal_var=False)[1]
    print 'p value is:', p_val

    group_1_df['CTR'].hist(normed=True, label=group_1_name, color='g', alpha=0.3)
    group_2_df['CTR'].hist(normed=True, label=group_2_name, color='r', alpha=0.3)
    plt.axvline(group_1_mean, color='r', alpha=0.6, lw=2)
    plt.axvline(group_2_mean, color='g', alpha=0.6, lw=2)

    plt.ylabel('Probability Density')
    plt.xlabel('CTR')
    plt.legend()
    plt.grid('off')
    plt.show()

plot_t_test(df_signed_in, df_not_signed_in, 'Signed In', 'Not Signed In')
'''
