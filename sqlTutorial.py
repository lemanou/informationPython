from datetime import datetime
import json
from couchdb import Server, Database
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

server = Server()
db = Database('python-tests2 ')  # server.create('python-tests2')


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


with open("dailyPosts/" + "myDictionary" + ".txt", "r") as myfile:
    a = json.load(myfile)

# print (a)

article = myArticles(id='1', myJson=a)
article.store(db)

print(article.myJson)
