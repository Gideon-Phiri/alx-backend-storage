#!/usr/bin/env python3
"""Module 101-students: Contains the function `top_students` for finding top students by average score in a MongoDB collection."""

def top_students(mongo_collection):
    """Returns all students sorted by average score.
    
    Args:
        mongo_collection: The pymongo collection object.
    
    Returns:
        A cursor to the list of students sorted by their average score.
    """
    return mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])

