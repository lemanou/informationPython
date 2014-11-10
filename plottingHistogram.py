# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 15:00:00 2014

@author: Sigurd

"""

with open( "ResultSentiment.txt", "r") as FileToRead:
    # we read our article sentiment data and
    # sort the articles in sentiment bins
    # we plot the graph
    D = {}
    SentimentScores = [0,0,0,0,0,0]
    
    for Line in FileToRead:
        (NumberOfWords, val1, ArticleID, val2, Average, val3, Sentiment, val4) = Line.split()
        D[NumberOfWords] = val1.strip(': ,')
        D[ArticleID] = val2.strip(': ,u\'\/telgram')
        D[Average] = val3.strip(': ,')
        D[Sentiment] = val4.strip(': ,}')
        # CHANGE HERE
        DfloatAverage = float(D[Average])
        if(DfloatAverage < -2):
            SentimentScores[0] += 1
        elif(DfloatAverage < -1):
            SentimentScores[1] += 1
        elif(DfloatAverage < 0):
            SentimentScores[2] += 1
        elif(DfloatAverage < 1):
            SentimentScores[3] += 1
        elif(DfloatAverage < 2):
            SentimentScores[4] += 1
        else:
            SentimentScores[5] += 1

FileToRead.close()

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(SentimentScores)
plt.xlabel("Sentiment Bins")
plt.ylabel("Number of Articles")
plt.title("Histogram of Articles Divided in Sentiment Scores")
plt.savefig("SentimentHistogram.png")
plt.show()