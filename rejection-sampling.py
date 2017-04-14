####REJECTION SAMPLING DEMO###

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#Rejection sampling allows us to sample from any density whether un-normalised or not or valid distribution or not simply if we know that density's shape. Typically this can be used to sample from a distribution which is known only up to a normalisation constant, as happens a lot in bayesian statistics with intractable posterior normalisation integrals required. If we can sample from them, we can use these samples to obtain a monte-carlo estimate of the value of the integral.

# Problems with rejection sampling is that it simply does not scale well to high dimensions as the volume of space covered by the approximating density relative to the true density will typically increase exponentially with dimensions, thus leading to a plummeting acceptance rate and a really slow sampling speed. This is why MCMC methods must be used instead, even though rejection sampling produces independent samples so many fewer are necessary than in MCMC sampling under ideal conditions.

#In this demo I use a simple uniform box covering the distribution. Smarter ways are possible if you know anything about the distribution you want to approximate, you can often define a covering distribution closer to it, which will mean a much higher acceptance rate and faster convergence.


def univariate_gaussian(x, params):
	#this gaussian is unnormalised, to prove that we can sample from completely un-normalised and non-valid "distributions" if we please via rejection sampling
	mu = params[0]
	sigma = params[1]
	return np.exp(-(x-mu)**2/np.sqrt(sigma))

#def crazy_density(x, params):
		#this plots a piecewise linear function density which is not valid at all, but still can be sampled from by rejection sampling
		#start = params[0]
		#stop = params[1]
		#slope = params[2]
		#stop2 = params[3]
		#slope2 = params[4]
		#if x == stop:
		#	return 0
		#if x < start:
			#return 0
		#if x < stop and x > start:
		#	return slope*(x-start)
		#if x > stop and x < stop2:
		#	return slope2*(x-start)
		#if x > stop2:
		#	return 0

def cubic_density(x,params):
	#also a completely invalid cubic density
	a = params[0]
	b = params[1]
	c = params[2]
	d = params[3]
	return a*(x**3) + b*(x**2) + c*x + d


def rejection_sample(M,P, N, distribution = univariate_gaussian, dist_params = [0,1]):
	samples = []	#hold our sample list
	rejections = 0
	acceptances = 0
	for i in xrange(N):
		width = np.random.uniform()	#sample from a U(0,1) distribution
		width = (width*2*P) - P	#rescale our width to match the width we actually want to sample from
		height = np.random.uniform()	#sample height from U(0,1) distribution
		height = height * M		#scale our height as desired
		pheight = distribution(width, dist_params)	#the height of the distribution up to normalisation constant we can calculate
		#print height, pheight
		if height <= pheight:		#accept if height <=pheight
			samples.append(width)	#we don't care about height, only width. i.e. we're noly sampling in x dimension, as y dimension is probability of getting that x
			acceptances +=1
		if height > pheight:
			rejections +=1
	rejection_rate = rejections/(rejections+acceptances) * 100	#calculate our rejection rate here
	return samples, rejection_rate


def plot_samples_histogram(samples, bins):
	plt.hist(samples, bins, normed = 1, facecolor = "blue")
	plt.xlabel("x")
	plt.ylabel("Probability")
	plt.title("Estimated distribution based on rejection sampling")
	plt.show()


def plot_distribution(distribution = univariate_gaussian, params = [0,1]):
	x = np.linspace(-5,5,100)
	vals = []
	for xs in x:
		vals.append(distribution(x,params))
	plt.plot(vals)
	plt.show()


M = 1	#Our constant bounding the size of the sampling box upwards
P = 10	#Our constant bounding the width of the sampling box
N = 50000	#the number of sampling runs you want to run


gauss_params = [1,10]	#the paramaters for our known distribution to be sampled from
crazy_params = [-4, -1,1000,4,100]
cubic_params = [0.5, 1, -2,-3]

#plot_distribution(univariate_gaussian, [0,2])
#plot_distribution(cubic_density, cubic_params)


print "Sampling from Un-normalised gaussian"
samples, rejection_rate = rejection_sample(M,P,N, univariate_gaussian, gauss_params)
print "Rejection Rate = " + str(rejection_rate)
bins = 100
plot_samples_histogram(samples, bins)

#print "Sampling from Illegal piecewise linear crazy density"
#samples, rejection_rate = rejection_sample(M,P,N, crazy_density, crazy_params)
#print "Rejection Rate = " + str(rejection_rate)
#bins = 100
#plot_samples_histogram(samples, bins)


#print "Sampling from cubic density"
#samples, rejection_rate = rejection_sample(M,P,N, cubic_density, cubic_params)
#print "Rejection Rate = " + str(rejection_rate)
#bins = 100
#plot_samples_histogram(samples, bins)


