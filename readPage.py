# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""

import urllib
import couchdb
from bs4 import BeautifulSoup

def parseNormal(url):
	# Open the site
	print "Opening: " + url
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	
	tree  = BeautifulSoup(htmltext)	
	# Get the relevant parts from the page
	for title in tree.findAll("h1", class_="node-title"):
		print title
	print type(title.contents[0])
	for abstract in tree.findAll("div", class_="field field-name-field-underrubrik"):
		print abstract	
	for numCom in tree.findAll("a", class_="field-name-comment-count-link-top"):
		print numComs

def parseHTML():	
	 
	# Read and split the links from a file
	newsFile = open("myNewsSites.txt")
	newsList = newsFile.read()
	newsList = newsList.split("\n")

	title = newsList[0]
	myLink = title[0:26]
	print "\nConnecting to: " + myLink + "\n"

	# Open the link
	htmlobj = urllib.urlopen(myLink)	
	htmltext = htmlobj.read()
	tree  = BeautifulSoup(htmltext)
	count = 0
	myList = []
	
	# Get the available article posts of the page
	for node in tree.findAll("h3", class_="node-title"):
		#print node
		soup = BeautifulSoup(str(node))
		for link in soup.findAll('a'):
			#print link.get('href')
			count+=1
			myId = link.get('href')
			myList.insert(len(myList), myId)
	
	print "OUTPUT - Number of articles: " + str(count) + "\n"
	#print type(myList)
	
	for i,v in enumerate(myList):		
		# Open the article's site
		myLink = myLink[0:25]
		url = myLink + str(v)
		#print url
		urlLength = len(url)
		
		# Separate the articles based on link's length
		if (urlLength == 32):
			#print "Normal/Random: " + str(urlLength)
			parseNormal(url)
		elif (urlLength == 41):
			print "Telegram OR Protocol: " + str(urlLength)
		elif (urlLength == 43):
			print "Nyhedsblog: " + str(urlLength)
		elif (urlLength == 55):
			print "Comment from random article: " + str(urlLength)
		elif (urlLength == 44):
			print "Blogs: " + str(urlLength)
		elif (urlLength == 49):
			print "Kortfilmsbloggen: " + str(urlLength)
		else:
			print "Not processed / Unknown size: " + str(urlLength)			
		
parseHTML()
