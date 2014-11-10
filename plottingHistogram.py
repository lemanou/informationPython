# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 15:00:00 2014

@author: Sigurd

"""

with open( "ResultSentiment.txt", "r") as FileToRead:
    FileToWrite = open('DataToPlot.txt', 'w')
    D = {}
    SentimentScores = [0,0,0,0,0,0]
    
    for Line in FileToRead:
        (NumberOfWords, val1, ArticleID, val2, Average, val3, Sentiment, val4) = Line.split()
        D[NumberOfWords] = val1.strip(': ,')
        D[ArticleID] = val2.strip(': ,u\'\/telgram')
        D[Average] = val3.strip(': ,')
        D[Sentiment] = val4.strip(': ,}')
        # CHANGE HERE
        DintAverage = float(D[Average])
        if(DintAverage < -2):
            SentimentScores[0] += 1
        elif(DintAverage < -1):
            SentimentScores[1] += 1
        elif(DintAverage < 0):
            SentimentScores[2] += 1
        elif(DintAverage < 1):
            SentimentScores[3] += 1
        elif(DintAverage < 2):
            SentimentScores[4] += 1
        else:
            SentimentScores[5] += 1

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(SentimentScores)
plt.xlabel("Sentiment Bins")
plt.ylabel("Number of Articles")
plt.title("Histogram of Articles Divided in Sentiment Scores")
plt.savefig("SentimentHistogram.png")
plt.show()