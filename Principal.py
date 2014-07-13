#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Method import *
import sys, time, datetime, os


if __name__ == "__main__":

	firstTime = False
	os.system('clear')
	
	print '=====================Fermat====================='
	print 'Option - Description'
	print '     1 - Solve the problem using Romberg'
	print '     2 - About'
	print '     0 - Exit' 
	print ''  
	option = -7

	while( option < 0  or option > 3):
		try:
			option = int(raw_input('Your Option: '))
		except Exception,msg:
			log.write('Principal: Error: '+str(msg))
	if option == 1:    
		romberg()
	elif option == 0:
		print 'Good Bye!'
	elif option == 2:
		print 'Biblioteca desenvolvida para solucionaro o problema'
		print '     proposto no trabalho de Calculo Numerico. Para  saber'
		print '     mais sobre o trabalho, por favor, acesse Ava/UFPel'
		print ''
		print 'Integrantes:'
		print '		André Alba'
		print '     Glauco Roberto'
	else:
		print 'Something is wrong!'
