# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from nltk import word_tokenize
import dataToCouchDB


def splitTextToWords(text):
    '''
    Function used to word tokenize fron nltk
    '''
    return word_tokenize(text)


def createSentDict():
    '''
    Function used to create a dictionary from the sentiment file
    '''
    sentList = {}
    with open('Nielsen2011Sentiment_afinndk.txt', 'r') as f:
        for line in f:
            (key, val) = line.split()
            sentList[key] = int(val)
    return sentList


def wordCounting(wordsList, sentList):
    '''
    Function used to calculate the Number Of Words found in sentiment list
    and the sentiment score
    '''
    aSent = 0       # Sentiment
    sCount = 0      # Number Of Words found in sentiment list

    for word in wordsList:
        if word in sentList:
            sCount += 1
            aSent += sentList[word]

    return sCount, aSent    


def getCommentsSentiment(post, sentList):
    '''
    Function used to calculate the sentiment of the comments
    from a specific article
    '''
    comSent = 0     # CommentS sentiment
    sCount = 0      # Number Of Words found in sentiment list
    sAvg = 0
    # Get the comments of the article, split it to words and lowercase them
    myArticle = post['article']['comments']
    # Check if the article is empty
    if (not myArticle):
        myArticle = post['article']['comments']['commentsBody']
        for i, articleComments in enumerate(myArticle):
            wordsList = splitTextToWords(myArticle[str(i)])
            wordsList = [x.lower() for x in wordsList]

            # Calculate the sentiment score
            sCount, comSent = wordCounting(wordsList, sentList)
            
        if sCount != 0:
            sAvg = round(float(comSent)/sCount, 2)

    sDict = {'Sentiment': comSent, 'NumberOfWords': sCount, 'Average': sAvg}
    return sDict


def getBodySentiment(post, sentList):
    '''
    Function used to calculate the sentiment of the body
    from a specific article
    '''
    bdSent = 0  # Body sentiment
    sCount = 0  # Number Of Words found in sentiment list
    sAvg = 0

    # Get the body of the article, split it to words and lowercase them
    articleBody = post['article']['body']
    wordsList = splitTextToWords(articleBody)
    wordsList = [x.lower() for x in wordsList]
    
    # Calculate the sentiment score
    sCount, bdSent = wordCounting(wordsList, sentList)

    if sCount != 0:
        sAvg = round(float(bdSent)/sCount, 2)

    sDict = {'Sentiment': bdSent, 'NumberOfWords': sCount, 'Average': sAvg}
    return sDict


def startAnalysis(dbConn):
    '''
    Function used to calculate the sentiment of the comments and a body
    from all db articles
    '''
    # Create Dictionary from sentiment file
    sentList = createSentDict()
    numOfCalculated = 0
    print "===startAnalysis: Checking DB for missing sentiments==="
    for article in dbConn:
        calculated = False
        myArticle = dataToCouchDB.loadArticleFromDB(dbConn, article)
        # First checking if article's sentiment already calculated
        # By checking the keys from the dictionary
        for key, value in myArticle.iteritems():
            if (key == 'sentiment'):
                calculated = True

        if (not calculated):
            result = {}
            bodyDict = getBodySentiment(dict(dbConn[article]), sentList)
            commetsDict = getCommentsSentiment(dict(dbConn[article]), sentList)
            result['body'] = bodyDict
            result['comments'] = commetsDict
            dataToCouchDB.storeSentInDB(dbConn, result, article)
            numOfCalculated += 1

    return numOfCalculated


def main():
    myDBname = 'information_dk_articles'
    dbConnection = dataToCouchDB.getConnectionDB(myDBname)
    startAnalysis(dbConnection)

if __name__ == "__main__":
    main()
