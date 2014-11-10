# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 10:31:23 2014

@author: Sigurd

"""

with open( "ResultSentiment.txt", "r") as FileToRead:
    # we read our article sentiment data and
    # sort the average sentiments from low to high
    # we save it to a file and plot the graph
    FileToWrite = open('DataToPlot.txt', 'w')
    D = {}
    Data = []
    for Line in FileToRead:
        (NumberOfWords, val1, ArticleID, val2, Average, val3, Sentiment, val4) = Line.split()
        D[NumberOfWords] = val1.strip(': ,')
        D[ArticleID] = val2.strip(': ,u\'\/telgram')
        D[Average] = val3.strip(': ,')
        D[Sentiment] = val4.strip(': ,}')
        # CHANGE HERE
        DfloatAverage = float(D[Average])
        Data.append(DfloatAverage)

FileToRead.close()

sortedDataList = sorted(Data)

FileToWrite.write("%s\n" % sortedDataList)
FileToWrite.close()

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(sortedDataList)
plt.xlabel("Articles")
plt.ylabel("Average Sentiment")
plt.title("Average Sentiment For Each Article")
plt.savefig("SentimentSortedAverageCurve.png")
plt.show()