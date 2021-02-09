# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import scipy.integrate as integrate
import scipy.special as special

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(5), 120)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(2,1,-1), (0.5,-1))
        self.assertEqual(utils.roots(4,2,-2), (0.5,-1))
        pass
    
    def test_integrate(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
