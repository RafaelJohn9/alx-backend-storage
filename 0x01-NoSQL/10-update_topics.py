#!/usr/bin/env python3
"""
Write a python function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes topos of a school document
    """
    updated = mongo_collection.update({"name": name}, {"$set": {"topics": topics}})
