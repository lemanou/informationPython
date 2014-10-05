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

class fEdit():

	def __init__(self):
		# Make new file
		myfile = open("dailyPosts/" + postID + ".txt","w+")
		myfile.close()
		
	def writeInFile(self):
		# Write the title in the file
		myfile = open("dailyPosts/" + postID + ".txt","a")
		myfile.write("Title\n" + myPostTitle + "\nAbstract\n" + abstract)
		myfile.close()
