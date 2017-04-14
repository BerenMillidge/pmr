###GIBBS SAMPLING SIMPLE DEMO###

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#so here we implement gibbs sampling of a simple bivariate gaussian. It should be quite simple really. Gibbs sampling iteratively updates the conditional distributionsfor each variable given all other variables. This can be thought of as a markov chain of form q(x^i+1 | x^i). It satisfies detailed balance and is thus ergodic with a stationary distibution of p(x) under ideal conditions. The updates/samples are not at all dependent however, so many samples are typically needed. Also, despite the ergodicity, initial conditions can have a big effect, thus meaning that for complicated high-dimensional distributions, a burn-in period is often useful. If the density is not contiguous so there is no path from one mode to another, then gibbs samplingwill notexplore that mode unless initialised there. This is a flaw common to all MCMC variants except hamiltonian MCMC.

#We first define our distribution - a bivariate gaussian

mu = [1,2]
sigma = [[3,1],[1,5]]

#We define our conditional distributions. These come from the fact that the conditional of a gaussian is a gaussian.

#We should rewrite these to be significantly more general if we are to write this up in a proper manner

def mu1cond(y2, mu, sigma):
	return mu[0] + np.linalg.inv(np.dot(sigma[0][0], sigma[0][1]))* (y2 - mu[1])

def mu2cond(y1, mu,sigma):
	return mu[1] + np.linalg.inv(np.dot(sigma[1][0], sigma[1][1]))* (y1 - mu[0])

def sigma1cond(sigma):
	return sigma[0][0] - np.dot(np.dot(sigma[0][1], np.linalg.inv(sigma[1][1])), sigma[1][0])

def sigma2cond(sigma):
	return sigma[1][0] - np.dot(np.dot(sigma[1][1], np.linalg.inv(sigma[0][1])), sigma[0][0])

def Gibbs_sampler(N, mu, sigma):
	samples = []
	samples_x = []
	samples_y = []
	#Init our parameters
	y1, y2 = np.random.multivariate_normal([0,0], [[1,0],[0,1]])
	samples_x.append(y1)
	samples_y.append(y2)
	sigma1 = sigma1cond(sigma)
	sigma2 = sigma2cond(sigma)
	for i in xrange(N):	#start the sample loop
		mu1 = mu1cond(y2,mu,sigma)
		y1 = np.random.normal(mu1, sigma1)
		mu2 = mu2cond(y1, mu,sigma)
		y2 = np.random.normal(mu2, sigma2)
		samples_x.append(y1)
		samples_y.append(y2)
	return samples_x, samples_y



N = 1000
x, y = Gibbs_sampler(N, mu, sigma)
plt.plot(x,y)
plt.show()
		
	
