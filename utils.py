# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt
import scipy.special as special
import scipy.integrate as integratee
from scipy.integrate import quad

def fact(n):
    factorial = 1
    if n < 0:  
        return ValueError
    elif n == 0:  
        return 1  
    else:  
        for i in range(1,n + 1):  
            factorial = factorial*i  
        return factorial
    pass

def roots(a, b, c):
    if (a**2-4*b*c<0):
            return (Nothing)
    if (a**2-4*b*c==0):
        return (-b/a)
    if (a**2-4*b*c>0):
        return ((-b**2+sqrt(a**2-4*b*c))/(2*a), (-b**2-sqrt(a**2-4*b*c))/(2*a))
    pass

def integrate(function, lower, upper):
    result = integratee.quad(lambda x: eval(function), lower, upper)
    return (result)
    pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
