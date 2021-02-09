# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt
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
    if ((b**2)-4*a*c<0):
            return (Nothing)
    if ((b**2)-4*a*c==0):
        return (-b/2*a)
    if ((b**2)-4*a*c>0):
        return ((((-b)+sqrt((b**2)-4*a*c)))/(2*a), (((-b)-sqrt((b**2-4*a*c)))/(2*a)))
    pass

def integrate(function, lower, upper):
    return integratee.quad(lambda x: eval(function), lower, upper)
    pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(4, 2, -2))
	print(integrate('x ** 2 ', 0, 3))