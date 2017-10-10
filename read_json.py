#!/usr/bin/python3

import json

def readJson(path = "json/UserRegistry_meta.json"):
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data
    
def docFromJson(path = "json/UserRegistry_meta.json"):
    json_data = readJson(path)
    return json_data["output"]["devdoc"]
    

if __name__ == "__main__":
    doc = docFromJson()
    title, author = doc["title"], doc["author"]
    methods = doc["methods"]
