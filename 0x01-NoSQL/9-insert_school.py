#!/usr/bin/env python3
"""Module 9-insert_school: Contains the function `insert_school` for inserting a document into a MongoDB collection."""

def insert_school(mongo_collection, **kwargs):
    """Insert a new document into a MongoDB collection.
    
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The key-value pairs representing the document fields.
    
    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id

