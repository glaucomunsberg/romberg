#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Method import *
import sys, time, datetime, os


if __name__ == "__main__":

	rangeOut = False
	sair = False
	while( not sair):
		firstTime = False
		os.system('clear')
		print bcolors.HEADER + '============================= Romberg =========================' + bcolors.ENDC
		print 'Option - Description'
		print '     1 - Solve the problem using Romberg'
		print '     2 - About'
		print '     3 - Calculate f(x)'
		print '     4 - Result with Scipy Library'
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
			print bcolors.HEADER + '========================= Romberg  - Method =====================' + bcolors.ENDC
			#try:
			romberg()
			#except Exception,msg:
			#	print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('\nPress enter')

		elif option == 0:
			os.system('clear')
			print bcolors.HEADER + '======================== Romberg - Exit ========================' + bcolors.ENDC
			print 'Good Bye!'
			sair = True

		elif option == 2:
			os.system('clear')
			print bcolors.HEADER + '===================== Romberg - Integrantes =====================' + bcolors.ENDC
			print 'Biblioteca desenvolvida para solucionaro o problema'
			print '     proposto no trabalho de Calculo Numerico. Para  saber'
			print '     mais sobre o trabalho, por favor, acesse Ava/UFPel'
			print ''
			print 'Integrantes:'
			print '		André Alba'
			print '     Glauco Roberto'
			raw_input('\nPress enter')

		elif option == 3:
			os.system('clear')
			try:
				print bcolors.HEADER + '===================== Romberg - Calculate ======================' + bcolors.ENDC
				result = function(int(raw_input('Your \'x\' to function(x):')))
				print 'Result to function(x)=',result
			except Exception,msg:
				print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('Press enter')

		elif option == 4:
			os.system('clear')
			try:
				print bcolors.HEADER + '====================== Romberg - Library =======================' + bcolors.ENDC
				print 'Using Scipy Library'
				print ''
				result = RombergByScipy()
			except Exception,msg:
				print bcolors.FAIL +'Something is wrong!\n'+ str(msg) + bcolors.ENDC
			raw_input('\nPress enter')

		else:
			os.system('clear')
			print bcolors.HEADER + '======================= Romberg - Ooops! ======================' + bcolors.ENDC
			print bcolors.FAIL +'Something is wrong! Oops!' + bcolors.ENDC
			sair = True
