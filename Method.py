from numpy 	import *
from math 	import *
from PrettyTable import *
import sys
sys.setrecursionlimit(10000)
a = 0
b = pi
table = PrettyTable()
iterations = range(9)
table.field_names = ['Interation','k','j','value']

def romberg():

	a=0
	for k in iterations:
		for j in iterations:
			table.add_row([a,k,j, Rkj(k,j)])
			a+=1
	print table

def function(x):

	return sin(x) 

def h_of_k(k):

	return (a-b)/2**(k-1)

def R11():

	return ( (b-a) / 2 ) * ( function(a) + function(b) )

def Rk1(k,j):

	if k == 1:
		return R11()
	
	else:
		
		somatorio = range( 1, 2**(k-2) )
		totalSomatorio = 0

		for i in somatorio:
			total += function( a+(2*i-1) * h_of_k(k) )

		return (1 / 2 ) * ( Rk1(k-1,1) + h_of_k(k-1) * totalSomatorio )

def Rkj(k,j):

	if k == 1 and j == 1:
		return R11()
	elif j == 1:
		return Rk1(k,j)
	else:
		return ( Rkj(k,j-1) + (Rkj(k,j-1) - Rkj(k-1,j-1) )* (4**(j-1)-1) ) 