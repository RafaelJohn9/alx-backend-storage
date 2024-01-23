#!/usr/bin/env python3
"""
a python script that provides some stats about nginx logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    numOfLogs = nginx_logs.count_documents({})
    print(numOfLogs)

    methods = {
            "GET": 0,
            "POST": 0,
            "PUT": 0,
            "PATCH": 0,
            "DELETE": 0
            }
    for method in nginx_logs.find().method:
        methods[method] += 1

    for key, value in methods.items():
        print(f"method {key}: {value}")
