# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:39:42 2014

Information.dk mining
---------------------------------------------------------
"""
from datetime import datetime
import json
from couchdb import Server, Database
from couchdb.mapping import Document, TextField, DateTimeField


class myArticles(Document):
    myJson = TextField()
    added = DateTimeField(default=datetime.now)


def createDB(name):
    server = Server()
    db = server.create(name)


def storeFileInDB(myPath):
    db = Database('informationDKarticles')
    with open(myPath, "r") as myfile:
        a = json.load(myfile)
    # Create dictionary from the JSON
    parent = a["article"]
    # print parent["id"]
    myID = str(parent["id"])
    if not(myID in db):
        db[myID] = (a)
        print "DB updated. " + myID
    else:
        print "Article already exists. " + myID


def storeDicInDB(locDB, myDic, postID):
    db = Database(locDB)
    # Select the parent from the dictionary
    parent = myDic["article"]
    myID = postID
    if not(myID in db):
        db[myID] = (myDic)
        print "DB updated. " + myID
    else:
        print "Article already exists. " + myID


def loadFromDB():
    db = Database('my_articles')
    for row in db.view('_all_docs'):
        # print(row.id)
        article = myArticles.load(db, row.id)
        # print article.rev
        # print article.id
        # print dir(article)
        # print article.__getitem__
        myDict = article.__dict__
        # print type(myDict['_data'])
        print "------- " + row.id + " ---------"
        for x in myDict:
            for y in myDict[x]:
                if (y == 'article'):
                    print myDict[x][y]['abstract'].encode('ascii', 'replace')  # .encode('utf-8')
        break
        print "--------------------------------"


def main():
    # db.delete(doc)
    # db = Server()
    # db.delete('python-tests2')

    # createDB()
    # storeInDB("dailyPosts/" + "511562" + ".txt")
    # loadFromDB()
    loadFromDB()


if __name__ == "__main__":
    main()
