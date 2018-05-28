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
	    self.db_file = "photographs.db"
				
	def execute(self, sql):
		try:
			conn = sqlite3.connect(db_file)
		except Error as e:
			print(e)
		finally:
			conn.close()            
		c = conn.cursor()
		c.execute(sql)
		conn.commit()
		conn.close()
		
		
		

