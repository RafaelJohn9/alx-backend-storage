#!/usr/bin/env python3
"""
a python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists doc in collection {mongodb}
    """
    cursor = mongo_collection.find()
    
    documents = list(cursor)
    return documents
