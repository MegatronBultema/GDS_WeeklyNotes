## Miniquiz: Random Variable Class

**Include your code and answers in** `python_rv_class.py`.

Now that we have a PMF (from yesterday), we will create a random variable class.  
The (somewhat artificial) distinction between the two will be that the random variable class defines
a set of outcomes on a sample space, while the PMF is the actual mapping of outcome to probability.
In this vein a RV can be sampled from to collect a series of trials, while the PMF will represent the 
idealized/theoretical distribution of the RV.

<br>

1. Create a Random Variable class (`RV`) that represents a distribution of a possible set of outcomes. 
   It should have the following methods:
   
   - `sample()`: makes a draw from the RV and returns an outcome proportional to its distribution.  
     The draws should be independent (i.e. stateless)
   - `all_outcomes()`: enumerate every possible outcome
   - `pmf()`: returns the PMF of the random variable

2. The RV class should be instantiated with a PMF, i.e. you cannot create a random variable without a
   backing distribution.

   ```python
   from my_stats import PMF
    
   die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })
    
   die_rv = RV(die)
   
   die_rv.sample() #=> "3"
   die_rv.sample() #=> "2"
   die_rv.sample() #=> "6"
   die_rv.sample() #=> "3"
    
   die_rv.all_outcomes() #=> ["1", "2", "3", "4", "5", "6"]
    
   die_rv.pmf() #=> < PMF object ... >
   ```
