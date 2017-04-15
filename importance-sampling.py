### IMPORTANCE SAMPLING DEMO ###

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## fill in later and actually implement

#So, importance sampling is a method of sampling to calculate averages and expectations of intractable distributions. typically it is used when we can evaluate a distribution only up to a normalisation constant - i.e we know p*(x), but not p(x) where p(x) = p*(x)/Z.

#We instead sample from a distribution we know we can sample from which covers the distribution we want to compute the normalisation of, and then reweight each sample so that they are of the same size they would have been had we actually been sampling from the intractable posterior. With these samples wecan then compute the monte-carlo approximation of the expectation.
	#well, hang on a minute here, this is straight up not working, because we need to compute the q(x) which in a uniform will be pretty negligible overall cmopared to a point in a gaussian, right? or am I just silly.? because the uniform depends entirely on the region while the gaussian does not seem to and seems to be able to produce point probabilities which are not zero, which is obviously wrong, so I'm really not sure what the difference is here - I must be misunderstanding something, but what? # nope, this is just me not understanding how probaility densities work, now I read about it it makes much more sense, and the uniform is exactly what I expect it to be!

class Uniform_distribution:
#this will be our hyper naive Q
	# I'm actually using OOP lol!
	def __init__(a,b):
		self.a = a	#start point
		self.b = b 	#end point

	def get_P(x):
		return 1/(b-a)

	def sample():
		return np.random.uniform(self.a, self.b)



def unnormalised_gaussian(x,params):
	#our unnormalised gaussian we are computing the expectation of the normalised gaussian imho
	mu = params[0]
	sigma = params[1]
	return np.exp(-(x-mu)**2/np.sqrt(sigma))


def importance_sampler(N, p_dist, p_params, q_dist, q_params, f = np.identity):
	# will return the samples, will return the average calcualted from the samples
	#where f is a function on the distribution we're taking the expectation of - this idea really isn't still not that clearto me tbh, but hey. the default is identity
	samples = []
	weights = []
	q = q_dist(q_params)	#initialise our Q - which must be a class while the other must be a function, because who needs sane interfaces, right?
	for i in xrange(N):
		x = q.sample()	#sample from q
		w = p_dist(x, p_params)/q.get_P(x)	#calculate unnormalised weights
		samples.append(f(x))
		weights.append(w)
	Zw = 1/sum(weights)	#calculate normalisation constant for weights
	weights = map(lambda x: x*Zw, weights)	#normalise the weights
	expectation = np.dot(samples, weights)	#calculate the expectation
	return expectation, samples, weights	#return
		

def resampler(weights):
	#get a discrete distribution over the indices of the weights in the weight vector
	indicies = np.arrange(len(weights))
	discrete = stats.rv.discrete(values = (indices, weights))
	#get N samples from our new formed discrete distribution
	weight_samples = discrete.rvs(size=N)
	norm = 1/len(weights)	#the normalisation constant is really easy here
	weight_samples = map(lambda x: x*norm, weight_samples)	#normalise the weight_samples distribution
	return weight_samples


gauss_params = [5,3]
q = Uniform_distribution(0,10)
N = 10000

expectation, samples, weights = importance_sampler(N, unnormalised_gaussian, gaus_params, q)
print expectation

print "Resampling!"

weight_samples = resampler(weights)
resampled_E = np.dot(samples, weight_samples)
print resampled_E

		
	




