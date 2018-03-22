# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:00:46 2018

@author: Ajanta
"""

import json
from elasticsearch import Elasticsearch

query = {
    'query': {
        'match_all': {}
    }
}

elastic_obj = Elasticsearch(
    INDEX_NAME = 'products',
    TYPE_NAME = 'snapdeal'
)

f = open('products.json', 'w')
f.write(json.dumps(elastic_obj.mget(body=query)))
f.close()