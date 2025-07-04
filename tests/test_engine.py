import sys
import os
import json
import pytest
from pathlib import Path

# Add playbook-engine directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../playbook-engine")))

from engine import run_playbook

def test_run_playbook_prints(capfd):
    alert = {
        "type": "high_gas",
        "details": "unit test triggered"
    }
    run_playbook(alert)
    out, _ = capfd.readouterr()
    assert "Responding to high_gas" in out

