#!/usr/bin/env python3
"""Return document of collection."""


def list_all(mongo_collection):
    """Return the list of collection."""
    mongo_list = []
    for document in mongo_collection.find():
        mongo_list.append(document)
    return mongo_list
