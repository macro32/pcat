#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqlite.py
#  
#  Copyright 2018 john@johnratcliffe.com
#  
#  sqlite3 database handler
#

import sqlite3

class Sqlite:
	
	def __init__(self):
		print('sqlite.init')
		self.db_file = "photographs.db"

	def execute(self, sql):
		try:
			# connecting creates the db if it doesn't exist
			self.conn = sqlite3.connect(self.db_file)
		except Error as e:
			print(e)
#		finally:
#			conn.close()            
		c = self.conn.cursor()
		c.execute(sql)
		self.conn.commit()
		self.conn.close()
		
		
		

