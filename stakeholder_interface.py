# stakeholder_interface.py
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

# ==================== TELEMETRY COLLECTOR (Embedded) ====================
class TelemetryCollector:
    def collect_all(self):
        return {
            "timestamp": str(datetime.now()),
            "siem_logs": [
                {"event": "Failed login attempt", "service": "payment-api", "severity": "HIGH"},
                {"event": "API rate limit exceeded", "service": "transaction-service", "severity": "MEDIUM"}
            ],
            "metrics": {"cpu": 67.5, "latency_p95": 245, "error_rate": 0.012},
            "service_mesh": {"topology_changes": 3, "anomalous_services": ["auth-service"]},
            "change_events": [{"type": "Deployment", "service": "payment-gateway", "version": "v2.3"}]
        }

# ==================== MAIN APP ====================
st.set_page_config(page_title="Objective 1 Dashboard", layout="wide")
st.title("🎯 Objective 1: Collaborative Threat Modelling Framework")
st.subheader("Real-time Telemetry + Multi-Stakeholder Input")

# Show Telemetry
st.markdown("### Current Telemetry Data")
collector = TelemetryCollector()
telemetry = collector.collect_all()
st.json(telemetry)

# Stakeholder Input
col1, col2 = st.columns([1, 2])

with col1:
    stakeholder = st.selectbox("Select Your Role", ["CISO", "Architect", "Compliance", "DevSecOps"])
    priority = st.slider("Risk Priority (1-10)", 1, 10, 7)

with col2:
    feedback = st.text_area("Your Comments / Actions", 
                          height=150, 
                          placeholder="Example: High risk detected in payment service...")

if st.button("Submit Feedback", type="primary"):
    if feedback.strip():
        feedback_data = {
            "stakeholder": stakeholder,
            "priority": priority,
            "feedback": feedback,
            "timestamp": str(datetime.now()),
            "telemetry_snapshot": telemetry
        }
        
        output_dir = "outputs/stakeholder_feedback"
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        filename = f"{output_dir}/{stakeholder}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(feedback_data, f, indent=2)
        
        st.success(f"✅ Feedback from **{stakeholder}** saved!")
        st.balloons()
    else:
        st.warning("Please write your feedback.")

# Show Previous Feedback
st.markdown("### Recent Feedback")
feedback_files = list(Path("outputs/stakeholder_feedback").glob("*.json")) if Path("outputs/stakeholder_feedback").exists() else []
if feedback_files:
    for file in sorted(feedback_files, reverse=True)[:5]:
        with st.expander(f"📄 {file.name}"):
            with open(file, "r") as f:
                data = json.load(f)
            st.json(data)
else:
    st.info("No feedback submitted yet.")

if __name__ == "__main__":
    st.info("Running Objective 1 Dashboard")