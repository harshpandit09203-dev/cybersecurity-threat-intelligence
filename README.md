# cybersecurity-threat-intelligence
# 🛡️ Cybersecurity Threat Intelligence Platform

> AI-Powered Real-Time Network Threat Detection System

[![API](https://img.shields.io/badge/API-Live-green?style=for-the-badge)](https://cybersecurity-threat-intelligence-api.onrender.com)

[![Dashboard](https://img.shields.io/badge/Dashboard-Live-red?style=for-the-badge)](https://cybersecurity-threat-intelligence-ivpn.onrender.com)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)](https://python.org)

---

## 📌 What This Does

End-to-end AI-powered cybersecurity platform that ingests network logs, detects anomalies, classifies attacks, and provides real-time threat intelligence dashboards.

---

## 🔗 Live Links

| Component | URL |
|-----------|-----|
| Streamlit Dashboard | https://cybersecurity-threat-intelligence-ivpn.onrender.com |
| FastAPI Backend | https://cybersecurity-threat-intelligence-api.onrender.com |
| API Docs | https://cybersecurity-threat-intelligence-api.onrender.com/docs |

---

## 🧠 ML Models

| Model | Type | Accuracy |
|-------|------|----------|
| XGBoost | Attack Classification | 93.93% |
| Isolation Forest | Anomaly Detection | — |
| Autoencoder | Deep Learning Anomaly Detection | — |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Data Engineering | Python, PostgreSQL, ETL Pipelines |
| Database | Supabase (PostgreSQL) |
| ML Models | XGBoost, Isolation Forest, Autoencoder |
| Backend API | FastAPI |
| Frontend Dashboard | Streamlit |
| Streaming | Kafka-style Simulation |
| Deployment | Render |

---

## 📊 Dataset

- Source: UNSW-NB15 Network Intrusion Dataset
- Records: 257,673
- Attack Types: 10 Categories
- Features: 19 Engineered Features

### Attack Categories
- Normal
- Generic
- Exploits
- Fuzzers
- DoS
- Reconnaissance
- Analysis
- Backdoor
- Shellcode
- Worms

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health Check |
| GET | /stats | Summary Statistics |
| GET | /alerts | Recent High Threat Alerts |
| GET | /top-attacks | Top Attack Types |
| POST | /predict | Real-Time Threat Prediction |
| GET | /stream | Live Kafka-Style Threat Stream |

---

## ⚙️ Features

✅ Real-Time Threat Detection  
✅ ML-Based Attack Classification  
✅ Deep Learning Anomaly Detection  
✅ Interactive Security Dashboard  
✅ Threat Score System  
✅ Risk Categorization  
✅ FastAPI Backend  
✅ Supabase Cloud Database  
✅ Streamlit Visualization  
✅ Autoencoder Neural Network  
✅ Kafka-Style Streaming Simulation  
✅ Slack Alert Integration  
✅ Email Alert Integration  
✅ ETL Pipeline  
✅ REST API Architecture  

---

## 📈 Model Performance

### XGBoost
- Accuracy: 93.93%
- F1 Score: 95.25%

### Random Forest
- Accuracy: 93.87%
- F1 Score: 95.18%

### Isolation Forest
- Unsupervised Anomaly Detection

### Autoencoder
- Deep Learning-Based Reconstruction Error Detection

---

## 🚀 Deployment

### Backend
- FastAPI deployed on Render

### Frontend
- Streamlit Dashboard deployed on Render

### Database
- PostgreSQL hosted on Supabase

---

## 📡 Real-Time Streaming

Kafka-style streaming simulation implemented using:

- Python Queue
- Multi-threading
- Producer / Consumer Architecture
- Live Stream API Endpoint
- Real-Time Streamlit Monitoring

---

## 🚨 Alerting System

Integrated Real-Time Alerting:

- Slack Webhook Notifications
- Email Threat Alerts
- High-Risk Attack Detection Alerts
- Live Threat Monitoring

---

## 📂 Project Structure

bash
cybersecurity-threat-intelligence/
├── README.md
├── api.py
├── app.py
├── kafka_simulation.py
├── autoencoder_model.keras
├── notebooks/
├── requirements.txt
├── runtime.txt
├── scaler.pkl
├── xgb_model.pkl


---

## 👤 Author

*Harsh Pandit*  
Founder @ Nexport Trade | B.Sc. Computer Science  

GitHub: [@harshpandit09203-dev](https://github.com/harshpandit09203-dev)
