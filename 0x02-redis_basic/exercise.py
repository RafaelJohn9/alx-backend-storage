#!/usr/bin/env python3
"""
a Cache class
"""
import uuid
import redis
from typing import Union, Callable


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

    def get(self,
            key: str,
            fn: Callable = None
            ) -> Union[str, int, float, bytes]:
        """
        converts utf8 strings back to strings from bin
        """
        value = self._redis.get(key)
        if value is not None:
            return fn(value) if fn is not None else value
        else:
            return None

    def get_str(self, key:str) -> str:
        """
        Retrieves a string from cache using a specified key
        """
        return str(self._redis.get(key))

    def get_int(self, key:str) -> int:
        """
        Retrieves a int from cache using a specified key
        """
        return int(self._redis.get(key))
