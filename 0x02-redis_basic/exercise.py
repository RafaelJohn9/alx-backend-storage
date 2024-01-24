#!/usr/bin/env python3
"""
a Cache class
"""
import uuid
import redis
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    methodName = method.__qualname__

    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """ Wrapper function that increments a key in Redis"""
        self._redis.incr(methodName)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to track method calls and their inputs/outputs in Redis"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper that records input and output data in Redis lists."""
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output_data = method(self, *args)
        self._redis.rpush(output_key, output_data)
        return output_data

    return wrapper


def replay(method: Callable) -> None:
    """function to display the history of calls of a particular function."""
    client = redis.Redis()

    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    in_data = client.lrange(in_key, 0, -1)
    out_data = client.lrange(out_key, 0, -1)
    zippy = list(zip(in_data, out_data))

    print("{} was called {} times:".format(method.__qualname__, len(zippy)))

    for value, r_id in zippy:
        print("{}(*{}) -> {}".format(
            method.__qualname__,
            value.decode("utf-8"),
            r_id.decode("utf-8")))


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

    @count_calls
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
        return None

    def get_str(self, key: str) -> str:
        """
        Retrieves a string from cache using a specified key
        """
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """
        Retrieves a int from cache using a specified key
        """
        return int(self._redis.get(key))
