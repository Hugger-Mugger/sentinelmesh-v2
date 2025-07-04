import sys, os, json
from pathlib import Path
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../playbook-engine")))
from engine import process_alert_file

def test_process_alert_file(tmp_path, capfd):
    # Create a mock alert file
    alert_data = {"type": "high_gas", "details": "unit test triggered"}
    alert_file = tmp_path / "incoming_alert.json"
    alert_file.write_text(json.dumps(alert_data))

    # Run the processor
    result = process_alert_file(alert_file)

    # Capture output
    out, _ = capfd.readouterr()
    assert "Responding to high_gas" in out
    assert result == alert_data
    assert not alert_file.exists()
