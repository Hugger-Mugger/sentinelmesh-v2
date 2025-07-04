import os, time, json, requests
from sample_logic import simulate_detection
from shared.utils.logger import log

USE_FORTE_API = os.getenv("USE_FORTE_API", "false").lower() == "true"
API_URL = os.getenv("FORTA_API_URL")
API_KEY = os.getenv("FORTA_API_KEY")

def fetch_forta_alert():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    r = requests.get(API_URL, headers=headers)
    return r.json()

while True:
    try:
        alert = fetch_forta_alert() if USE_FORTE_API else simulate_detection()
        with open("/app/shared/alert.json", "w") as f:
            json.dump(alert, f)
        log(f"[BOT] Alert dispatched: {alert}")
    except Exception as e:
        log(f"[BOT] Error: {e}")
    time.sleep(10)
