#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
import json
import pymongo


# In[2]:


couch=couchdb.Server('http://admin:epn2020@localhost:5984/')
db= couch['en_venta']

MONGODB_DATABASE = 'examen'

try:
    client = pymongo.MongoClient('mongodb+srv://esfot:esfot@cluster0.yy6tu.mongodb.net/test?retryWrites=true&w=majority')
    client.server_info()
    print ('OK -- Connected to MongoDB at server %s' % ('cluster0'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB: %s' % error)

for id in db:
    
    doc= db[id]
    json_tweet = json.dumps(doc)
    data = json.loads(json_tweet) 
    
    try:
        destination = 'en_venta'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert(data)
        print ("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, data))
    except Exception as error:
        print ("Error saving data: %s" % str(error))

