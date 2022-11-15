import json
import re

imported_json_file = open('small.json')
imported_json = json.load(imported_json_file)
i = 0
nrql_queries = {}

for data in imported_json:
    for i in data['patterns']:
        query = ""
        if i[:6] == "where(":
            query = i[6:-1]
        else:
            query = i
        query = re.sub(r'(?<!\\)/','÷÷÷',query) #changing to ÷÷÷ so that other special characters can be dealt with 
        query = re.sub(r'([+\-&|!(){}\[\]^"~\*\?:])',r'\\\1',query) #/ are preceeded by \ already so not adding
        query = re.sub('÷÷÷','"',query) #changing back to ""
        query = re.sub(r'(?:\bNOT\b |\bNOT\b)', "-", query) 
        nrql_queries[i] = query
