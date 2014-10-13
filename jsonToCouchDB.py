from datetime import datetime
import json
from couchdb import Server, Database
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField, ViewField


class myArticles(Document):
    myJson = TextField()
    added = DateTimeField(default=datetime.now)


def createDB():
    server = Server()
    db = server.create('my_articles')


def storeInDB(myPath):
    # server = Server()
    db = Database('my_articles')
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


def loadFromDB():
    # server = Server()
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
        print "-------" + row.id + "---------"
        # print article
        for x in myDict:
            # print (x)
            for y in myDict[x]:
                if (y == 'article'):
                    print (y,':',myDict[x][y]) #['abstract']
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
