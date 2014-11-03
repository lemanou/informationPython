# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from nltk import word_tokenize
import couchdb


def splitTextToWords(text):
    tokens = word_tokenize(text) 
    return tokens


def createSentDict():
    sentList = {}
    with open('Nielsen2011Sentiment_afinndk.txt', 'r') as f:
        for line in f:
           (key, val) = line.split()
           sentList[key] = int(val) 
    return sentList


def getSentiment(article):
    # Create Dictionary from sentiment file
    sentList =  createSentDict()
    
    # Get the body of the article, split it to words and lowercase them
    articleBody = (article['article']['body'])
    wordsList = splitTextToWords(articleBody)
    wordsList = [x.lower() for x in wordsList]
    
    # Calculate the sentiment score
    sum = 0
    count = 0
    avg = 0
    for word in wordsList:
        if word in sentList:
            count+=1
            sum+=sentList[word]
    if count != 0:
        avg = round (float(sum)/count, 2)
    myDict = {'ArticleID': article['_id'], 'Sentiment': sum, 'NumberOfWords':count, 'Average':avg}
    return myDict
    
 
def main():
    # json_data=open('dailyPosts/514321.txt', 'r')
    couch = couchdb.Server()
    db = couch['information_dk_articles']
    myList = []
    for article in db:
        myList.append(getSentiment(dict(db.get(article))))
    #print myList
    f = open('ResultSentiment.txt','w')
    for item in myList:
        f.write("%s\n" % item)
    f.close()

if __name__ == "__main__":
    main()
