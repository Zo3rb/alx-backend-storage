#!/usr/bin/python3
""" 10. Change school topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name.
    Args:
            mongo_collection (Collection): The name of collection.
            name (str): Document's filter with name attr.
            topics (list[str]): List of the strings to add to docs.
    Returns: None.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
