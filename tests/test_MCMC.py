#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_MCMC
----------------------------------

Tests for `MCMC` module.
"""


import sys
import unittest
import numpy as np
import networkx as nx

from MCMC import MCMC



class TestMcmc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_initialization(self):
        #verifies that the initial graph is symmetric
    	grid = [[1,2],[1,9],[5,9],[2,3]]
    	init_graph = MCMC.initialization(grid)
    	val = np.allclose(init_graph,np.transpose(init_graph))
    	self.assertTrue(val)


    def test_candidate_symmetry(self):
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	init_graph = MCMC.initialization(grid)
    	for i in range(0,10,1):
    		candidate = MCMC.q(init_graph,grid)
    	val = np.allclose(candidate, np.transpose(candidate))
    	self.assertTrue(val)

    def test_remove_link(self):
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	graph = [[0,1,1],[1,0,1],[1,1,0]]
    	candidate = MCMC.q(graph, grid)
    	val = False
    	if candidate[0,0] == 0 or candidate[1,0] == 0 or candidate[2,0]==0:
    		val = True 
    	self.assertTrue(val)  	

    def test_actual_change(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	candidate = MCMC.q(Current_graph,grid)
    	val = np.array_equal(Current_graph,candidate)
    	self.assertFalse(val)

    def test_theta(self):
        Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
        prob = MCMC.theta(Current_graph)
        self.assertEqual(prob,6)

    def test_probability(self):
        i = np.array([[0,1,1],[1,0,0],[1,0,0]])
        j = np.array([[0,1,1],[1,0,1],[1,1,0]])
        self.assertEqual((1/3)/(np.exp(2.0)),MCMC.probability(i,j))
        self.assertEqual(1.0,MCMC.probability(j,i))

    def test_state_generator(self):
        i = np.array([[0,1,1],[1,0,0],[1,0,0]])
        j = np.array([[0,1,1],[1,0,1],[1,1,0]])
        for val in range(0,50):
            next_state = MCMC.next_state(i,j,MCMC.probability(i,j))
            next_state = MCMC.next_state(i,j,MCMC.probability(i,j))
            next_state = MCMC.next_state(i,j,MCMC.probability(i,j))
            next_state = MCMC.next_state(i,j,MCMC.probability(i,j))
            if np.allclose(next_state,j == True): 
                break 
        if np.allclose(i,next_state) or np.allclose(j,next_state) == True:
            value = True
        self.assertTrue(value)

    def test_expected_edges(self):
        grid = [(1,3),(4,5),(3,6),(3,9)]
        val = MCMC.expected_number_edges(grid,25)
        self.assertIsInstance(val, float)

    def test_expected_connections_to_0(self):
        grid = [(1,3),(4,5),(3,6),(3,9)]
        val_2 = MCMC.expected_connect_to_0(grid,25)
        self.assertIsInstance(val_2, float)

    def test_longest_path(self):
        grid = [(1,3),(4,5),(3,6),(3,9)]
        val_2 = MCMC.expected_furthest_from_0(grid,25)
        self.assertIsInstance(val_2,float)

    def test_graphs_returned(self):
        grid = [(1,3),(4,5),(3,6),(3,9),(12,13),(18,27),(48,32),(2,14),(58,36)]
        graph = MCMC.most_likely_graphs(grid,.01,25)
        nx_graph = nx.from_numpy_matrix(graph[0])
        connectedness = nx.is_connected(nx_graph)
        symmetry = np.allclose(graph[0],np.transpose(graph[0]))
        self.assertTrue(connectedness)
        self.assertTrue(symmetry)


        











tests = unittest.TestLoader().loadTestsFromTestCase(TestMcmc)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())


