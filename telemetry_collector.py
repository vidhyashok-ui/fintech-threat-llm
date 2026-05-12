import requests
import json
from datetime import datetime
from config import Config

class TelemetryCollector:
    def collect_all(self):
        data = {
            "timestamp": str(datetime.now()),
            "siem_logs": self._collect_siem(),
            "metrics": self._collect_metrics(),
            "service_mesh": self._collect_service_mesh(),
            "change_events": self._collect_changes()
        }
        return data
    
    def _collect_siem(self):
        # Simulate or connect to real SIEM (ELK, Splunk, etc.)
        return [
            {"event": "Failed login attempt", "service": "payment-api", "severity": "HIGH"},
            {"event": "API rate limit exceeded", "service": "transaction-service", "severity": "MEDIUM"}
        ]
    
    def _collect_metrics(self):
        return {"cpu": 67.5, "latency_p95": 245, "error_rate": 0.012}
    
    def _collect_service_mesh(self):
        return {"topology_changes": 3, "anomalous_services": ["auth-service"]}
    
    def _collect_changes(self):
        return [{"type": "Deployment", "service": "payment-gateway", "version": "v2.3"}]