# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:31:23 2014

Information.dk mining

"""

import numpy as np
import matplotlib.pyplot as plt
import dataToCouchDB
from collections import defaultdict


def sentPlotting(mydefaultDict):
    bodyAvgList = []
    commAvgList = []
    for sentDict in sentList:
        floatBAvg = float(sentDict['body']['Average'])
        bodyAvgList.append(floatBAvg)
        floatCAvg = float(sentDict['comments']['Average'])
        commAvgList.append(floatCAvg)

    hist, bins = np.histogram(bodyAvgList, bins=15)
    hist2, bins = np.histogram(commAvgList, bins=15)
    width = 0.5 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width,
            color='blue', alpha=0.5, label='Body')
    plt.bar(center, hist2, align='center', width=width,
            color='red', alpha=0.5, label='Comments')
    plt.plot(center, hist, 'b--')
    plt.plot(center, hist2, 'r-')

    plt.legend(loc='upper right')
    plt.xlabel("Sentiment Bins")
    plt.ylabel("Number of Articles")
    plt.title("Articles Sorted in Sentiment Bins")
    plt.savefig("SentimentNumpyHistogram.png")
    plt.show()


def startPlotting(dbConn):
    '''
    Function used to fetch and plot specific articles
    '''
    # Define the article types that we use and their lengths
    myDict = {'Articles': 7, 'Telegram': 16, 'Nyhedsblog': 18}
    print "===startPlotting: Checking DB==="
    d = defaultdict(list)
    for k in myDict:
        sentList = []
        for article in dbConn:
            if (len(article) is myDict[k]):  # 7, 16, 18
                myArticle = dataToCouchDB.loadArticleFromDB(dbConn, article)
                sentList.append(myArticle['sentiment'])

        print "===startPlotting: Number of " + k + ": " + str(len(sentList))
        d[k].append(sentList)
    
    print len(d)
    return
    print "===startPlotting: Plotting======"
    sentPlotting(d)

    return "===Plotting complete==="


def main():
    myDBname = 'information_dk_articles'
    dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    startPlotting(dbConnection)

if __name__ == "__main__":
    main()
