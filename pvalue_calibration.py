import scipy.stats
import random
import math
import matplotlib.pyplot as plt
random.seed(0)

N = 1000 # number of hypotheses to test
pi_0 = 0.5 # proportion of null hypotheses that are true
n_null = round(N*pi_0) # number of null hypotheses that are true
alternative = 0.2

def pvalue(mean=0, sigma=1, n=100):
	"""Generate random p-value for test of mean=0, given true mean
	mean and std dev sigma and sample of size n."""
	X = [random.normalvariate(mean, sigma) for _ in range(n)]
	Xbar = sum(X)/n
	T_X = math.sqrt(n)*abs(Xbar)/sigma
	return 2*(1-scipy.stats.norm.cdf(T_X))

p1 = [pvalue(0, 1, 100) for _ in range(n_null)]
p1_cat = [(i/10+0.03, len([1 for p in p1 if p >= i/10 and p < (i+1)/10]))
	for i in range(0, 10)]
p2 = [pvalue(alternative, 1, 100) for _ in range(N-n_null)]
p2_cat = [(i/10+0.06, len([1 for p in p2 if p >= i/10 and p < (i+1)/10]))
	for i in range(0, 10)]

x, freq = zip(*p1_cat)
plt.bar(x, freq, 0.03, label='Null hypothesis (mean=0)')
x, freq = zip(*p2_cat)
plt.bar(x, freq, 0.03, label='Alternative hypothesis (mean={})'.format(alternative))
plt.xticks([i/10 for i in range(0, 11)])
plt.xlabel('p-value')
plt.title('Distribution of p-values under null and alternative hypotheses')
plt.legend()
plt.show()

