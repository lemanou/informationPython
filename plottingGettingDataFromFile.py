# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 10:31:23 2014

@author: Sigurd
"""


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
        Data.append(D[Average])

print Data
FileToWrite.write("%s\n" % Data)
FileToWrite.close()

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(Data)
plt.xlabel("Articles")
plt.ylabel("Average Sentiment")
plt.title("Average Sentiment of Articles")
plt.savefig("SentimentAverageCurve.png")
plt.show()






"""
FileToWrite = open('DataToPlot.txt', 'w')
for item in myList:
    FileToWrite.write("%s\n" % item)
FileToWrite.close()


import collections

dict = {'a': 1, 'c': 2, 'b': 3, 'd': 4}

sortedDict = collections.OrderedDict(sorted(dict.items()))
print sortedDict

print ("lineData: ")
print lineDataArray



print ("Keys:")
for k in sortedDict.keys() :
    for value in dict:
        " if dict[ value ] == k:"
        print k
        break   
print ("Values:")
for v in sortedDict.values() :
    for key in dict:
        "if dict[ key ] == v:"
        print v
        break
print ("Items:")
for v in sortedDict.values() :
    for key in dict:
        if dict[ key ] == v:
            print key, v
            break
"""