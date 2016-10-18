#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_MCMC
----------------------------------

Tests for `MCMC` module.
"""


import sys
import unittest

from MCMC import MCMC



class TestMcmc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_candidate_generator(self):
    	def test_q(i):
    		return 3*i + 12
    	candidate = MCMC.q(test_q,2)
    	self.assertEqual(candidate,18)

    # def test_alpha_actually_minimizes(self):
    # 	eq_distrib = [.2,.3,.2,.7]
    	
    # 	probability = MCMC




tests = unittest.TestLoader().loadTestsFromTestCase(TestMcmc)
unittest.TextTestRunner().run(tests)
        


if __name__ == '__main__':
    sys.exit(unittest.main())


