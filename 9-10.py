#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pymongo
import pandas as pd


# In[3]:


MONGODB_DATABASE = 'examen'

try:
    client = pymongo.MongoClient('mongodb+srv://esfot:esfot@cluster0.yy6tu.mongodb.net/test?retryWrites=true&w=majority')
    client.server_info()
    print ('OK -- Connected to MongoDB Atlas at server %s' % ('cluster0'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB Atlas connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB Atlas: %s' % error)

db = client.examen
col = db.en_venta
    
my_cursor = col.find()

aux=[]
for item in my_cursor:
    aux.append(item)
    
pd.DataFrame([aux]).to_csv('en_venta.csv', index=False)


# In[ ]:




