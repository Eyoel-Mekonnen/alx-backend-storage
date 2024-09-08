#!/usr/bin/env python3
"""stores instance of redis."""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def replay(method: Callable) -> None:
    """Return the replay of our history call."""
    function_input = method.__qualname__ + ":inputs"
    function_output = method.__qualname__ + ":outputs"
    instance = method.__self__
    method_input = instance._redis.lrange(function_input, 0, -1)
    method_output = instance._redis.lrange(function_output, 0, -1)
    
    print("Cache.store was called {} times:".format(len(method_input)))
    for inputs, outputs in zip(method_input, method_output):
        input_hs = inputs.decode('utf-8')
        output_hs = outputs.decode('utf-8')
        print("{}(*{}) -> {}".format(method.__qualname__, input_hs, output_hs))    
    


def call_history(method: Callable) -> Callable:
    """Store input and output history."""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Call the function that is passed."""
        input_argument = str(args)
        self._redis.rpush(input_key, input_argument)
        result = method(self, *args, **kwargs)
        result = str(result)
        self._redis.rpush(output_key, result)
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Count how much each method was called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Call the function that is passed."""
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache():
    """cache class."""

    def __init__(self):
        """Create a new database each and then flushes it."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key and store the input."""
        random = str(uuid.uuid4())
        self._redis.set(random, data)
        return random
    
    @call_history
    @count_calls
    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Get value of assocaited key."""
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(data)
    
    @call_history
    @count_calls
    def get_str(self, data: bytes) -> str:
        """Convert byte to string."""
        string = data.decode('utf-8')
        return string
    
    @call_history
    @count_calls
    def get_int(self, data: bytes) -> int:
        """Convert byte to string."""
        integer = int(data.decode('utf-8'))
        return integer
