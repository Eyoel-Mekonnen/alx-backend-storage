#!/usr/bin/env python3
"""update a doc with specific attribute."""


def update_topics(mongo_collection, name, topics):
    """Update the update topics."""
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
