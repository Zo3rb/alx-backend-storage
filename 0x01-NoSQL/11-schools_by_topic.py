#!/usr/bin/python3
""" 11. Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic.
    Args:
            mongo_collection (Collection): The name of collection.
            topics (str): Filtered STR to search in docs.
    Returns:
            (List[DOCS]): Documents those have topic filtered.
    """

    return [doc for doc in mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic, }, }, })]
