import time, json
from pathlib import Path
from collections import Counter

counter = Counter()
while True:
    alert_path = Path("/app/shared/incoming_alert.json")
    if alert_path.exists():
        with alert_path.open() as f:
            alert = json.load(f)
            counter[alert["type"]] += 1
        alert_path.unlink()

    with open("/app/metrics.txt", "w") as f:
        for k, v in counter.items():
            f.write(f'alerts_total{{type="{k}"}} {v}\n')
        f.write('heartbeat{service="metrics_exporter"} 1\n')
    print("[METRICS] Updated")
    time.sleep(10)
