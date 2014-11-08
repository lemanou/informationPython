# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from nltk import word_tokenize
import couchdb


def splitTextToWords(text):
    return word_tokenize(text)


def createSentDict():
    sentList = {}
    with open('Nielsen2011Sentiment_afinndk.txt', 'r') as f:
        for line in f:
            (key, val) = line.split()
            sentList[key] = int(val)
    return sentList


def getSentiment(post, sentList):
    # Get the body of the article, split it to words and lowercase them
    articleBody = post['article']['body']
    wordsList = splitTextToWords(articleBody)
    wordsList = [x.lower() for x in wordsList]

    # Calculate the sentiment score
    sSum = 0
    sCount = 0
    sAvg = 0
    for word in wordsList:
        if word in sentList:
            sCount += 1
            sSum += sentList[word]
    if sCount != 0:
        sAvg = round(float(sSum)/sCount, 2)
    sDict = {'ID': post['_id'], 'Sent': sSum, 'NumOWords': sCount, 'Avg': sAvg}
    return sDict


def main():
    couch = couchdb.Server()
    db = couch['information_dk_articles']

    # Create Dictionary from sentiment file
    sentList = createSentDict()

    myList = []
    mCount = 0
    for article in db:
        mCount += 1
        myList.append(mCount)
        myList.append(getSentiment(dict(db[article]), sentList))
    # print myList
    f = open('ResultSentiment.txt', 'w')
    for item in myList:
        f.write("%s\n" % item)
    f.close()

if __name__ == "__main__":
    main()
