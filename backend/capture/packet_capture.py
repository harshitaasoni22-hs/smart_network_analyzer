import threading
import random
from datetime import datetime
from models.packet import insert_packet
from ml.anomaly_detector import AnomalyDetector

detector = AnomalyDetector()
_stop_event = threading.Event()
_capture_thread = None

PROTOCOLS = ["TCP", "UDP", "HTTP", "HTTPS", "DNS", "ICMP"]
SAMPLE_IPS = ["192.168.1.1","192.168.1.2","10.0.0.1","172.16.0.1","8.8.8.8","1.1.1.1"]

def _simulate_packet():
    return {
        "src_ip": random.choice(SAMPLE_IPS),
        "dst_ip": random.choice(SAMPLE_IPS),
        "protocol": random.choice(PROTOCOLS),
        "length": random.randint(40, 1500),
        "src_port": random.randint(1024, 65535),
        "dst_port": random.choice([80, 443, 53, 22, 8080, 3306]),
        "ttl": random.randint(32, 128),
        "timestamp": datetime.utcnow().isoformat(),
    }

def _capture_loop(socketio):
    while not _stop_event.is_set():
        batch = []
        for _ in range(10):
            pkt = _simulate_packet()
            is_anomaly, score = detector.predict(pkt)
            pkt["anomaly"] = is_anomaly
            pkt["anomaly_score"] = round(score, 4)
            insert_packet(pkt)
            batch.append(pkt)
        socketio.emit("new_packets", batch)
        anomalies = [p for p in batch if p["anomaly"]]
        if anomalies:
            socketio.emit("anomaly_detected", anomalies)
        _stop_event.wait(1)

def start_capture(socketio):
    global _capture_thread, _stop_event
    if _capture_thread and _capture_thread.is_alive():
        return {"status": "already_running"}
    _stop_event.clear()
    _capture_thread = threading.Thread(
        target=_capture_loop, args=(socketio,), daemon=True)
    _capture_thread.start()
    return {"status": "started"}

def stop_capture():
    _stop_event.set()
    return {"status": "stopped"}

def is_running():
    return _capture_thread is not None and _capture_thread.is_alive()