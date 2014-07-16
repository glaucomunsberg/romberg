#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Method import *
from RombergIterate import *
import sys, time, datetime, os


if __name__ == "__main__":

	rangeOut = False
	sair = False
	while( not sair):
		firstTime = False
		os.system('clear')
		print bcolors.HEADER + '============================= Romberg =========================' + bcolors.ENDC
		print 'Option - Description'
		print '     1 - Solve the problem using Romberg Recursive'
		print '     2 - Solve the problem using Romberg Iterative'
		print '     3 - Solve the problem using Scipy Library'
		print '     4 - Calculate f(x)'
		print '     5 - About'
		print '     0 - Exit' 
		print ''
		option = -7

		while( option < 0  or option > 4):
			try:
				if rangeOut == True:
					print bcolors.FAIL+'Out of range, try again' + bcolors.ENDC
				option = int(raw_input('Option: '))

				if option < 0  or option > 4:
					rangeOut = True

			except Exception,msg:
				rangeOut = True

		if option == 1:
			os.system('clear')
			print bcolors.HEADER + '========================= Romberg  - Recursive =====================' + bcolors.ENDC
			#try:
			rombergRecursive()
			#except Exception,msg:
			#	print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('\nPress enter')

		

		elif option == 2:
			os.system('clear')
			print bcolors.HEADER + '========================= Romberg  - Iterative =====================' + bcolors.ENDC
			#try:
			gaussian = lambda x: -1.47206*(10**-7)*(x**10)+0.0000148524*(x**9)-0.000642464*(x**8)+0.0155672*(x**7)-0.231584*(x**6)+2.17898*(x**5)-12.861*(x**4)+45.434*(x**3)-85.9344*(x**2)+65.5502*(x)
			rombergIterate(gaussian,a,b,show=True)
			#except Exception,msg:
			#	print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('\nPress enter')

		elif option == 4:
			os.system('clear')
			try:
				print bcolors.HEADER + '===================== Romberg - Calculate ======================' + bcolors.ENDC
				result = function(int(raw_input('Your \'x\' to function(x):')))
				print 'Result to function(x)=',result
			except Exception,msg:
				print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('Press enter')

		elif option == 3:
			os.system('clear')
			try:
				print bcolors.HEADER + '====================== Romberg - Library =======================' + bcolors.ENDC
				print 'Using Scipy Library'
				print ''
				result = rombergByScipy()
			except Exception,msg:
				print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('\nPress enter')
		elif option == 5:
			os.system('clear')
			print bcolors.HEADER + '===================== Romberg - Group =====================' + bcolors.ENDC
			print 'Biblioteca desenvolvida para solucionaro o problema'
			print '     proposto no trabalho de Calculo Numerico. Para  saber'
			print '     mais sobre o trabalho, por favor, acesse Ava/UFPel'
			print ''
			print 'Integrantes:'
			print '		André Alba'
			print '     Glauco Roberto'
			print '		Guilherme Cousin'
			raw_input('\nPress enter')
		elif option == 0:
			os.system('clear')
			print bcolors.HEADER + '======================== Romberg - Exit ========================' + bcolors.ENDC
			print 'Good Bye!'
			sair = True
		else:
			os.system('clear')
			print bcolors.HEADER + '======================= Romberg - Ooops! ======================' + bcolors.ENDC
			print bcolors.FAIL +'Something is wrong! Oops!' + bcolors.ENDC
			sair = True
