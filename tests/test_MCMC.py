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

from MCMC import MCMC



class TestMcmc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_initialization(self):
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
    	val = 0
    	if candidate[0,0] == 0 or candidate[1,0] == 0 or candidate[2,0]==0:
    		val = True 
    	else:
    		val = False 
    	self.assertTrue(val)


    # def test_candidate_connected(self):
    # 	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    # 	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    # 	States = np.array([0,1,2])
    # 	candidate = MCMC.q(Current_graph,grid)
    	

    def test_actual_change(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	candidate = MCMC.q(Current_graph,grid)
    	val = np.array_equal(Current_graph,candidate)
    	self.assertFalse(val)

    def test_theta(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	States = np.array([0,1,2])






tests = unittest.TestLoader().loadTestsFromTestCase(TestMcmc)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())


