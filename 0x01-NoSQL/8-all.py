#!/usr/bin/env python3
"""Module 8-all: Contains the function `list_all` for listing documents in a MongoDB collection."""

def list_all(mongo_collection):
    """List all documents in a MongoDB collection.
    
    Args:
        mongo_collection: The pymongo collection object.
    
    Returns:
        A list of documents in the collection or an empty list if the collection is empty.
    """
    return list(mongo_collection.find()) if mongo_collection else []

