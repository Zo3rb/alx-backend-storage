#!/usr/bin/env python3
""" 14. Top students. """


def top_students(mongo_collection):
    """ returns all students sorted by average score.
    Args:
            mongo_collection (DB): pymongo collection object.
    Returns:
            (List[DOCS]): List of students sorted by averge score.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
