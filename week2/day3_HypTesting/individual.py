'''
1. State which test should be used for the following scenarios to calculate p-values. Explain your
   choice.

   - You randomly select 50 dogs and 80 cats from a large animal shelter, and want to
     know if dogs and cats have the same weight.

     Two sample t-test, Ho: ucats=udogs, Ha ucats!=udogs
         could use 2 sample z test but t-test is more conservative and would approach z test at higher sample size

   - A random sample of San Franciscans and Oaklanders were surveyed about their favorite baseball team,
     and you want to determine if the same proportion of people like the SF Giants.

     Two sample t-test, Ho:


2. A study attempted to measure the influence of patients' astrological signs on their risk for heart failure.
   12 groups of patients (1 group for each astrological sign) were reviewed and the incidence of heart
   failure in each group was recorded.

   For each of the 12 groups, the researchers performed a z-test comparing the incidence of heart failure in one group to the    incidence among the patients of all the other groups (i.e. 12 tests). The group with the highest rate of heart failure was    Pisces, which had a p-value of .026 when assessing the null hypothesis that it had the same heart failure rate as the        group with the lowest heart failure rate, Leo. What is the the problem with concluding from this p-value that Pisces         have a higher rate of heart failure than Leos at a significance level of 0.05? How might you adjust your interpretation of    this p-value?

   If a researcher wants to conduct multiple tests (i.e. make multiple comparisons), we need to adjust the individual alpha(I) rate so that the overall experimental alpha(E) rate remains at the desired level.
        alpha(I)=alpha(e)/#comparisons

Part 2
We will use hypothesis testing to analyze **Click Through Rate (CTR)** on the New York Times website.
CTR is defined as the number of clicks a user makes per impression that is made upon the user.
We are going to determine if there is statistically significant difference between the mean CTR for
the following groups:
1. Signed in users v.s. Not signed in users
2. Male v.s. Female
3. Each of 7 age groups against each other (7 choose 2 = 21 tests)

1. Calculate the adjustment needed to account for multiple testing at the 0.05 significance level.
        For comparisons in #3 0.05/21 = 0.0024
'''
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats
df=pd.read_csv('ab-testing/data/nyt1.csv')
ctr= df[df['Impressions']!=0]
ctr.head()
ctr['CTR']=ctr['Clicks']/ctr['Impressions']
#ctr.hist()
sin=ctr[ctr['Signed_In']==1]
notin=ctr[ctr['Signed_In']!=1]
#sin.hist()
#notin.hist()
#plt.show()


#This is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected) values. This test assumes that the populations have identical variances.
ttest_signin=scipy.stats.ttest_ind(sin['CTR'], notin['CTR'], equal_var=False)


male=notin[notin['Gender']==1]
female=notin[notin['Gender']==0]
male.hist()
female.hist()
#plt.show()
ttest_gender=scipy.stats.ttest_ind(male['CTR'], female['CTR'], equal_var=False)
print('signed in: {}' .format(ttest_signin), 'gender: {}'.format(ttest_gender))


'''
signed in: Ttest_indResult(statistic=55.376117934260868, pvalue=0.0)
gender: Ttest_indResult(statistic=-3.2897560659351059, pvalue=0.0010028527313147612)

both comparisons have low (less than 0.05) p values so for both of them we would reject the null hypothesis that the two averages are equal. At first glance the p value for the signed in would appear lower and suggest that we are more confident in this Ho rejection but the sample size for the gender comparison is smaller (we had to throw out the samples that are not signed in becuase gender is unknown).
'''
#age=pd.cut(sin['Age'], [7, 18, 24, 34, 44, 54, 64, 1000])
sin['age_cat']=pd.cut(sin['Age'], [7, 18, 24, 34, 44, 54, 64, 1000], labels=['18-24', '24-34', '34-44', '44-54', '54-64', '64-1000', '7-18'])
#print(sin.head())
#`'(18, 24]', '(24, 34]', '(34, 44]', '(44, 54]', '(54, 64]', '(64, 1000]', '(7, 18]'`
print(sin.info())
age7_18=sin[sin['age_cat']=='7-18']
age18_24=sin[sin['age_cat']=='18-24']
age24_34=sin[sin['age_cat']=='24-34']
age34_44=sin[sin['age_cat']=='34-44']
age44_54=sin[sin['age_cat']=='44-54']
age64_1000=sin[sin['age_cat']=='64-1000']

labels=['18-24', '24-34', '34-44', '44-54', '54-64', '64-1000', '7-18']
comparison =pd.DataFrame()
list_grp=[age7_18, age18_24, age24_34, age34_44, age44_54, age64_1000]
for group in list_grp:
    # create a datafram with col = age group, difference of mean, pvalue for comparison, significant same or not same with pvalu
    scipy.stats.ttest_ind(male['CTR'], female['CTR'], equal_var=False)



print(age18_24.head())
