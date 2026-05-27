import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import threading

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, n_estimators=100, random_state=42)
        self._lock = threading.Lock()
        self._is_trained = False
        self._proto_classes = ["TCP","UDP","DNS","HTTP","HTTPS","ICMP","ARP","OTHER"]
        self._enc = LabelEncoder()
        self._enc.fit(self._proto_classes)

    def _features(self, pkt):
        proto = pkt.get("protocol","OTHER")
        if proto not in self._proto_classes:
            proto = "OTHER"
        return np.array([
            float(pkt.get("length", 0)),
            float(pkt.get("src_port") or 0),
            float(pkt.get("dst_port") or 0),
            float(self._enc.transform([proto])[0]),
            float(pkt.get("ttl") or 64),
        ]).reshape(1, -1)

    def train(self, packets):
        if len(packets) < 50:
            return
        X = np.vstack([self._features(p) for p in packets])
        with self._lock:
            self.model.fit(X)
            self._is_trained = True

    def predict(self, pkt):
        if not self._is_trained:
            return False, 0.0
        X = self._features(pkt)
        with self._lock:
            pred = self.model.predict(X)[0]
            score = self.model.decision_function(X)[0]
        return (pred == -1), float(score)
    