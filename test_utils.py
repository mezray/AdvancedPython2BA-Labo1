# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import scipy.integrate as integrate
import scipy.special as special

class TestUtils(unittest.TestCase):
    def test_fact(self):
        
        pass
    
    def test_roots(self):
        if (a**2-4*b*c<0):
            return (Nothing)
        if a**2-4*b*c==0:
            return (-b/a)
        if (a**2-4*b*c>0):
            return ((-b**2+sqrt(a**2-4*b*c))/(2*a), (-b**2-sqrt(a**2-4*b*c))/(2*a))
        pass
    
    def test_integrate(self):
        result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
        return (result)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())