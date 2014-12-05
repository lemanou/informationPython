# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining

Main program.
---------------------------------------------------------
"""


import sys
import dataToCouchDB
import readPage
import basicSentimentAnalysis
import fetchTags
import plottinByTag
import plottinByType


def checkStart():
    '''
    Function used to check if this is the first time the code runs
    '''
    print "Is this the first time you are running this code? (y/n)"
    yes = set(['yes', 'y', 'ye', ''])
    no = set(['no', 'n'])

    choice = raw_input().lower()
    if choice in yes:
        print "Do you have couchDB installed? (y/n)"
        choice = raw_input().lower()
        if choice in yes:
            return True
        else:
            sys.stdout.write("Install couchDB to run this software. Exiting.")
            sys.exit()
    elif choice in no:
        return False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'. Exiting.")
        sys.exit()


def main():
    choise = checkStart()
    myDBname = 'information_dk_articles'
    if (choise):
        dbConnection = dataToCouchDB.createDB(myDBname)
    else:
        try:
            dbConnection = dataToCouchDB.getConnectionDB(myDBname)
        except Exception:
            print "DB connection error. " + str(Exception)
            return

    print "\n===Starting parsing==="
    newArticleCount, myList = readPage.parseHTML(dbConnection)

    print "\n===Starting sentiment calculation==="
    calculated = basicSentimentAnalysis.startAnalysis(dbConnection)

    print "\n===Fetching tags==="
    tags = fetchTags.updateTags(dbConnection)

    print "\n============Results============"
    print "Number of new articles: " + str(newArticleCount)
    print "Out of: " + str(len(myList)) + " possible"
    print "Number of calculated articles: " + str(calculated)
    print "Number of new articles with tags: " + str(tags)

    print "\n=======Plotting by Tag========="
    plottinByTag.startPlotting(dbConnection)

    print "\n=======Plotting by Type========"
    plottinByType.startPlotting(dbConnection)

    print "\n==============================="


if __name__ == "__main__":
    main()
