from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from scipy.stats import norm


def dump(name,f):
    with open(fname+name, "wb") as output_file:
        pickle.dump(f,output_file)
        
def load(name):
    with open(fname+name, "rb") as input_file:
        data = pickle.load(input_file)
        return data

def savefig(fig,fname):
	base = "/afs/inf.ed.ac.uk/user/s16/s1686853/pmr/"
	fig.savefig(base + fname)
    


full_covar = np.load("full_covar.npz")
diag_covar = np.load("diag_covar.npz")


def predictive_probabilities():
	#for the full covariance
	globals().update(full_covar)
	#set up our x* vector:
	x = np.zeros([n_players,1])
	x[alpha_go_id] = 1/math.sqrt(skill_prior_var)
	x[ke_jie_id] = -1/math.sqrt(skill_prior_var)

	print x.T.shape
	print x.shape
	print approx_covar.shape
	numerator = np.dot(approx_mean.T, x)
	denom = np.dot(np.dot(x.T, approx_covar), x) +1
	denom = np.sqrt(denom)
	frac = numerator/denom
	full_prob = norm.cdf(frac)
	print full_prob
	
	#for the diagonal covariance
	globals().update(diag_covar)
	#set up our x* vector:
	x = np.zeros([n_players,1])
	x[alpha_go_id] = 1/math.sqrt(skill_prior_var)
	x[ke_jie_id] = -1/math.sqrt(skill_prior_var)
	
	#create the diagonal matrix
	#diag = np.zeros([n_players, n_players])
	diag = np.diag(approx_covar)

	#calculate the probability
	numerator = np.dot(approx_mean.T, x)
	denom = np.dot(np.dot(x.T, diag), x) +1
	denom = np.sqrt(denom)
	frac = numerator/denom
	diag_prob = norm.cdf(frac)
	print diag_prob
	return full_prob, diag_prob

