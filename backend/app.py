from flask import Flask
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, origins="*")
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
jwt = JWTManager(app)

from api.routes import api
from api.auth import auth_bp

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/auth")

@socketio.on("connect")
def on_connect():
    print("Client connected")

@socketio.on("disconnect")
def on_disconnect():
    print("Client disconnected")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)