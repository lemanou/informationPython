# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
import couchdb


def createDB(name):
    '''
    Function used to create couchDB
    '''
    couch = couchdb.Server()
    db = couch.create(name)
    return db


def deleteDB(name):
    '''
    Function used to delete couchDB
    '''
    couch = couchdb.Server()
    couch.delete(name)
    return "DB deleted"


def getConnectionDB(locDB):
    '''
    Function used to create couchDB connection
    '''
    couch = couchdb.Server()
    db = couch[locDB]
    return db


def checkIfArticleInDB(db, postID):
    '''
    Function used to check a specific article is in couchDB
    '''
    if not(postID in db):
        return -1
    else:
        return 1


def loadArticleFromDB(db, postID):
    '''
    Function used to load a specific article from couchDB
    '''
    if not(postID in db):
        return -1
    else:
        return dict(db[postID])


def storeDicInDB(db, myDic, postID):
    '''
    Function used to store a new article in couchDB
    '''
    if not(postID in db):
        db[postID] = myDic
        print "DB updated. " + postID
    else:
        print "Article already exists. " + postID


def storeSentInDB(db, mySentiment, postID):
    '''
    Function used to store the calculated sentiment
    in couchDB for the specific article
    '''
    if (postID in db):
        doc = db[postID]
        doc['sentiment'] = mySentiment
        db.save(doc)
        print "+Article sentiment updated. " + postID
    else:
        print "Article not in DB. " + postID


def main():
    # createDB("test")
    # print deleteDB("test")
    print "Nothing to do here."

if __name__ == "__main__":
    main()
