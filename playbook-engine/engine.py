# engine.py
import json, time
from pathlib import Path
from shared.utils.logger import log

def run_playbook(alert):
    log(f"[ENGINE] Responding to {alert['type']} → {alert['details']}")

def process_alert_file(file_path: Path):
    if file_path.exists():
        with file_path.open() as f:
            alert = json.load(f)
        run_playbook(alert)
        file_path.unlink()
        return alert  # Optional: return for test verification
    return None

def start_engine_loop():
    file_path = Path("/app/shared/incoming_alert.json")
    while True:
        process_alert_file(file_path)
        time.sleep(5)
