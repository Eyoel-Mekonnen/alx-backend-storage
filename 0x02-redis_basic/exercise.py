#!/usr/bin/env python3
"""stores instance of redis."""
import redis
import uuid
from typing import Union


class Cache():
    """cache class."""
    def __init__(self):
        """creates a new database each and then flushes it."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key and store the input."""
        random = str(uuid.uuid4())
        self._redis.set(random, data)
        return random
