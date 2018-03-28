# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:05:58 2018

@author: Ajanta
"""
import requests
import json
from elasticsearch import Elasticsearch,helpers

es= Elasticsearch([{'host': 'localhost', 'port': 9200}])

r = requests.get('http://localhost:9200') 

def push(fp):
    
      doc=  {"_index":"products",
    "_type":"snapdeal",
    "_source":json.loads(fp.read())
    }
      yield(doc)
fp = open("snapdeal.json",'r')
    #es.create(index='products',doc_type='snapdeal',id=i,body=None)
helpers.bulk(actions=push(fp),client=es)
    
res = es.search(index="products", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
