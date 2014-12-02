# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining

fetchTags
=========================================================
Fetching tags ONLY from normal type articles
---------------------------------------------------------
"""
import urllib
import dataToCouchDB
from bs4 import BeautifulSoup


def getTags(post):
    '''
    Function used to fetch the tags of the normal articles
    '''
    # Open the site
    url = "http://www.information.dk" + post['_id']
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    myTags = ""

    neededClass = "field field-name-field-keywords"
    for tags in tree.findAll("div", class_=neededClass):
        for childdiv in tags.find_all('a'):
            if not (childdiv.string is None):
                myTags += childdiv.string
                myTags += " "

    neededClass = "field field-name-field-places"
    for tags in tree.findAll("div", class_=neededClass):
        for childdiv in tags.find_all('a'):
            if not (childdiv.string is None):
                myTags += childdiv.string
                myTags += " "

    return myTags


def updateTags(dbConn):
    '''
    Function used to update the tags of the normal articles
    '''
    numOfCalculated = 0
    print "===updateTags: Checking DB for missing tags==="
    for article in dbConn:
        if (len(article) is 7):
            calculated = False
            myArticle = dataToCouchDB.loadArticleFromDB(dbConn, article)
            # First checking if article's sentiment already calculated
            # By checking the keys from the dictionary
            for key, value in myArticle.iteritems():
                if (key == 'tags'):
                    calculated = True

            if (not calculated):
                result = ""
                result = getTags(dict(dbConn[article]))
                dataToCouchDB.storeTagsInDB(dbConn, result, article)
                numOfCalculated += 1

    return numOfCalculated


def main():
    myDBname = 'information_dk_articles'
    dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    updateTags(dbConnection)

if __name__ == "__main__":
    main()
