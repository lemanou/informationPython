# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from nltk import word_tokenize
import jsonToCouchDB


def splitTextToWords(text):
    return word_tokenize(text)


def createSentDict():
    sentList = {}
    with open('Nielsen2011Sentiment_afinndk.txt', 'r') as f:
        for line in f:
            (key, val) = line.split()
            sentList[key] = int(val)
    return sentList


def is_NOT_empty(any_structure):
    if any_structure:
        return True
    else:
        return False


def getCommentsSentiment(post, sentList):
    comSent = 0     # CommentS sentiment
    sCount = 0      # Number Of Words found in sentiment list
    sAvg = 0
    # Get the comments of the article, split it to words and lowercase them
    myArticle = post['article']['comments']
    if (is_NOT_empty(myArticle)):
        myArticle = post['article']['comments']['commentsBody']
        for i, articleComments in enumerate(myArticle):
            wordsList = splitTextToWords(myArticle[str(i)])
            wordsList = [x.lower() for x in wordsList]

            # Calculate the sentiment score
            for word in wordsList:
                if word in sentList:
                    sCount += 1
                    comSent += sentList[word]

        if sCount != 0:
            sAvg = round(float(comSent)/sCount, 2)

    sDict = {'Sentiment': comSent, 'NumberOfWords': sCount, 'Average': sAvg}
    return sDict


def getBodySentiment(post, sentList):
    # Get the body of the article, split it to words and lowercase them
    articleBody = post['article']['body']
    wordsList = splitTextToWords(articleBody)
    wordsList = [x.lower() for x in wordsList]

    # Calculate the sentiment score
    bdSent = 0  # Body sentiment
    sCount = 0  # Number Of Words found in sentiment list
    sAvg = 0

    for word in wordsList:
        if word in sentList:
            sCount += 1
            bdSent += sentList[word]

    if sCount != 0:
        sAvg = round(float(bdSent)/sCount, 2)

    sDict = {'Sentiment': bdSent, 'NumberOfWords': sCount, 'Average': sAvg}
    return sDict


def main():
    myDBname = 'information_dk_articles'
    # myDBname = 'test'
    db = jsonToCouchDB.getConnectionDB(myDBname)

    # Create Dictionary from sentiment file
    sentList = createSentDict()

    myList = []
    for article in db:
        result = {}
        bodyDict = getBodySentiment(dict(db[article]), sentList)
        commetsDict = getCommentsSentiment(dict(db[article]), sentList)
        result['body'] = bodyDict
        result['comments'] = commetsDict
        myList.append(result)
        jsonToCouchDB.storeSentInDB(db, result, article)

    f = open('ResultSentiment.txt', 'w')
    for item in myList:
        f.write("%s\n" % item)
    f.close()

if __name__ == "__main__":
    main()
