#!/usr/bin/env python3
"""
a Cache class
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    this is a a cache class used in redis
    """
    def __init__(self):
        """
        stores the attr of the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a  random key and stores
        data with the random key generated
        """
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey
