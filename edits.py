# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:05:58 2018

@author: Ajanta
"""
import requests
import json
from elasticsearch import Elasticsearch

es= Elasticsearch([{'host': 'localhost', 'port': 9200}])

r = requests.get('http://localhost:9200') 
i = 1
while r.status_code == 200:
    r = open('snapdeal.json', 'r')
    es.index(index='products',doc_type='snapdeal',id=i,body=json.load(r))
    i=i+1
print(i)