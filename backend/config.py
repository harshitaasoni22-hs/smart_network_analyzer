import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = "super-secret-change-me"
    MONGO_URI = "mongodb://localhost:27017/network_analyzer"
    REDIS_URL = "redis://localhost:6379/0"
    JWT_SECRET_KEY = "jwt-secret"
    CAPTURE_INTERFACE = "eth0"
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"