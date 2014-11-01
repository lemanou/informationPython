# -*- coding: utf-8 -*-
"""
Created on Sat Nov 1 19:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from nltk import sent_tokenize, word_tokenize
import json
import re  # Use regular expressions to find the numbers in the sentiment list
    
 
def splitS(text):
    sents = sent_tokenize(text)
    return sents


def splitW(sentence):
    tokens = word_tokenize(sentence) 
    return tokens


def word_score(wordCheck, acum_score):
    #Load Sentiment List and check for word
    with open('Nielsen2011Sentiment_afinndk.txt', 'r') as f:
        for line in f:            
            if wordCheck in line.split():
                print re.findall('\d+', line)[0]
                return int(re.findall('\d+', line)[0])
            else:                
                print "WORD: " + wordCheck.encode('utf-8','replase') + " NOT FOUND."
                return acum_score


def sentiment_score(wordsList):
    return sum([word_score(word, 0.0) for word in wordsList])

 
def main():
    json_data=open('dailyPosts/514201.txt', 'r')
    data = json.load(json_data)
    text = (data['article']['body'])
    #print text.encode('utf-8','replase')
     
    splitted_sentences = splitS(text)
    
    #print splitted_sentences
    words = splitW(text)
     
    #print words
    print "Sent: " + str(sentiment_score(words))

if __name__ == "__main__":
    main()
