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


def diag():
	globals().update(diag_covar)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	x = np.linspace(0.5,3.5,500)
	plt.plot(x, mlab.normpdf(x,approx_mean[ke_jie_id], approx_covar[ke_jie_id]**0.5), label = "Ke Jie")
	plt.plot(x,mlab.normpdf(x,approx_mean[lee_sedol_id], approx_covar[lee_sedol_id]**0.5), label = "Lee Sedol")
	plt.plot(x,mlab.normpdf(x,approx_mean[alpha_go_id], approx_covar[alpha_go_id]**0.5), label = "Alpha Go")
	ax.set_xlabel("Skill")
	ax.set_ylabel("Probability")
	ax.legend()
	fig.tight_layout()
	plt.show()
	return fig
def full():
	globals().update(full_covar)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	x = np.linspace(0.5,5,500)
	# The marginal distribution of a gaussian is just the gaussian 
	plt.plot(x, mlab.normpdf(x,approx_mean[ke_jie_id], approx_covar[ke_jie_id][ke_jie_id]**0.5), label = "Ke Jie")
	plt.plot(x,mlab.normpdf(x,approx_mean[lee_sedol_id], approx_covar[lee_sedol_id][lee_sedol_id]**0.5), label = "Lee Sedol")
	plt.plot(x,mlab.normpdf(x,approx_mean[alpha_go_id], approx_covar[alpha_go_id][alpha_go_id]**0.5), label = "Alpha Go")
	ax.set_xlabel("Skill")
	ax.set_ylabel("Probability")
	ax.legend()
	fig.tight_layout()
	plt.show()
	return fig
