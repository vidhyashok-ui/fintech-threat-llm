from telemetry_collector import TelemetryCollector
from abstraction_layer import TelemetryAbstractionLayer
import json
from pathlib import Path

def run_objective1():
    Path("outputs/objective1").mkdir(parents=True, exist_ok=True)
    
    # Step 1: Collect Telemetry
    collector = TelemetryCollector()
    raw_data = collector.collect_all()
    
    # Step 2: Abstract + Compress
    abstraction = TelemetryAbstractionLayer()
    context = abstraction.process(raw_data)
    
    # Step 3: Save Compressed Context for Objective 2
    output_file = f"outputs/objective1/compressed_context_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(output_file, "w") as f:
        json.dump(context, f, indent=2)
    
    print(f"✅ Objective 1 Completed! Compressed context saved → {output_file}")
    return context

if __name__ == "__main__":
    run_objective1()