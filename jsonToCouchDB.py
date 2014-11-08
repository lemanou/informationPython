# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
import couchdb


def storeDicInDB(locDB, myDic, postID):
    couch = couchdb.Server()
    db = couch[locDB]

    if not(postID in db):
        db[postID] = myDic
        print "DB updated. " + postID
    else:
        print "Article already exists. " + postID
