#!/usr/bin/python3
""" 8. List all documents in Python """


def list_all(mongo_collection):
    """ lists all documents in a collection
    Args:
            mongo_collection (Collection): The name of collection.
    Returns:
            Possibally List of Docs or empty list.
    """

    return [doc for doc in mongo_collection.find()]