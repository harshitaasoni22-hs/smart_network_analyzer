\# 🔍 Smart Network Traffic Analyzer



<div align="center">



!\[Dashboard Preview](assets/dashboard-preview.png)



\*\*Real-time network traffic monitoring with ML-powered anomaly detection\*\*



!\[Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square\&logo=python)

!\[Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square\&logo=flask)

!\[MongoDB](https://img.shields.io/badge/MongoDB-8.0-green?style=flat-square\&logo=mongodb)

!\[React](https://img.shields.io/badge/React-18-61dafb?style=flat-square\&logo=react)

!\[scikit-learn](https://img.shields.io/badge/ML-IsolationForest-orange?style=flat-square\&logo=scikit-learn)



</div>



\---



\## 📌 Overview



A full-stack cybersecurity tool that monitors network traffic in real time, stores packets in MongoDB, detects anomalous behavior using an unsupervised ML model (Isolation Forest), and visualizes everything on a live glassmorphism dashboard.



> Built as a portfolio project demonstrating skills in backend engineering, real-time systems, machine learning, and modern frontend design.



\---



\## ✨ Features



| Feature | Description |

|---|---|

| 🔴 Live Packet Capture | Real-time packet sniffing via PyShark/tshark |

| 🧠 ML Anomaly Detection | Isolation Forest — no labeled data needed |

| 📊 Live Dashboard | React + glassmorphism UI, updates every 2s |

| 🔒 JWT Authentication | Secure API access with token-based auth |

| 📡 WebSocket Streaming | Flask-SocketIO pushes packets to browser instantly |

| 🗄️ MongoDB Storage | Schema-less packet storage with aggregation analytics |

| 📈 Protocol Analytics | Live protocol distribution with animated bars |

| 👤 Top Talkers | Most active source IPs by traffic volume |

| 📥 CSV Export | Download captured packets as spreadsheet |

| ⚙️ Async Tasks | Celery + Redis for scheduled ML retraining |



\---



\## 🛠️ Tech Stack



&#x20;   Frontend   →   React 18, Recharts, Socket.IO Client

&#x20;   Backend    →   Python 3.12, Flask 3.1, Flask-SocketIO

&#x20;   Database   →   MongoDB 8.0 (pymongo)

&#x20;   ML Engine  →   scikit-learn — Isolation Forest

&#x20;   Auth       →   Flask-JWT-Extended (JWT tokens)

&#x20;   Queue      →   Celery + Redis

&#x20;   Capture    →   PyShark (Wireshark/tshark wrapper)



\---



\## 📁 Project Structure



&#x20;   smart-network-analyzer/

&#x20;   ├── backend/

&#x20;   │   ├── app.py                  # Flask entry point

&#x20;   │   ├── config.py               # Configuration

&#x20;   │   ├── api/

&#x20;   │   │   ├── routes.py           # REST API endpoints

&#x20;   │   │   └── auth.py             # JWT login

&#x20;   │   ├── capture/

&#x20;   │   │   └── packet\_capture.py   # Live packet capture

&#x20;   │   ├── models/

&#x20;   │   │   └── packet.py           # MongoDB models

&#x20;   │   ├── ml/

&#x20;   │   │   └── anomaly\_detector.py # Isolation Forest ML

&#x20;   │   └── tasks/

&#x20;   │       └── celery\_tasks.py     # Background jobs

&#x20;   └── frontend/

&#x20;       └── src/

&#x20;           └── components/

&#x20;               └── Dashboard.jsx   # Glassmorphism dashboard



\---



\## 🚀 Getting Started



\### Prerequisites

\- Python 3.10+

\- Node.js 16+

\- MongoDB (running on port 27017)



\### Backend Setup



&#x20;   cd backend

&#x20;   python -m venv venv

&#x20;   venv\\Scripts\\activate

&#x20;   pip install -r requirements.txt

&#x20;   py app.py



\### Frontend Setup



&#x20;   cd frontend

&#x20;   npm install

&#x20;   npm start



Open http://localhost:3000 — click Login then Start Capture



\## 🧠 How the ML Works



1\. Each packet → 5-feature vector: length, src\_port, dst\_port, protocol\_encoded, ttl

2\. Isolation Forest isolates anomalies — rare packets get isolated faster

3\. Returns anomaly score — more negative = more suspicious

4\. Model retrains every hour on latest 10,000 packets



\---



\## 📡 API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| POST | /auth/login | Get JWT token |

| POST | /api/capture/start | Start packet capture |

| POST | /api/capture/stop | Stop packet capture |

| GET | /api/packets | Get recent packets |

| GET | /api/analytics/protocols | Protocol distribution |

| GET | /api/export/csv | Download as CSV |



\---



\## 🔮 Future Improvements



\- \[ ] GeoIP mapping — world map of traffic

\- \[ ] Port scan detection

\- \[ ] Docker Compose deployment

\- \[ ] Email/Slack alerts on anomalies

\- \[ ] PCAP file upload for offline analysis



\---



\## 👩‍💻 Author



\*\*Harshita Soni\*\*

GitHub: \[@harshitaasoni22-hs](https://github.com/harshitaasoni22-hs)



\---



<div align="center">

⭐ Star this repo if you found it useful!

</div>

