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

    def test_candidate_symmetry(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	candidate = MCMC.q(Current_graph,grid)
    	val = np.allclose(candidate, np.transpose(candidate))
    	self.assertTrue(val)

    # def test_candidate_connected(self):
    # 	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    # 	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    # 	States = np.array([0,1,2])
    # 	candidate = MCMC.q(Current_graph,grid)
    	

    def test_actual_change(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	grid = [[1.0,4.0],[3.0,7.0],[14.0,28.0]]
    	candidate = MCMC.q(Current_graph)
    	np.assertNotEqual(candidate-Current_graph,np.zeroes((3,3)))

    def test_theta(self):
    	Current_graph = [[0,1,1],[1,0,0],[1,0,0]]
    	States = np.array([0,1,2])






tests = unittest.TestLoader().loadTestsFromTestCase(TestMcmc)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())


