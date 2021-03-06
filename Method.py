from numpy 	import *
from math 	import *
from PrettyTable import *
from scipy import integrate
from scipy import interpolate
from scipy.special import erf
import sys
sys.setrecursionlimit(10000)
class bcolors:
    HEADER = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# a e igual a 0
a = 0
# b e igual a 20
b = 20
table = PrettyTable()
# o numero de iteracoes que ela pede no problema e 8
iterations = range(1,9)
matrix = [[-1 for x in range(1,9)] for x in xrange(1,9)] 
table.field_names = ['','1','2','3','4','5','6','7','8']

def rombergRecursive():

	for k in iterations:

		interate = range(1,k+1)
		for j in interate:

			print "POS[",k,",",j,"]"
			R(k,j)
			
	for i in iterations:
		table.add_row([i,matrix[i-1][0],matrix[i-1][1],matrix[i-1][2],matrix[i-1][3],matrix[i-1][4],matrix[i-1][5],matrix[i-1][6],matrix[i-1][7]])
	print table

def function(x):
	
	x = [0,2,4,6,8,10,12,14,16,18,20]
	y = [0,1.8,2,4,4,6,4,3.6,3.4,2.8,0]
	print interpolate.lagrange(x,y)
	return 0
	
def h_of_k(k):

	return (a-b)/2**(k-1)

def R11(k,j):
	if matrix[k-1][j-1] == -1:
		matrix[k][j] = ( (b-a) / 2 ) * ( function(a) + function(b) )

	return matrix[k-1][j-1]

def Rk1(k,j):

	if matrix[k-1][j-1] != -1:
		print "RK1[",k,",",j,"]",matrix[k-1][j-1]
		return matrix[k-1][j-1]
	else:
		if k == 1:
			# Nunca vai cair nesse caso. O if do RKJ assegura isso.
			return R11(k,j)
		
		else:
			totalSomatorio = 0
			#faz o somatorio de 1 ate 2**(k-2) com a funcao abaixo.
			#Nao tem a necessidade de usar range.
					
			rang = range(1, int(2**(k-2)))
			
			for i in rang:
				totalSomatorio += function( a+(2*i-1)*h_of_k(k) )
			
			matrix[k-1][j-1] = (1 / 2 ) * ( matrix[k-2][1] + h_of_k(k-1) * totalSomatorio )
			print "RK1[",k,",",j,"]",matrix[k-1][j-1]
			return matrix[k-1][j-1]

# Passar os indices e os valores.


def R(k,j):
	if k == 1 and j == 1:
		return R11(k,j)
	elif k > 1 and j == 1:
		return Rk1(k,j)
	else:
		matrix[k-1][j-1] = ( R(k,j-1) + (((R(k,j-1) - R(k-1,j-1) )) / (4**(j-1)-1)) ) 
		return matrix[k-1][j-1]

def rombergByScipy():
	gaussian = lambda x: -1.47206*(10**-7)*(x**10)+0.0000148524*(x**9)-0.000642464*(x**8)+0.0155672*(x**7)-0.231584*(x**6)+2.17898*(x**5)-12.861*(x**4)+45.434*(x**3)-85.9344*(x**2)+65.5502*(x)
	result = integrate.romberg(gaussian,a, b, show=True)
	print("%g %g" % (2*result, erf(1)))
