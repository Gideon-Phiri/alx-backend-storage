#!/usr/bin/env python3
"""Module 12-log_stats: Provides statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total number of logs
    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    # Count each HTTP method usage
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of GET requests to /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

