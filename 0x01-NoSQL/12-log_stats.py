#!/usr/bin/env python3
"""
a python script that provides some stats about nginx logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    numOfLogs = nginx_logs.count_documents({})
    print(numOfLogs, "logs")

    methods = [
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE"
            ]

    print("Methods:")
    for method in methods:
        value = nginx_logs.count_documents({"method": method})
        print(f"\tmethod {method}: {value}")

    print(nginx_logs.count_documents({"method": "GET", "path": "/status"}),
          "status check")
