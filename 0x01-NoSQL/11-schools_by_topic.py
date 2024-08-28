#!/usr/bin/env python3
"""Module 11-schools_by_topic: Contains the function `schools_by_topic` for finding schools by topic in a MongoDB collection."""

def schools_by_topic(mongo_collection, topic):
    """Find all schools that have a specific topic.
    
    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.
    
    Returns:
        A cursor to the list of schools that have the specified topic.
    """
    return mongo_collection.find({"topics": topic})

