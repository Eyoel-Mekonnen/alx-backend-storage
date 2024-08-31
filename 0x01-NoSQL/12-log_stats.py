#!/usr/bin/env python3
"""Counts log based on request type and status."""
from pymongo import MongoClient


def nginx_request_log(nginx):
    """Print logs and status."""
    documents = nginx.aggregate([
        {"$count": "TotalCount"}
    ])
    documents = list(documents)
    if documents:
        print("{} logs".format(documents[0]['TotalCount']))
    else:
        print("0 logs")
    values = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for val in values:
        result = nginx.aggregate([
            {"$match": {'method': val}},
            {"$group": {"_id": "$method", "count": {"$sum": 1}}}
        ])
        result = list(result)
        if result:
            count = result[0]['count']
            print("\tmethod {}: {}".format(val, count))
        else:
            print("\tmethod {}: 0".format(val))
    result2 = nginx.aggregate([
        {"$match": {'method': 'GET', 'path': '/status'}},
        {"$group": {"_id": {"method": "$method",
                    "path": "$path"}, "count": {"$sum": 1}}}
    ])
    result2 = list(result2)
    if result2:
        count = result2[0]['count']
        print("{} status check".format(count))
    else:
        print("0 status check")


def start():
    """Start the mongo db."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_request_log(client.logs.nginx)


if __name__ == '__main__':
    start()
