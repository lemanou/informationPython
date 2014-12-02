Information.dk tutorial
==============================================================
Short description
--------------------------------------------------------------

Assuming that all the packages are installed, the user needs to run main.py.
The script will first ask the user if this is the first time they are running this code.
If yes, a new couchdb will be created, else the old one will be loaded.
After that the script will parse the main page of the news site and the sentiment will be calculated.
Hereafter, the code will again connect to the news page to fetch any missing tags from the "normal" articles.
Then the plotting begins. Three plots with tags will appear and after that three more by type.