Project Summary
==============================================================

Goals Achieved
---------------
Goal 1 - Parse Information.dk main page

We successfully parsed the main page of Information.dk by using beautiful soup.

Goal 2 - Save data to couchdb

We are successfully exchanging data from local couchdb. 
We choose couchdb because of its ease of use of json and dictionary objects.

Goal 3 - Calculate sentiment

We calculated the sentiment of the articles by using a file that the professor gave us, 
called Nielsen2011Sentiment_afinndk.txt

Goal 4 - Fetch Tags

We discovered that Normal articles have tags so we decided to build on our current 
implementation to add those. However, this is not optimal since we parse the page again.
By sorting articles by tags, we are somewhat able to compare articles on the same subject, 
allowing us to see if sentiments follow subject.

Goal 5 - Plotting

We decided to plot our data based on tags and types. As a result, by individually comparing the 
article body and its comments with a sentiment list, we get an average sentiment for each. 
We plot this correlation and compare the graphs for each of the three article types.
Afterwards we search our database by tags. The three most common tags are used - and articles with 
the same subject, according to tag, are compared.

Lessons Learned
-----------------
We got a first feeling on how to use python and what it can do as a language by using some basic libraries such as urllib, bs4 and nltk.
Also, we understood how sentiment analysis works and the possibilities it gives us.
Finally, by using matplotlib and numpy we saw how we can plot our results.