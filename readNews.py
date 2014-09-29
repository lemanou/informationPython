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

# Creates the connection and the db
conn = sqlite3.connect('news.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, title TEXT, abstract TEXT, datestamp TEXT)")

	
def dataEntry(idfordb, deTitle, deAbstract):
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO stuffToPlot (ID, title, abstract, datestamp) VALUES (?, ?, ?, ?)",
              (idfordb, deTitle, deAbstract, date))
    conn.commit()
	
# tableCreate()
  
# Read and split the links from a file
newsFile = open("myNewsSites.txt")
newsList = newsFile.read()
newsList = newsList.split("\n")
i=0
j=0

title = newsList[i]
link = title[0:25]
print "\nConnecting to: " + link + "\n"

# Open the link and load the Json object
htmlobj = urllib.urlopen(newsList[i])	
data = json.load(htmlobj)
newPost = len(data["ids"])

print "***********************************JSON ids***********************************"
print str(newPost) + " top posts in main page"
print "-----------------------------------Per page-----------------------------------"

while j < newPost: #newPost
	
	# Open the site
	url = link + "/" + str(data["ids"][j])
	print "###############################################################################"
	print url
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	
	# REGEX [^.]* = New string, any char, can be repeated any number of times
	regex = '<h1 class="node-title">(.+?)</h1>'
	# Convert the regex string for the regular expression library
	pattern = re.compile(regex)
	# compiled regex expression, test to search
	postTitle = re.findall(pattern,htmltext)	
	# Check if list is empty
	if not postTitle:
		regex = '<h1 class="title" id="page-title">(.+?)</h1>'
		pattern = re.compile(regex)
		postTitle = re.findall(pattern,htmltext)
		print postTitle[0]
		print "----------------\n"
	else:
		# Make new file
		postID = str(data["ids"][j])
		myfile = open("dailyPosts/" + postID + ".txt","w+")
		myfile.close()
		
		print postTitle[0]
		print "-----------------------------------Abstract-----------------------------------"
		regex = '<div class="field field-name-field-underrubrik">(.+?)</div>'
		pattern = re.compile(regex)
		abstract = re.findall(pattern,htmltext)
		if not abstract:
			abstract = "ERROR: No abstract text found."
			print abstract
			# Write the title in the file
			myfile = open("dailyPosts/" + postID + ".txt","a")
			myfile.write("Title\n" + postTitle[0] + "\nAbstract\n" + abstract)
			myfile.close()
			dataEntry(postID, postTitle[0], abstract)
		else:
			print abstract[0]
			# Write the title in the file
			myfile = open("dailyPosts/" + postID + ".txt","a")
			myfile.write("Title\n" + postTitle[0] + "\nAbstract\n" + abstract[0])
			myfile.close()
			dataEntry(postID, postTitle[0], abstract[0])
		print "-----------------------------------Comments-----------------------------------"
		regex = '<a href="/' + postID + '#kommentarer" class="active">(.+?)</a>'
		pattern = re.compile(regex)
		comments = re.findall(pattern,htmltext)
		if not comments:
			print "ERROR: Strange comments wrapper."
		else:			
			comNum = comments[0].split()[1]
			print comNum
		print "------------------------------------------------------------------------------\n"
	
	j+=1

print "***************************************END**************************************"
