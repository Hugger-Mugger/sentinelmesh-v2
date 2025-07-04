import json, sys
from pathlib import Path

alert = {
    "type": sys.argv[1] if len(sys.argv) > 1 else "high_gas",
    "details": "Manually injected for testing"
}

Path("/app/shared/incoming_alert.json").write_text(json.dumps(alert))
print(f"[TESTER] Injected manual alert: {alert}")
