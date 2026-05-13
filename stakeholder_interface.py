<<<<<<< HEAD
# stakeholder_interface.py
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

class StakeholderInterface:
    def __init__(self):
        self.output_dir = "outputs/stakeholder_feedback"
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def run(self):
        st.title("🎯 Objective 1: Collaborative Threat Modelling")
        st.subheader("Real-time Telemetry + Stakeholder Input")
        
        # Show current telemetry
        collector = TelemetryCollector()
        telemetry = collector.collect_all()
        st.json(telemetry)
        
        stakeholder = st.selectbox("Your Role", Config.STAKEHOLDERS)
        
        feedback = st.text_area("Your Input / Priority / Comments", height=150)
        priority = st.slider("Risk Priority (1-10)", 1, 10, 7)
        
        if st.button("Submit Feedback"):
            feedback_data = {
                "stakeholder": stakeholder,
                "feedback": feedback,
                "priority": priority,
                "timestamp": str(datetime.now()),
                "telemetry_snapshot": telemetry
            }
            filename = f"{self.output_dir}/{stakeholder}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            with open(filename, "w") as f:
                json.dump(feedback_data, f, indent=2)
=======
# stakeholder_interface.py
import streamlit as st
from datetime import datetime
import json
from pathlib import Path

class StakeholderInterface:
    def __init__(self):
        self.output_dir = "outputs/stakeholder_feedback"
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def run(self):
        st.title("🎯 Objective 1: Collaborative Threat Modelling")
        st.subheader("Real-time Telemetry + Stakeholder Input")
        
        # Show current telemetry
        collector = TelemetryCollector()
        telemetry = collector.collect_all()
        st.json(telemetry)
        
        stakeholder = st.selectbox("Your Role", Config.STAKEHOLDERS)
        
        feedback = st.text_area("Your Input / Priority / Comments", height=150)
        priority = st.slider("Risk Priority (1-10)", 1, 10, 7)
        
        if st.button("Submit Feedback"):
            feedback_data = {
                "stakeholder": stakeholder,
                "feedback": feedback,
                "priority": priority,
                "timestamp": str(datetime.now()),
                "telemetry_snapshot": telemetry
            }
            filename = f"{self.output_dir}/{stakeholder}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            with open(filename, "w") as f:
                json.dump(feedback_data, f, indent=2)
>>>>>>> 22b7eeefedeff39bef3e10ab786a247f94befabb
            st.success(f"✅ Feedback from {stakeholder} saved!")