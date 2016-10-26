=====
Usage
=====

To use MCMC in a project::

    import networkx as nx
    import numpy as np
    import MCMC


Available Functions
-------------------

-Expected connections to 0:
::
	grid = [(1,2),(3,4),(5,6)]
	help(MCMC.expected_connect_to_0)

	""" This function returns the arithmetic mean number of edges that are connected to the 0 node given an input grid. This should 
    approximate the expected number of edges of this type quite well if N is large.
    Example
    -------

    grid = [(12,17),(13,19),(34,69),(34,12)]
    number_edges = MCMC.expected_connect_to_0(grid,1000)

    Parameters
    ----------

    grid : list of tuples
      the x and y coordinates of all the different nodes in the graph. The 1st entry should be the all-important "0" node, while
      the rest of them can be in any arbitrary order.

    N : int
        the number of iterations desired.

    T : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    r : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    Output
    ------
    
    number_edges : float
    The expected number of edges that connect to the 0 node."""

- Expected number of total edges in a graph.
::

	help(MCMC.expected_number_edges)
	""" This function returns the arithmetic mean number of edges in the graph. This should 
    approximate the expected number of edges of this type quite well if N is large.
    Example
    -------

    grid = [(12,17),(13,19),(34,69),(34,12)]
    number_edges = MCMC.expected_number_edges(grid,1000)

    Parameters
    ----------

    grid : list of tuples
      the x and y coordinates of all the different nodes in the graph. The 1st entry should be the all-important "0" node, while
      the rest of them can be in any arbitrary order.

    N : int
        the number of iterations desired.

    T : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    r : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.


    Output
    ------
    
    number_edges : float
    The expected number of edges in a graph."""


- Expected path length of shortest path between 0 node and node furthest from 0 (i.e. longest 'shortest path' in the network):
::

	help(MCMC.expected_furthest_from_0)
	"""This function returns the arithmetic mean number of edges between the 0 node and the node that is the furthest from 0. 
    This should approximate the actual expected number of edges in this path as N gets large.

    Example
    -------

    grid = [(12,17),(13,19),(34,69),(34,12)]
    number_edges = MCMC.expected_furthest_from_0(grid,1000)

    Parameters
    ----------

    grid : list of tuples
        the x and y coordinates of all the different nodes in the graph. The 1st entry should be the all-important "0" node, while
        the rest of them can be in any arbitrary order.

    N : int
        the number of iterations desired.

    T : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    r : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    Output
    ------

    number_edges : float
    The expected number of edges in the shortest path between 0 and the vertex furthest from 0."""

- The most likely graphs given the innate probability distribution:
::

	help(MCMC.most_likely_graphs)
	"""This function returns the most likely graphs ordered from most to least. The amount of returned graphs depends on the input percentage.
    Example
    -------

    grid = [(12,17),(13,19),(34,69),(34,12)]
    graphs = MCMC.most_likely_graphs(grid,.01,1000)

    Parameters
    ----------

    grid : list of tuples
      the x and y coordinates of all the different nodes in the graph. The 1st entry should be the all-important "0" node, while
      the rest of them can be in any arbitrary order.

    percentage : float
        the percentage of different graphs travelled that you would like returned. e.g. .01 returns the 1% of most likely graphs.

    N : int
        the number of iterations desired.

    T : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    r : float (optional)
        adjustable parameter to improve specificity of intrinsic probability distribution.

    Output
    ------

    graphs : list
        a list of most likely graphs ordered from most to least likely (of the top given percentage of course). Each graph is
        itself a list."""
	



