import json, time
from pathlib import Path
from random import choice

types = ["high_gas", "phishing_activity", "contract_impersonation"]
contracts = ["0xabc...", "0xdef...", "0xdeadbeef..."]

for i in range(5):
    alert = {
        "type": choice(types),
        "details": f"Test burst from {choice(contracts)}"
    }
    Path("/app/shared/incoming_alert.json").write_text(json.dumps(alert))
    print(f"[BURST] Alert {i+1}: {alert}")
    time.sleep(2)
