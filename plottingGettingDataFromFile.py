# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 10:31:23 2014

@author: Sigurd

"""
import collections

with open( "ResultSentiment.txt", "r") as FileToRead:
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
        DintAverage = float(D[Average])
        Data.append(DintAverage)

sortedList = sorted(Data)
print sortedList

FileToWrite.write("%s\n" % sortedList)
FileToWrite.close()

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(sortedList)
plt.xlabel("Articles")
plt.ylabel("Average Sentiment")
plt.title("Average Sentiment For Each Article")
plt.savefig("SentimentSortedAverageCurve.png")
plt.show()