# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""

import urllib
from bs4 import BeautifulSoup

import dataToCouchDB
import basicSentimentAnalysis


def removeParenthesis(tmp):
    if '(' in tmp:
        tmp = tmp.replace("(", "")
    if ')' in tmp:
        tmp = tmp.replace(")", "")
    return tmp


# Parsing the articles based on categories and tags
def getBody(tree, postID):
    '''
    Function used to fetch all the body / <p> tags from an article
    '''
    body = ""
    neededClass = ""

    if 'nyhedsblog' in postID:
        neededClass = "field field-name-field-underrubrik"
    else:
        neededClass = "field field-name-body"

    for text in tree.findAll("div", class_=neededClass):
        for childdiv in text.find_all('p'):
            if not (childdiv.string is None):
                body += childdiv.string
            if '<strong>' or '</strong>' in childdiv:
                body += " "

    return body


def getComments(tree):
    '''
    Function used to fetch all the comments from an article
    '''
    article = {}
    dAuthor = {}
    dDomment = {}
    for comments in tree.findAll(class_="comment-wrapper"):
        myArray = []
        myArray2 = []
        if not (comments is None):
            count = 0
            for author in comments.findAll("div", class_="comment-name"):
                for childdiv in author.find_all('a'):
                    if not (childdiv.string is None):
                        count += 1
                        myArray.append(childdiv.string)
            count = 0  # !!!
            neededClass = "field-item even"
            for commentBody in comments.findAll("div", class_=neededClass):
                count += 1
                cmnt = ""
                for childdiv in commentBody.find_all('p'):
                    if not (childdiv.string is None):
                        cmnt += childdiv.string
                myArray2.append(cmnt)
        for id in range(len(myArray)):
            dAuthor[id] = myArray[id]
            dDomment[id] = myArray2[id]
        article["commentsAuthor"] = dAuthor
        article["commentsBody"] = dDomment
    return article


def parseNormal(myLink, postID):
    '''
    Function used to parse the normal articles
    '''
    article = {}
    # Open the site
    url = myLink + postID
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    # Get the relevant parts from the page
    for title in tree.findAll("h1", class_="node-title"):
        article["title"] = title.contents[0]

    neededClass = "field field-name-field-underrubrik"
    for abstract in tree.findAll("div", class_=neededClass):
        article["abstract"] = abstract.contents[0]

    neededClass = "field-name-comment-count-link-top"
    for numCom in tree.findAll("div", class_=neededClass):
        tmp = numCom.contents[0].contents[0][13:15]
        article["numberOfComments"] = removeParenthesis(tmp)

    article["body"] = getBody(tree, postID)
    article["comments"] = getComments(tree)

    return article


def parseTelegram(myLink, postID):
    '''
    Function used to parse the telegram articles
    '''
    article = {}
    # Open the site
    url = myLink + postID
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    # Get the relevant parts from the page
    for title in tree.findAll("h1", class_="node-title"):
        article["title"] = title.contents[0]

    neededClass = "field field-name-field-ritzau-subheader"
    for abstract in tree.findAll("div", class_=neededClass):
        article["abstract"] = abstract.contents[0]

    if 'protokol' in postID:
        article["numberOfComments"] = "unknown"
    else:
        for numCom in tree.findAll("a", class_="active"):
            tmp = ""
            tmp = numCom.contents[0][13:15]
            article["numberOfComments"] = removeParenthesis(tmp)

    article["body"] = getBody(tree, postID)
    article["comments"] = getComments(tree)

    return article


def parseNyheder(myLink, postID):
    '''
    Function used to parse the news articles
    '''
    article = {}
    # Open the site
    url = myLink + postID
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    # Get the relevant parts from the page
    for title in tree.findAll("div", class_="field field-name-title"):
        article["title"] = title.contents[0].contents[0]

    neededClass = "field field-name-field-underrubrik"
    for abstract in tree.findAll("div", class_=neededClass):
        article["abstract"] = abstract.contents[0]

    for numCom in tree.findAll("li", class_="comment last"):
        tmp = ""
        tmp = numCom.contents[0].contents[0][13:15]
        article["numberOfComments"] = removeParenthesis(tmp)

    article["body"] = getBody(tree, postID)
    article["comments"] = getComments(tree)

    return article


def parseBlog(myLink, postID):
    '''
    Function used to parse the blog articles
    '''
    article = {}
    # Open the site
    url = myLink + postID
    # print "Opening: " + url
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    # Get the relevant parts from the page
    for title in tree.findAll("h1", class_="node-title"):
        article["title"] = title.contents[0]

    neededClass = "field field-name-body"
    for div in tree.find_all(class_=neededClass):
        # Get the first child (<p>) in the div
        for childdiv in div.find_all('p'):
            article["abstract"] = childdiv.string
            break

    for numCom in tree.findAll("li", class_="comment last"):
        tmp = ""
        tmp = numCom.contents[0].contents[0][13:15]
        article["numberOfComments"] = removeParenthesis(tmp)

    article["body"] = getBody(tree, postID)
    article["comments"] = getComments(tree)

    return article


def parseFilme(myLink, postID):
    '''
    Function used to parse the film articles
    '''
    article = {}
    # Open the site
    url = myLink + postID
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    tree = BeautifulSoup(htmltext)

    # Get the relevant parts from the page
    for title in tree.findAll("div", class_="field field-name-title"):
        article["title"] = title.contents[0].contents[0]

    neededClass = "field field-name-body"
    for div in tree.find_all(class_=neededClass):
        # Get the first child (<p>) in the div
        for childdiv in div.find_all('p'):
            article["abstract"] = childdiv.string
            break

    for numCom in tree.findAll("li", class_="comment last"):
        tmp = ""
        tmp = numCom.contents[0].contents[0][13:15]
        article["numberOfComments"] = removeParenthesis(tmp)

    article["body"] = getBody(tree, postID)
    article["comments"] = getComments(tree)

    return article


def parseHTML(myDB):
    '''
    Function used to parse the information.dk main page
    Find the relevant articles
    Call the different "parser" for each article type
    '''

    # Read and split the links from a file
    newsFile = open("myNewsSites.txt")
    newsList = newsFile.read()
    newsList = newsList.split("\n")
    newArticleCount = 0
    title = newsList[0]
    myLink = title[0:26]

    # Open the link
    htmlobj = urllib.urlopen(myLink)
    htmltext = htmlobj.read()
    tree = BeautifulSoup(htmltext)

    myList = []
    # Get all the available article posts (postID) from the page
    for node in tree.findAll("h3", class_="node-title"):
        soup = BeautifulSoup(str(node))
        for link in soup.findAll('a'):
            myId = link.get('href')
            # Inserting the new post to the end of the list
            myList.insert(len(myList), myId)
    # print "OUTPUT - Number of possible articles: " + str(len(myList)) + "\n"

    for i, postID in enumerate(myList):
        print postID
        # First check if article is already in local DB
        if (dataToCouchDB.checkIfArticleInDB(myDB, postID) == 1):
            print "Article already in DB - SKIPPING"
        # If not, parse the article's page
        else:
            # Open the article's site
            myLink = myLink[0:25]
            url = myLink + postID
            urlLength = len(url)
            myDict = {}
            check = False

            # Different parsing based on article type / URL length
            if (urlLength == 32):
                # print "Normal/Random: " + str(urlLength)
                myArticle = parseNormal(myLink, postID)
                myDict["article"] = myArticle
                check = True
            elif (urlLength == 41):
                # print "Telegram OR Protocol: " + str(urlLength)
                # Protocols have no abstract or numCom
                myArticle = parseTelegram(myLink, postID)
                myDict["article"] = myArticle
                check = True
            elif (urlLength == 43):
                # print "Nyhedsblog: " + str(urlLength)
                myArticle = parseNyheder(myLink, postID)
                myDict["article"] = myArticle
                check = True
            elif (urlLength == 44):
                # print "Blogs: " + str(urlLength)
                myArticle = parseBlog(myLink, postID)
                myDict["article"] = myArticle
                check = True
            elif (urlLength == 49):
                # print "Kortfilmsbloggen: " + str(urlLength)
                myArticle = parseFilme(myLink, postID)
                myDict["article"] = myArticle
                check = True
            elif (urlLength == 55):
                print "\t NOT PROCESSED - Comment from random article."
            else:
                print "\t NOT PROCESSED - Unknown type: " + str(urlLength)

            # Check for "known" / parsed article.
            if (check):
                dataToCouchDB.storeDicInDB(myDB, myDict, postID)
                newArticleCount += 1

    return newArticleCount, myList


def main():
    myDBname = 'information_dk_articles'
    try:
        dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    except Exception:
        print "DB connection error. " + Exception
    print "===Starting parsing==="
    newArticleCount, myList = parseHTML(dbConnection)
    print "===Starting sentiment calculation==="
    calculated = basicSentimentAnalysis.startAnalysis(dbConnection)
    print "============Results============"
    print "Number of new articles: " + str(newArticleCount)
    print "Out of: " + str(len(myList)) + " possible"
    print "Number of calculated articles: " + str(calculated)

if __name__ == "__main__":
    main()
