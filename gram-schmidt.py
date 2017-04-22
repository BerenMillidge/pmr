# This is just some quick code to imlement the gram-schmidt orthogonalisatoin procedure in vector form. in matrix form it is effectively equal to the QR decomposition. It can also be used to determine the rank of a matrix form from the columns of the independent vectors given to it, which we will implement and possibly plot

from __future__ import division
import numpy as np

matrix = []

def euclid_norm(vect):
	vec_sum = 0
	for x in vect:
		vec_sum += x**2
	return np.sqrt(vec_sum)

def gram_schmidt(matrix)
	mat = matrix.T
	qs = []
	a_sum = 0
	for i in xrange(len(mat)):
		q = mat[i] - 
