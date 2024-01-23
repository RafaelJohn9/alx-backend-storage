#!/usr/bin/env python3
"""
a python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    newSchool = mongo_collection.insert_one(kwargs)
    return newSchool.inserted_id
