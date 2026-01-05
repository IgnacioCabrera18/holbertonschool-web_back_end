#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
count_logs = collection.count_documents({})
print("{} logs".format(count_logs))
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count_method = collection.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, count_method))
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(status_check))

