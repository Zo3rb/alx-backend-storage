#!/usr/bin/python3
""" 15. Log stats - new version. """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print(f"{logs_collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = logs_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = logs_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
