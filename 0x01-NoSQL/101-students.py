#!/usr/bin/python3
""" 14. Top students. """


def top_students(mongo_collection):
    """ returns all students sorted by average score.
    Args:
            mongo_collection (DB): pymongo collection object.
    Returns:
            (List[DOCS]): List of students sorted by averge score.
    """
    return mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
