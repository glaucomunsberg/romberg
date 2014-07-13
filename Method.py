from numpy 	import *
from math 	import *
a = 0
b = pi
k = range(9)

def function(x):
	return sin(x) 

def h_of_k(k):
	return (a-b)/2**(k-1)

def rules_of_trapezoid():
	return (h_of_k(1)/2)*( function(a) + function(b) )

def trapezoid_again(left,right):
	return (h_of_k(right) / 2 ) * ( rules_of_trapezoid() + h_of_k(right) * function(a+(right*left)-1*h_of_k(left) )
