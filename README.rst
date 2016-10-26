===============================
Markov Chain Monte Carlo 
===============================


.. image:: https://img.shields.io/travis/ukurumba/MCMC.svg
        :target: https://travis-ci.org/ukurumba/MCMC

.. image:: https://codecov.io/gh/ukurumba/MCMC/branch/master/graph/badge.svg
		:target: https://codecov.io/gh/ukurumba/MCMC


Uses Metropolis-Hastings algorithm and Markov Chain Monte Carlo method to estimate different network parameters.

This algorithm takes in a list of tuples (i.e. a list of cartesian coordinates) and generates graphs that represent different networks that could be formed, considering each tuple a node in the graph. The initial tuple is considered a special node, the '0' node that represents some sort of central hub.

Using an innate probability function and the Metropolis-Hastings algorithm for Markov Chain Monte Carlo, this program then generates candidate graphs, generating more likely candidate graphs more often. This sort of 'weighted' generation allows the program to calculate a set of network parameters. The following are parameters this function can calculate:

- Expected number of connections to the 0 node.
:: 
	grid = [(1,2),(3,4),(5,6)]
	MCMC.expected_connect_to_0(grid,1000,T=0.5)

- Expected number of total edges in a graph.
::

	grid = [(1,2),(3,4),(5,6)]
	MCMC.expected_number_edges(grid,1000,T=0.5)

- Expected path length of shortest path between 0 node and node furthest from 0 (i.e. longest 'shortest path' in the network)
::

	grid = [(1,2),(3,4),(5,6)]
	MCMC.expected_furthest_from_0(grid,1000,T=0.5)

- The most likely graphs given the innate probability distribution
::

	grid = [(1,2),(3,4),(5,6)]
	MCMC.most_likely_graphs(grid,0.01,1000,T=0.5)




Details
-------

* Free software: MIT license
* .. _Documentation: https://


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

