from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.packet import get_packets, get_alerts, get_protocol_stats, get_top_talkers, insert_alert
from capture.packet_capture import start_capture, stop_capture, is_running

api = Blueprint("api", __name__)

@api.route("/capture/start", methods=["POST"])
@jwt_required()
def start():
    from app import socketio
    return jsonify(start_capture(socketio))

@api.route("/capture/stop", methods=["POST"])
@jwt_required()
def stop():
    return jsonify(stop_capture())

@api.route("/capture/status", methods=["GET"])
@jwt_required()
def status():
    return jsonify({"running": is_running()})

@api.route("/packets", methods=["GET"])
@jwt_required()
def packets():
    filters = {}
    if proto := request.args.get("protocol"):
        filters["protocol"] = proto
    if request.args.get("anomaly") == "true":
        filters["anomaly"] = True
    return jsonify(get_packets(filters))

@api.route("/alerts", methods=["GET"])
@jwt_required()
def alerts():
    return jsonify(get_alerts())

@api.route("/analytics/protocols", methods=["GET"])
@jwt_required()
def protocols():
    return jsonify(get_protocol_stats())

@api.route("/analytics/top-talkers", methods=["GET"])
@jwt_required()
def top_talkers():
    return jsonify(get_top_talkers())