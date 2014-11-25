# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:31:23 2014

Information.dk mining

"""

import numpy as np
import matplotlib.pyplot as plt
import dataToCouchDB
from collections import Counter


def createList(tmpList):
    resultList = []
    for i,val in enumerate(tmpList):
        resultList.append(i)
    return resultList


def tagSentPlotting(sentList, tag):
    bodyAvgList = []
    commAvgList = []
    for i, sentDict in enumerate(sentList):
        floatBAvg = float(sentDict['body']['Average'])
        bodyAvgList.append(floatBAvg)
        floatCAvg = float(sentDict['comments']['Average'])
        commAvgList.append(floatCAvg)
    
    print "Body: " + str(bodyAvgList)
    print "Comments: " + str(commAvgList)
    width = 0.3
    nOfArt = createList(bodyAvgList)
    plt.bar(nOfArt, bodyAvgList, width=width, color='blue', alpha=0.5, label='Body')
    plt.bar(nOfArt, commAvgList, width=width, color='red', alpha=0.5, label='Comments')
    plt.legend(loc='upper right')
    plt.xlabel("Articles")
    plt.ylabel("Sentiment Average")
    plt.title("Tag: " + tag)
    plt.savefig("SentimentNumpyHistogram.png")
    plt.show()


def startPlotting(dbConn):
    '''
    Function used to fetch and plot specific articles
    '''
    print "===startPlotting: Checking DB==="
    tagList = []
    tmpList = []
    for article in dbConn:
        if (len(article) is 7):
            myArticle = dataToCouchDB.loadArticleFromDB(dbConn, article)
            if (myArticle['tags']):
                tmpList = myArticle['tags'].split()
                for word in tmpList:
                    if len(word)>3:
                        tagList.append(word)
                    
    counts = Counter(tagList)
    # print counts.most_common(5)
    tag = counts.most_common(1)[0][0]
    
    sentList = []
    for article in dbConn:
        if (len(article) is 7):
            myArticle = dataToCouchDB.loadArticleFromDB(dbConn, article)
            if (tag in myArticle['tags']):
                # print tag.replace('utf-8','replace')
                sentList.append(myArticle['sentiment'])    
    
    tagSentPlotting(sentList, tag)

    return "===Plotting complete==="


def main():
    myDBname = 'information_dk_articles'
    dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    startPlotting(dbConnection)

if __name__ == "__main__":
    main()
