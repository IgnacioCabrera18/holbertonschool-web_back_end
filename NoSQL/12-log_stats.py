#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = collection.count_documents({})
    print("{} logs".format(count_logs))

    print("Methods:")
    for method in methods:
        count_method = collection.count_documents({"method": method})
        print("    method {}: {}".format(method, count_method))

    check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(check))
