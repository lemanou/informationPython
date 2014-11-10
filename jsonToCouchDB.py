# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
import couchdb


def createDB(name):
    couch = couchdb.Server()
    db = couch.create(name)
    return db


def deleteDB(name):
    couch = couchdb.Server()
    couch.delete(name)
    return "DB deleted"


def getConnectionDB(locDB):
    couch = couchdb.Server()
    db = couch[locDB]
    return db


def checkIfArticleInDB(db, postID):
    if not(postID in db):
        return -1
    else:
        return 1


def loadArticleFromDB(db, postID):
    if not(postID in db):
        return -1
    else:
        return dict(db[postID])


def storeDicInDB(db, myDic, postID):
    if not(postID in db):
        db[postID] = myDic
        print "DB updated. " + postID
    else:
        print "Article already exists. " + postID


def storeSentInDB(db, mySentiment, postID):
    if (postID in db):
        doc = db[postID]
        doc['sentiment'] = mySentiment
        db.save(doc)
        print "Article sentiment updated. " + postID
    else:
        print "Article not in DB. " + postID


def main():
    # createDB("test")
    # print deleteDB("test")
    print "Nothing to do here."

if __name__ == "__main__":
    main()
