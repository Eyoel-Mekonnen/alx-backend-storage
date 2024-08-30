#!/usr/bin/env python3
"""Return inserted id."""


def insert_school(mongo_collection, **kwargs):
    """Return inserted id"""
    output = mongo_collection.insert_one(kwargs)
    return output.inserted_id
