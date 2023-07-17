#!/usr/bin/python3
""" 9. Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs
    Args:
            mongo_collection (Collection): The name of collection.
            **kwargs (dict): Dictionary returns attrs to insert.
    Returns:
            _id of the Document that inserted.
    """

    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
