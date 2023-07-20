#!/usr/bin/env python3
''' 0/1/2/3/4 - tasks. '''

import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """ Cache Class of Redis. """

    def __init__(self) -> None:
        """ Class's Constructor function. """

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Assing passed data to a random key and add it to redis.

        Args:
                data (Union[str, bytes, int, float]): Passed data value.

        Returns:
                key (str): The key of the saved data.
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """ Gets a value from a key using helper function.

        Args:
                key (str): the Key to look with.
                fn (Callable): Helper function to trnsform data.

        Returns:
            data (Union[str, bytes, int]).
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes]:
        """ Getting String data or b"string".

        Args:
                key (str): the key to look with.

        Returns:
                data (Union[str, bytes])
        """
        return self.get(key)

    def get_int(self, key: str) -> Union[int, bytes]:
        """ Getting Int data or b"int".

        Args:
                key (str): the key to look with.
                fn (Callable): function to convert DT to int.
        Returns:
                data (Union[int, bytes]).
        """
        return self.get(key, fn=int)

    def replay(self):
        keys = sorted([k.decode() for k in self._redis.keys("*")])
        for key in keys:
            if key == "Cache.replay":
                continue
            count = self._redis.get(key).decode()
            method_name = key.split(".")[1]
            method = getattr(self, method_name)
            inputs = [arg.decode() for arg in self._redis.lrange(key, 0, -1)]
            outputs = [self.get(arg) for arg in inputs]
            print(f"{method_name} was called {count} times:")
            for i in range(int(count)):
                print(f"{method_name}(*{inputs[i:i+1]}) -> {outputs[i]}")

