# stakeholder_interface.py
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

from telemetry_collector import TelemetryCollector
from config import Config

class StakeholderInterface:
    def __init__(self):
        self.output_dir = "outputs/stakeholder_feedback"
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def run(self):
        st.set_page_config(page_title="Objective 1 - Collaborative Threat Modelling", layout="wide")
        st.title("🎯 Objective 1: Collaborative Threat Modelling Framework")
        st.subheader("Real-time Telemetry + Multi-Stakeholder Input")

        # Show Current Telemetry
        st.markdown("### Current Telemetry Data")
        collector = TelemetryCollector()
        telemetry = collector.collect_all()
        st.json(telemetry)

        # Stakeholder Input Section
        col1, col2 = st.columns([1, 2])
        
        with col1:
            stakeholder = st.selectbox("Select Your Role", Config.STAKEHOLDERS)
            priority = st.slider("Risk Priority (1 = Low, 10 = Critical)", 1, 10, 7)
        
        with col2:
            feedback = st.text_area("Your Comments / Risk Priority / Suggested Actions", 
                                  height=150, 
                                  placeholder="Example: High risk on payment service due to recent deployment...")

        if st.button("Submit Stakeholder Feedback", type="primary"):
            if feedback.strip():
                feedback_data = {
                    "stakeholder": stakeholder,
                    "priority": priority,
                    "feedback": feedback,
                    "timestamp": str(datetime.now()),
                    "telemetry_snapshot": telemetry
                }
                
                filename = f"{self.output_dir}/{stakeholder}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                
                with open(filename, "w") as f:
                    json.dump(feedback_data, f, indent=2)
                
                st.success(f"✅ Feedback from **{stakeholder}** saved successfully!")
                st.balloons()
            else:
                st.warning("Please enter your feedback before submitting.")

        # Show previously submitted feedback
        st.markdown("### Recent Stakeholder Feedback")
        feedback_files = list(Path(self.output_dir).glob("*.json"))
        if feedback_files:
            for file in sorted(feedback_files, reverse=True)[:5]:
                with st.expander(f"📄 {file.name}"):
                    with open(file, "r") as f:
                        data = json.load(f)
                    st.json(data)
        else:
            st.info("No feedback submitted yet.")

if __name__ == "__main__":
    interface = StakeholderInterface()
    interface.run()