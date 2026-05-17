import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

API_URL = "https://cybersecurity-threat-intelligence-api.onrender.com"

st.set_page_config(
    page_title="Cybersecurity Threat Intelligence",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Cybersecurity Threat Intelligence Platform")

st.markdown(
    "AI-Powered Real-Time Network Threat Detection & Security Analytics"
)

st.markdown("---")

try:

    stats = requests.get(
        f"{API_URL}/stats"
    ).json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🌐 Total Events",
        f"{stats['total_events']:,}"
    )

    col2.metric(
        "🚨 Total Attacks",
        f"{stats['total_attacks']:,}"
    )

    col3.metric(
        "✅ Normal Traffic",
        f"{stats['normal_traffic']:,}"
    )

    col4.metric(
        "🔴 High Risk",
        f"{stats['high_risk_events']:,}"
    )

except Exception as e:

    st.error(
        f"API Connection Failed: {e}"
    )

st.markdown("---")

st.subheader("📊 Top Attack Categories")

top = requests.get(
    f"{API_URL}/top-attacks"
).json()

df_attacks = pd.DataFrame(
    top["top_attacks"]
)

fig = px.bar(
    df_attacks,
    x="attack",
    y="count",
    color="count",
    color_continuous_scale="Reds",
    title="Cyber Attack Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("⚡ Live Threat Stream")

auto_refresh = st.toggle(
    "Auto Refresh (every 3 sec)",
    value=False
)

stream_placeholder = st.empty()

try:
    stream = requests.get(
        f"{API_URL}/stream"
    ).json()
    events = stream.get("events", [])
    if events:
        df_stream = pd.DataFrame(events)
        stream_placeholder.dataframe(
            df_stream,
            use_container_width=True
        )
    else:
        stream_placeholder.info(
            "No live events yet — run Kafka simulation"
        )
except:
    stream_placeholder.error("Stream not available")


st.markdown("---")

st.subheader("🚨 Recent Threat Alerts")

alerts = requests.get(
    f"{API_URL}/alerts"
).json()

df_alerts = pd.DataFrame(
    alerts["alerts"]
)

st.dataframe(
    df_alerts,
    use_container_width=True
)

st.markdown("---")

st.subheader("🔍 Real-Time Threat Scanner")

col1, col2, col3 = st.columns(3)

with col1:

    dur = st.number_input(
        "Duration",
        value=0.001
    )

    spkts = st.number_input(
        "Source Packets",
        value=2
    )

    dpkts = st.number_input(
        "Destination Packets",
        value=0
    )

    sbytes = st.number_input(
        "Source Bytes",
        value=500
    )

    dbytes = st.number_input(
        "Destination Bytes",
        value=0
    )

    rate = st.number_input(
        "Traffic Rate",
        value=90000.0
    )

    sloss = st.number_input(
        "Source Loss",
        value=0
    )

with col2:

    dloss = st.number_input(
        "Destination Loss",
        value=0
    )

    sttl = st.number_input(
        "Source TTL",
        value=254
    )

    dttl = st.number_input(
        "Destination TTL",
        value=0
    )

    sload = st.number_input(
        "Source Load",
        value=0.0
    )

    dload = st.number_input(
        "Destination Load",
        value=0.0
    )

    ct_srv_src = st.number_input(
        "CT Service Source",
        value=2
    )

    ct_srv_dst = st.number_input(
        "CT Service Destination",
        value=2
    )

with col3:

    is_sm_ips_ports = st.selectbox(
        "Same IP Ports?",
        [0, 1]
    )

    packet_ratio = st.number_input(
        "Packet Ratio",
        value=1.0
    )

    byte_ratio = st.number_input(
        "Byte Ratio",
        value=1.0
    )

    failed_login_ratio = st.number_input(
        "Failed Login Ratio",
        value=0.0
    )

    conn_freq_score = st.number_input(
        "Connection Frequency Score",
        value=4.0
    )

if st.button(
    "🔍 Scan Network Traffic",
    type="primary"
):

    payload = {
        "dur": dur,
        "spkts": int(spkts),
        "dpkts": int(dpkts),
        "sbytes": int(sbytes),
        "dbytes": int(dbytes),
        "rate": rate,
        "sloss": int(sloss),
        "dloss": int(dloss),
        "sttl": int(sttl),
        "dttl": int(dttl),
        "sload": sload,
        "dload": dload,
        "ct_srv_src": int(ct_srv_src),
        "ct_srv_dst": int(ct_srv_dst),
        "is_sm_ips_ports": int(is_sm_ips_ports),
        "packet_ratio": packet_ratio,
        "byte_ratio": byte_ratio,
        "failed_login_ratio": failed_login_ratio,
        "conn_freq_score": float(conn_freq_score)
    }

    result = requests.post(
        f"{API_URL}/predict",
        json=payload
    ).json()

    st.markdown("---")

    st.subheader("🛡️ Threat Detection Result")

    if result["risk_category"] == "HIGH":

        st.error(
            f"🚨 HIGH RISK DETECTED | Threat Score: {result['threat_score']} | Attack Probability: {result['attack_probability']:.2%}"
        )

    elif result["risk_category"] == "MEDIUM":

        st.warning(
            f"⚠️ MEDIUM RISK DETECTED | Threat Score: {result['threat_score']}"
        )

    else:

        st.success(
            f"✅ LOW RISK | Threat Score: {result['threat_score']}"
        )

    st.json(result)

st.markdown("---")

st.caption(
    "Built with FastAPI + XGBoost + Supabase + Streamlit"
)
