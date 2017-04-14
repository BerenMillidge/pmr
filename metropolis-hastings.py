### METROPOLIS HASTINGS SAMPLING DEMO ###


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#So yeah, MH MCMC. So the actual algorithm intuitively is pretty simple. We have a p*(X) which we know and we just want the normalisation constant, this is the standard thing in bayesian inference. So what we do is we have a proposal function q(x|x^-1) which is a markov chain effectively. this is usually a simple gaussian of form N(x; x^1, sigma) i.e. a normal based on the previous step, and we propose locations in the posterior by simply sampling from this distribution. Then we need to decide whether we move. we do this quite simply by evaluating the current position against the proposal. The probability of moving is the ratio of the probability density at the proposed position vs the probability mass at the currnet position. This gives it a bias to move as even when the probability mass at the proposed position is lower there is still a chance of moving there, but when it is higher you always move there
#there is some complicated maths proving that this thing satisfies detailed balance, and thus the stationary distribution of q(x'|x) is p(x) and I should learn that properly. the actual detaild functoin is pretty easy though so  Ishould implement it to try to get some understanding

def unnormalised_gaussian(x,mu,sigma):
	#un-normalised gaussian which we want to compute the normalisation constant of via MHMCMC
	return np.exp(-(x-mu)**2/np.sqrt(sigma))

def MH_sampler(N, q_sigma, params, distribution = unnormalised_gaussian):
	#init our markov chain q
	current = np.random.normal(0,3)
	samples = []
	for i in xrange(N):	#start our sample loop
		proposal = np.random.normal(current, q_sigma) #get proposal
		# get probability ratio
		p_ratio = distribution(proposal, params)/distrbution(current, params)	
		#get probability of acceptance
		p_accept = min([1, p_ratio])
		#determine whether to accept or reject
		rand = np.random.uniform()
		#When we accept
		if rand <=accept:
			samples.append(proposal)	#we've got a sample!
			current = proposal	#we've now moved to the proposal
	return samples
	#wow, this was actually really straightforward to implement. obviously it's  dumb implementation, but MH is really not so bad after all. It's all beginning to click, which is really nice!
			
