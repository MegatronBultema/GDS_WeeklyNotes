'''Taken from power-bayes/individual_solns.md'''
import math
def calc_power(data, null_mean, ci=0.95):
    '''Inputs:
            data - an array of values, in this example a list of weight of coke bottles
            null_mean - the expected value being tested in the null
        Return: power of this test
        Example do coke bottles on average weigh 20.4 oz.
        H0: mu = 20.4
        H1: mu != 20.4
        data - list of coke bottle weights
        null_mean - 20.4


    '''
   m = data.mean()
   se = standard_error(data)
   z1 = scs.norm(null_mean, se).ppf(ci + (1 - ci) / 2)
   z2 = scs.norm(null_mean, se).ppf((1 - ci) / 2)
   return 1 - scs.norm(data.mean(), se).cdf(z1) + scs.norm(data.mean(), se).cdf(z2)


def explore_power(data, null_mean, ci=0.95):

   # Calculate the mean, se and me-(4 std)
   data_mean = np.mean(data)
   data_se = np.std(data, ddof=1) / np.sqrt(len(data))

   # Create a normal distribution based on mean and se
   null_norm = scs.norm(null_mean, data_se)
   data_norm = scs.norm(data_mean, data_se)

   # Calculate the rejection values (X*)
   reject_low = null_norm.ppf((1 - ci) / 2)
   reject_high = null_norm.ppf(ci + (1 - ci) / 2)

   # Calculate power
   power_lower = data_norm.cdf(reject_low)
   power_higher = 1 - data_norm.cdf(reject_high)
   power = (power_lower + power_higher) * 100
   return power

'''
General commands for power calculation
'''





def calc_min_sample_size(a1, a2, eff_size, alpha=0.05, two_tail=True, power=0.8):
    '''Calculate the minimum sample size needed in a CTR study for a power of 0.8
    Inputs:
        Data from piolt study
        a1 - list of 1 (conversion) or 0 (no conversion) of visitors of site 1
        a2 - list of 1 (conversion) or 0 (no conversion) of visitors of site 2
    Return:
        minimum number of samples needed to gain desired power (0.80 default)
    '''
   av1 = np.mean(a1)
   av2 = np.mean(a2)
   n1 = len(a1)
   n2 = len(a2)
   p = (av1 * n1 + av2 * n2)/(n1 + n2)
   sem = np.sqrt(p * (1-p) / n1 + p * (1-p)/ n2)
   pdiff = abs(av2 - av1)

   beta = 1-power
   if two_tail:
      alpha = alpha/2
   if pdiff >= eff_size:
      b = scs.norm(pdiff, sem).ppf(beta) + pdiff
      z_sem = b - eff_size
      z = scs.norm().ppf(1-alpha)
   else:
      b = scs.norm(pdiff, sem).ppf(1-beta) + pdiff
      z_sem = eff_size - b
      z = scs.norm().ppf(alpha)
   sem_des = z_sem / z
   n_des = (p * (1-p) / sem_des) ** 2
   return int(math.ceil(n_des))

print calc_min_sample_size(old_data, new_data, 0.001) # We want to be able to detect a 0.001 difference
# Need to select a sample of 76827
