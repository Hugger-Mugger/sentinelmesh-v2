import json, time
from pathlib import Path

while True:
    path = Path("/app/shared/alert.json")
    if path.exists():
        with path.open() as f:
            alert = json.load(f)
        with open("/app/shared/incoming_alert.json", "w") as f:
            json.dump(alert, f)
        print("[DISPATCHER] Alert relayed")
    time.sleep(5)
