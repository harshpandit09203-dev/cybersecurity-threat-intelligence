import os
import pickle
import numpy as np
import psycopg2

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Cybersecurity Threat Intelligence API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

DATABASE_URL = os.getenv("DATABASE_URL")
stream_events = []

def get_db():
    return psycopg2.connect(DATABASE_URL)

with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class ThreatInput(BaseModel):
    dur: float
    spkts: int
    dpkts: int
    sbytes: int
    dbytes: int
    rate: float
    sloss: int
    dloss: int
    sttl: int
    dttl: int
    sload: float
    dload: float
    ct_srv_src: int
    ct_srv_dst: int
    is_sm_ips_ports: int
    packet_ratio: float
    byte_ratio: float
    failed_login_ratio: float
    conn_freq_score: float

@app.get("/")
def health():
    return {"status": "Cybersecurity Threat Intelligence API Running 🛡️"}

@app.get("/stats")
def get_stats():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM fact_security_events")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM fact_security_events WHERE label = 1")
    attacks = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM fact_security_events WHERE label = 0")
    normal = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM fact_security_events WHERE risk_category = 'HIGH'")
    high_risk = cursor.fetchone()[0]
    conn.close()
    return {
        "total_events": total,
        "total_attacks": attacks,
        "normal_traffic": normal,
        "high_risk_events": high_risk
    }

@app.get("/alerts")
def get_alerts():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT event_id, attack_cat, threat_score, risk_category, proto, event_timestamp
        FROM fact_security_events
        WHERE label = 1
        ORDER BY threat_score DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()
    conn.close()
    return {
        "alerts": [
            {
                "event_id": r[0],
                "attack_category": r[1],
                "threat_score": r[2],
                "risk_category": r[3],
                "protocol": r[4],
                "timestamp": str(r[5])
            }
            for r in rows
        ]
    }

@app.get("/top-attacks")
def top_attacks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT attack_cat, COUNT(*) as total
        FROM fact_security_events
        WHERE label = 1
        GROUP BY attack_cat
        ORDER BY total DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return {
        "top_attacks": [{"attack": r[0], "count": r[1]} for r in rows]
    }

@app.post("/predict")
def predict_threat(data: ThreatInput):
    values = np.array([[
        data.dur, data.spkts, data.dpkts, data.sbytes, data.dbytes,
        data.rate, data.sloss, data.dloss, data.sttl, data.dttl,
        data.sload, data.dload, data.ct_srv_src, data.ct_srv_dst,
        data.is_sm_ips_ports, data.packet_ratio, data.byte_ratio,
        data.failed_login_ratio, data.conn_freq_score
    ]])
    scaled = scaler.transform(values)
    prediction = model.predict(scaled)[0]
    probability = float(model.predict_proba(scaled)[0][1])
    threat_score = round(probability * 100, 2)
    risk = "LOW"
    if threat_score >= 70:
        risk = "HIGH"
    elif threat_score >= 40:
        risk = "MEDIUM"
    return {
        "prediction": int(prediction),
        "attack_probability": probability,
        "threat_score": threat_score,
        "risk_category": risk
    }

@app.get("/stream")
def get_stream():
    return {"events": stream_events[-20:]}

@app.post("/stream-event")
def add_stream_event(event: dict):
    stream_events.append(event)
    if len(stream_events) > 100:
        stream_events.pop(0)
    return {"status": "event added"}
