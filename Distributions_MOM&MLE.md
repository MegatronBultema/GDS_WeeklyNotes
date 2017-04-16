
Normal distribution
Bernoulli(p): probability that a single coin flip turns out to be heads
        PDF - p if x=1, 1-p if x=0

Binomial(n,p): (k)number of coin flips out of 100 that turn out to be heads
        PDF - choose(n,k) * p**k * (1-p)**(n-k) for 0<= k <=n

Geometric(p): (k) number of trials until coin flip turns out to be heads
        PDF - p(1-p)**(k-1) for k=1,2,...

Poisson(theta or lambda): (k) number of taxis passing a street corner in a given hour (on average pass 10/hour = theta)
        PDF - e**(-theata) * (theta**k)/k!

Exponential(theta or lambda): Time until taxi will pass street corner
        PDF - theta*e**(-theta*k) for k>=0 and theta>0

Uniform(a,b): Degrees between hour hand and minute hand
        PDF - 1/(b-a)

Normal or Gaussian(mu,stddev): normal distribution
        PDF - 1/(stddev * sqrt(2*pi)) * e**( k - (mu)**2/(2 * stddev**2)

Gamma:
The gamma distribution is widely used as a conjugate prior in Bayesian statistics. It is the conjugate prior for the precision (i.e. inverse of the variance) of a normal distribution. It is also the conjugate prior for the exponential distribution.

In a gamma distribution population context, the mean and variance are defined as $\mu = \alpha / \beta $ and $\sigma^2 = \alpha / \beta^2$ so we can't directly substitue sample statistics for population parameters; however, it is straight forward to show that the population parameters can be readily estimated by MOM as $\hat{\alpha} = \bar{x}^2 / s^2$ and $\hat{\beta} = \bar{x} / s^2$ where $\bar{x}$ is the sample mean and $s^2$ is the sample variance.


Examples:
What distribution would you use to model the following cases:
* What is the probability that the mean volume of 50 bottles is less than 500 ml?
	normal distribution
* Deciding to go for a run or not.
	binomial - multiple success fail trials
 	bernuli - one trial for success or failure for a single instance
* Determining how many days pass before you finally decide to go for a run.
	geometric
* Determining how likely it is that you go for 10 runs in a month.
	binomial
* Calculating how much water falls into an open swimming pool during a rain storm.
	gamma * add gamma to list
          (poisson - is discrete, exponential- time until)
* Assuming you run at a 9 minute mile pace avg pace, determining how likely it is that you pass the 3 mile mark in a race in 25 minutes?
	exponential - within 25 min
	poisson - at exactly 25 min
