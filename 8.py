#!/usr/bin/env python
# coding: utf-8

# In[1]:


from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json


# In[5]:


CLIENT = pymongo.MongoClient('mongodb://localhost:27017')
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

DBS = ['examen']

SERVER = pymongo.MongoClient('mongodb+srv://esfot:esfot@cluster0.yy6tu.mongodb.net/test?retryWrites=true&w=majority')
try:
    SERVER.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBS2 = SERVER.get_database('examen')
dbsCollection2 = DBS2.en_venta

for db in DBS:
    if db in ('examen'):  
        cols = CLIENT[db].list_collection_names() 
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbsCollection2.insert_one(documents)
                    print("SAVE")
                    print(documents)
                except Exception as error:
                    print ("Error saving data: %s" % str(error))


# In[ ]:




