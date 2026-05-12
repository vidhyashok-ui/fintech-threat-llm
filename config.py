import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # LLM Settings
    LLM_MODEL = "meta-llama/Llama-3.2-3B-Instruct"   # Use 1B or 3B for local testing
    EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
    
    # Telemetry
    SIEM_ENDPOINT = "http://localhost:8080/siem"
    PROMETHEUS_URL = "http://localhost:9090"
    
    # Output
    OUTPUT_DIR = "outputs/objective1"
    
    # Stakeholders
    STAKEHOLDERS = ["CISO", "Architect", "Compliance", "DevSecOps"]

    # Paths
    SAMPLE_DIR = "data/samples"
    KNOWLEDGE_BASE = "data/knowledge_base"
    OUTPUT_DIR = "outputs"
    
    # Neo4j
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
    
    # PCI-DSS Controls (you can expand this)
    PCI_CONTROLS = {
        "6.4": "Change control processes",
        "10.2": "Implement audit trails",
        "11.3": "Regular testing of security systems"
    }

      