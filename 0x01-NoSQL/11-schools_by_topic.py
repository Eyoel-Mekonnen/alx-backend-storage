#!/usr/bin/env python3
"""Update a document."""


def schools_by_topic(mongo_collection, topic):
    """Return list of school with specific topic."""
    topic = mongo_collection.find({'topics': topic})
    return list(topic)
