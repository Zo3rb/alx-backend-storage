#!/usr/bin/python3
""" 8. List all documents in Python """

from pymongo import MongoClient

def list_all(mongo_collection):
    """ lists all documents in a collection
    Args:
            mongo_collection (Collection): The name of collection.
    Returns:
            Possibally List of Docs or empty list.
    """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)

    return docs
