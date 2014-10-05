# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""

import urllib
import re
import json
import time
import datetime
import sqlite3

class insertInDB():

	def __init__(self):
		# Creates the connection and the db
		self.conn = sqlite3.connect('news.db')
		self.c = conn.cursor()
	
	def tableCreate(self):
		self.c.execute("CREATE TABLE stuffToPlot(ID INT, title TEXT, abstract TEXT, datestamp TEXT)")

		
	def dataEntry(self,idfordb, deTitle, deAbstract):
		date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
		self.c.execute("INSERT INTO stuffToPlot (ID, title, abstract, datestamp) VALUES (?, ?, ?, ?)",
				  (idfordb, deTitle, deAbstract, date))
		self.conn.commit()

	sql = "SELECT * FROM stuffToPlot WHERE ID=?" 
	ID = 509626
	 
	def readData(self):
		for row in self.c.execute(sql, [(ID)]):
			print str(row)
