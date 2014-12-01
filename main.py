# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""


import dataToCouchDB
import readPage
import basicSentimentAnalysis
import fetchTags
import plottinByTag
import plottinByType


def main():
    myDBname = 'information_dk_articles'
    try:
        dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    except Exception:
        print "DB connection error. " + Exception

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
