from datetime import datetime
import json
from couchdb import Server, Database
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

server = Server()
db = Database('python-tests2 ')  # server.create('python-tests2')
# db.name
# del server['python-tests']

# class Person(Document):
#    name = TextField()
#    age = IntegerField()
#    added = DateTimeField(default=datetime.now)

# person = Person(name='John Doe', age=42)
# person.store(db)

# print(person.age)

class myArticles(Document):
    id = IntegerField()
    myJson = TextField()
    added = DateTimeField(default=datetime.now)


# with open("dailyPosts/" + "myDictionary" + ".txt", "r") as myfile:
#    a = json.load(myfile)

# print (a)

# article = myArticles(id='1', myJson=a)
# article.store(db)
# print(article.myJson)

# json_string = json.dumps(a, sort_keys=True, indent=2)
# print json_string


# article = myArticles(myJson=a)
# article.store(db)
# doc = {'foo': 'bar', '_id':'1'}
# db.save(a)

article = myArticles.load(db, article.id)
comment = article.myJson[0]

print(comment)

