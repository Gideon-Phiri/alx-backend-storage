#!/usr/bin/env python3
"""Module 10-update_topics: Contains the function `update_topics` for updating the topics of a document in a MongoDB collection."""

def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document in a MongoDB collection.
    
    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to update.
    
    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

