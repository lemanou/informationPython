# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""

import urllib
import json
from bs4 import BeautifulSoup


def parseNormal(myLink, postID):
	article = {}
	# Open the site
	url = myLink + postID
	# print "Opening: " + url
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	tree = BeautifulSoup(htmltext)
	# Get the relevant parts from the page
	for title in tree.findAll("h1", class_="node-title"):
		# print title
		article["title"] = title.contents[0]
	# print type(title.contents[0])
	neededClass = "field field-name-field-underrubrik"
	for abstract in tree.findAll("div", class_=neededClass):
		# print abstract
		article["abstract"] = abstract.contents[0]
	for numCom in tree.findAll("div", class_="field-name-comment-count-link-top"):
		# print str(numCom)[104:107]
		article["comments"] = numCom.contents[0].contents[0]
	return article


def parseTelegram(myLink, postID):
	article = {}
	# Open the site
	url = myLink + postID
	# print "Opening: " + url
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	tree = BeautifulSoup(htmltext)
	# Get the relevant parts from the page
	for title in tree.findAll("h1", class_="node-title"):
		# print title
		article["title"] = title.contents[0]
	# print type(title.contents[0])
	neededClass = "field field-name-field-ritzau-subheader"
	for abstract in tree.findAll("div", class_=neededClass):
		# print abstract
		article["abstract"] = abstract.contents[0]
	for numCom in tree.findAll("a", class_="active"):
		# print str(numCom)[104:107]
		article["comments"] = numCom.contents[0]
	return article
	
def parseNyheder(myLink, postID):
	article = {}
	# Open the site
	url = myLink + postID
	# print "Opening: " + url
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	tree = BeautifulSoup(htmltext)
	# Get the relevant parts from the page
	for title in tree.findAll("div", class_="field field-name-title"):
		#print title.contents[0].contents[0]
		article["title"] = title.contents[0].contents[0]
	# print type(title.contents[0])
	neededClass = "field field-name-field-underrubrik"
	for abstract in tree.findAll("div", class_=neededClass):
		# print abstract
		article["abstract"] = abstract.contents[0]
	for numCom in tree.findAll("li", class_="comment last"):
		#print numCom.contents[0].contents[0]
		article["comments"] = numCom.contents[0].contents[0]
	return article
	
def parseHTML():

	# Read and split the links from a file
	newsFile = open("myNewsSites.txt")
	newsList = newsFile.read()
	newsList = newsList.split("\n")

	title = newsList[0]
	myLink = title[0:26]
	# print "\nConnecting to: " + myLink + "\n"

	# Open the link
	htmlobj = urllib.urlopen(myLink)
	htmltext = htmlobj.read()
	tree = BeautifulSoup(htmltext)
	count = 0
	myList = []
	# Get the apostIDailable article posts of the page
	for node in tree.findAll("h3", class_="node-title"):
		# print node
		soup = BeautifulSoup(str(node))
		for link in soup.findAll('a'):
			# print link.get('href')
			count += 1
			myId = link.get('href')
			# Inserting the new post to the end of the list
			myList.insert(len(myList), myId)
	print "OUTPUT - Number of articles: " + str(count) + "\n"
	# print type(myList)
	myDict = {}

	for i, postID in enumerate(myList):

		# Open the article's site
		myLink = myLink[0:25]
		url = myLink + postID
		print url
		urlLength = len(url)
		
		if (urlLength == 32):
			# print "Normal/Random: " + str(urlLength)
			myArticle = parseNormal(myLink, postID)
			myDict[postID] = myArticle
		elif (urlLength == 41):
			# print "Telegram OR Protocol: " + str(urlLength)
			myArticle = parseTelegram(myLink, postID)
			myDict[postID] = myArticle
		elif (urlLength == 43):
			# print "Nyhedsblog: " + str(urlLength)
			myArticle = parseNyheder(myLink, postID)
			myDict[postID] = myArticle
			break
		elif (urlLength == 55):
			print "Comment from random article: " + str(urlLength)
		elif (urlLength == 44):
			print "Blogs: " + str(urlLength)
		elif (urlLength == 49):
			print "Kortfilmsbloggen: " + str(urlLength)
		else:
			print "Not processed / Unknown size: " + str(urlLength)	
	
	# for x in myDict:
	# 	print (x)
	#	for y in myDict[x]:
	#		print (y,':',myDict[x][y])
	
	with open("dailyPosts/" + "myDictionary" + ".txt","w+")	as myfile:
		json.dump(myDict, myfile, indent=4)
	
parseHTML()
