# -*- coding: utf-8 -*-
import numpy as np 

def q(i,grid):
	"""This function returns a candidate state given the state that the Markov chain is currently in. 

	Example
	-------
	n = (0,1,2)
	i = 1
	candidate = q(i)
	print(candidate)


	Parameters
	----------
	i : M x M array
		The current state of the Markov distribution (a gonnected graph).
	grid : M x 2 array
		x and y distance values for the vertices in the initial Markov state.

	Returns
	-------
	candidate : array
		candidate is the candidate state based on the decision calculus intrinsic to q."""
	
	i = np.array(i)
	grid = np.array(grid)
	candidate = i[:]
	rand_i = np.random.randint(len(i))
	rand_j = np.random.randint(len(i))

	while rand_i == rand_j: # or is_connected(rand_i,rand_j) == false: 
	    rand_i = np.random.randint(len(i))
	    rand_j = np.random.randint(len(i))

	    
	if candidate[rand_i,rand_j] != 0:
	    candidate[rand_i,rand_j] = 0
	    candidate[rand_j,rand_i] = 0

	    
	elif candidate[rand_j,rand_i] == 0:
	    weight_i_j = np.sqrt((grid[rand_i,0] - grid[rand_j,0])**2 + (grid[rand_i,1]-grid[rand_j,1])**2)
	    candidate[rand_i,rand_j] = weight_i_j
	    candidate[rand_j,rand_i] = weight_i_j

	return candidate


    



def theta(i,grid,r=1):
	"""This function calculates the value of theta for the given state. Theta is a function defined in the problem statement.

	Example
	-------

	i = [[1,0],[0,1]]
	weights = [[1,2],[3,4]]
	value = theta(i,weights)

	Parameters
	----------

	i : MxM array
		This is the current state represented in an MxM adjacency matrix.

	grid : Mx2 array
		This is the array of x and y values in Cartesian space for the given index/label (i.e. the individual column headers in the 'i array.')

	Output
	------

	value : integer
		This is the theta value for the given state."""

	total_weight = np.sum(np.array(i))

def dijkstra(i):
	"""An implementation of Dijkstra's shortest path algorithm. 
	Used pseudocode from http://www.gitta.info/Accessibiliti/en/html/Dijkstra_learningObject1.html."""
	import math
	dist = [0]
	previous = [0]
	for v in range(1,len(i),1):
	    dist.append(math.inf)
	    previous.append(0)

	Q = []
	for j in range(0,len(i),1):
	    Q.append(j)

	while len(Q) != 0:
	    dist_u = min(dist)
	    u = dist.index(min(dist))
	    Q.remove(u)
	    alt = 0
	    for v in Q:
	        alt = dist_u + i[u,v]
	        if alt < dist[v]:
	            dist[v] = alt
	            previous[v] = u
	return previous


def probability(i,j):
	"""This function computes the probability that the candidate state will be selected.

	Example
	-------

	i = [[1,0],[0,1]]
	j = [[0,1],[1,0]]
	prob = probability(i,j)

	Parameters
	----------

	i : MxM array
		This is the current graph represented by its adjacency matrix.

	j : MxM array
		This is the candidate graph represented by its adjacency matrix.

	Output
	------

	prob : float
		This is the probability that the candidate graph is selected. It takes values on [0,1]."""

def next_state(i,j,probability):
	""" This function returns the next state using functions already defined.

	Example
	-------

	state = next_state(2,3,.4)

	Parameters
	----------

	i : integer
		the current state
	
	j : integer
		the candidate state

	probability : float
		the probability that state j is selected

	Output 
	------

	state : integer
		the state chosen"""

def iterator(i,eq_distrib,N):
	"""This is the main body of the implemented algorithm. This ignores the burn-off at the beginning of the simulation.

	Example
	-------
	n = (0,1,2)
	eq_distrib = (.4,.5,.1)
	N = 1000
	i = 2
	X, P = iterator(i,eq_distrib,N)
	print(X)
	print(P)

	Parameters
	----------

	i : integer
		the first state of the particle

	eq_distrib : 1-D array
		the equilibrium probability distribution of the n states in the state space

	N : the number of iterations desired

	Output
	------

	X : array of integers
		the record of all the states the Markov chain took
	P : nxn array of floats
		the transition probability matrix.
		"""

	import numpy as np



