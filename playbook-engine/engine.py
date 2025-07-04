import json, time
from pathlib import Path
from shared.utils.logger import log

def run_playbook(alert):
    log(f"[ENGINE] Responding to {alert['type']} → {alert['details']}")

while True:
    file = Path("/app/shared/incoming_alert.json")
    if file.exists():
        with file.open() as f:
            alert = json.load(f)
        run_playbook(alert)
        file.unlink()
    time.sleep(5)
