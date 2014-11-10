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
    DataList = []
    for Line in FileToRead:
        (NumberOfWords, val1, ArticleID, val2, Average, val3, Sentiment, val4) = Line.split()
        D[NumberOfWords] = val1.strip(': ,')
        D[ArticleID] = val2.strip(': ,u\'\/telgram')
        D[Average] = val3.strip(': ,')
        D[Sentiment] = val4.strip(': ,}')
        # CHANGE HERE
        DfloatAverage = float(D[Average])
        DataList.append(DfloatAverage)

# post: we have a dataList of sentiments
FileToRead.close()

import matplotlib.pyplot as plt
import numpy as np

hist, bins = np.histogram(DataList, bins=[-3, -2, -1, 0, 1, 2, 3])
width = 0.3 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.xlabel("Sentiment Bins")
plt.ylabel("Number of Articles")
plt.title("Articles Sorted in Sentiment Bins")
plt.savefig("SentimentNumpyHistogram.png")
plt.show()