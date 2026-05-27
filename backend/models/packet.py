from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/network_analyzer")
db = client.get_default_database()

packets_col = db["packets"]
alerts_col  = db["alerts"]

packets_col.create_index([("timestamp", DESCENDING)])
packets_col.create_index([("src_ip", ASCENDING)])
packets_col.create_index([("protocol", ASCENDING)])
alerts_col.create_index([("timestamp", DESCENDING)])

def insert_packet(pkt_dict):
    pkt_dict["timestamp"] = pkt_dict.get("timestamp", datetime.utcnow().isoformat())
    return packets_col.insert_one(pkt_dict)

def insert_alert(alert_dict):
    alert_dict["timestamp"] = datetime.utcnow().isoformat()
    alert_dict["resolved"] = False
    return alerts_col.insert_one(alert_dict)

def get_packets(filters={}, limit=200, skip=0):
    return list(packets_col.find(filters, {"_id": 0})
                .sort("timestamp", DESCENDING).skip(skip).limit(limit))

def get_alerts(resolved=False, limit=50):
    return list(alerts_col.find({"resolved": resolved}, {"_id": 0})
                .sort("timestamp", DESCENDING).limit(limit))

def get_protocol_stats():
    pipeline = [
        {"$group": {"_id": "$protocol", "count": {"$sum": 1},
                    "total_bytes": {"$sum": "$length"}}},
        {"$sort": {"count": -1}}
    ]
    return list(packets_col.aggregate(pipeline))

def get_top_talkers(limit=10):
    pipeline = [
        {"$group": {"_id": "$src_ip", "packets": {"$sum": 1},
                    "bytes": {"$sum": "$length"}}},
        {"$sort": {"bytes": -1}},
        {"$limit": limit}
    ]
    return list(packets_col.aggregate(pipeline))