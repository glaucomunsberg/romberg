from numpy 	import *
from math 	import *
from PrettyTable import *
import sys
sys.setrecursionlimit(10000)
# a é igual a 0
a = 0
# b é igual a 20
b = 20
table = PrettyTable()
# o numero de iterações que ela pede no problema é 8
iterations = range(1,8)
table.field_names = ['Interation','k','j','value']

def romberg():

	a=0
	for k in iterations:
		for j in iterations:
			# Colunas sem arredondamento
			#table.add_row([a,k,j, Rkj(k,j)])
			
			# Colunas com arredontamento tipo 1
			
			table.add_row([a,k,j, round(Rkj(k,j),5) ])
			
			# Colunas com arredontamento tipo 2			
			#table.add_row([a,k,j, '%.3f' %round(Rkj(k,j),5)])
			
			a+=1
	print table

# Função base para resolver o problema.
# -1.47206x10^-7x^10+0.0000148524x^9-0.000642464x^8+0.0155672x^7-0.231584x^6+2.17898x^5-12.861x^4+45.434x^3-85.9344x^2+65.5502x 

def function(x):
	
	return -1.47206*(10**-7)*(x**10)+0.0000148524*(x**9)-0.000642464*(x**8)+0.0155672*(x**7)-0.231584*(x**6)+2.17898*(x**5)-12.861*(x**4)+45.434*(x**3)-85.9344*(x**2)+65.5502*(x)

def h_of_k(k):

	return (a-b)/2**(k-1)

def R11():

	return ( (b-a) / 2 ) * ( function(a) + function(b) )

def Rk1(k,j):

	if k == 1:
		# Nunca vai cair nesse caso. O if do RKJ assegura isso.
		return R11()
	
	else:
		
		#faz o somatorio de 1 até 2**(k-2) com a função abaixo.
		#Não tem a necessidade de usar range.
				
		i=1
		
		for i in 2**(k-2):
			
			totalSomatorio += function( a+(2*i-1)*h_of_k(k) )
		
		return (1 / 2 ) * ( Rk1(k-1,1) + h_of_k(k-1) * totalSomatorio )

def Rkj(k,j):

	if k == 1 and j == 1:
		return R11()
	elif j == 1:
		return Rk1(k,j)
	else:
		return ( Rkj(k,j-1) + (((Rkj(k,j-1) - Rkj(k-1,j-1) )) / (4**(j-1)-1)) ) 
