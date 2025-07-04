# 🔐 SentinelMesh

_Modular Incident Response for Web3 Protocols_  
**Respond to chaos like it’s routine.**

---

## 🧠 What is SentinelMesh?

**SentinelMesh** is a modular, real-time incident response framework for high-severity events in Web3 protocols. It ingests on-chain alerts, applies triage logic, executes YAML-defined runbooks, and orchestrates emergency actions like contract pauses and multisig transactions—all while preserving audit trails and calm coordination.

Inspired by the relentless pace of protocol defense, SentinelMesh is built to stop $100M exploits before the tweet thread goes viral.

---

## 🛠️ Key Features

- 🔐 **Multisig Watchdog**: Monitor Gnosis Safe transactions for unauthorized or anomalous behavior.
- 🧠 **Alert Triage Engine**: Ingest alerts from Forta, Cyvers, Hypernative, and others; triage using rule-based or ML patterns.
- 📜 **Runbook-as-Code**: Define response flows in YAML for predictable escalation and automation.
- 🧰 **On-Chain Response Toolkit**: Automate pausing contracts, revoking access, or triggering upgrades.
- 📝 **Audit Logging**: Log every action with incident ID, timestamp, and tx hash.
- 📡 **Signal Relay**: Send encrypted, real-time alerts to responder channels.

---

## 🤖 Example Incident Flow

1. ⚠️ Forta bot emits alert for multisig signer anomaly  
2. 🧠 Triage engine detects `high_severity` → triggers playbook `pause_protocol.yml`  
3. 🧰 Runbook executes Gnosis Safe SDK to submit pause transaction  
4. 📡 Signal bot notifies responder room with transaction hash and summary  
5. 📝 Audit logger records all steps tied to the incident ID  

---

## 🧩 Architecture Overview

```
🛰️  Alert Sources 
   (Forta, Cyvers, Hypernative)
         ↓
🧠  Triage Engine
         ↓
📜  Runbook Executor
         ↓
🔐  Multisig Actions + 📡 Signal Relay
         ↓
📝  Audit Logger
```

Modular, stateless, and designed to plug into any SOC workflow or simulation setup.

---

## 🚦 Project Status

| Component            | Status         | Notes                                                       |
|----------------------|----------------|-------------------------------------------------------------|
| 🧠 Core Architecture | ✅ Complete     | Modular detection ➝ dispatch ➝ response pipeline is functional |
| 🔁 Forta API Swap     | 🔧 Configurable | Toggle with `USE_FORTE_API`, ready for live integration      |
| 📊 Observability      | ✅ Integrated   | Grafana panel + metrics exporter in place                    |
| 🧪 Test Suite         | ⚙️ Basic        | `pytest` stub for engine module, ready to expand             |
| 🚀 CI/CD Workflow     | ✅ Enabled      | GitHub Actions: Docker build + test profile                  |
| 🛠️ Dev Utilities      | ✅ Added        | Includes burst injector, manual trigger CLI, logger, docs    |

> 📦 Version: `v1.0.0` — tagged for initial client delivery  
> ✅ CI Status: ![CI](https://img.shields.io/github/actions/workflow/status/Hugger-Mugger/sentinelmesh-v2/docker-lint.yml?branch=main)

---

## 💡 Why It Exists

Web3 protocols don’t get a second chance when things go sideways. SentinelMesh exists to deliver structure when pressure spikes—runbooks instead of chaos, decisiveness instead of panic. Built by and for protocol defenders.

---

## 🚀 Quickstart

```bash
git clone https://github.com/Hugger-Mugger/sentinelmesh-v2.git
cd sentinelmesh-v2
docker compose up --build
```

To inject an alert manually:

```bash
python cli/manual_trigger.py --type high_severity --details "Suspicious signer activity"
```

Run tests:

```bash
python -m pytest tests/test_engine.py -v
```

---

## ✍️ Author

**Abhijeet Kumar**  
Security Analyst • Protocol Defender in the Making  
[LinkedIn](https://www.linkedin.com/in/abhijeet-kumar0412/) • Email: abhijeetkumar20011204@outlook.com

---

## 🧭 Milestones

- ✅ Finalize system architecture diagram  
- ✅ Build base rule engine in Python (YAML triage parser)  
- ✅ Script sample runbooks and contract response templates  
- ✅ Integrate mock Forta alerts and simulate response pipeline  
- ✅ Publish public MVP repo on GitHub with documentation  
- 🚀 Accept community testing and plug-and-play integrations  

---

## 🔭 Future Plans

- 🧠 Expand the triage engine with scoring, clustering, and ML-based alert prioritization  
- 🔌 Build plug-and-play integrations with incident tooling (PagerDuty, Slack, Notion SOC boards)  
- 🔐 Add support for multiple on-chain response profiles (multi-chain contract libraries, role revocation)  
- 🌐 Roll out REST API or GraphQL layer for external alert injection and system introspection  
- 📦 Publish SentinelMesh as a PyPI module for simulation tooling  
- 👥 Create example replay kits using historic exploits for SOC team training  
- 🧪 Migrate to full test coverage with container mocks and scenario-driven unit tests  
- 📈 Add time-series metrics on triage performance, alert flow rate, and playbook efficiency  
- 🛡️ Harden security posture with signing, secrets encryption, and repo audit checklist  
- 📚 Publish a whitepaper explaining architecture design decisions, threat model, and future roadmap

> Got a use case worth defending against? Open a proposal or challenge the framework design. Let's battle-test before production pressure arrives.

---

## 🦾 Contributing

Got ideas? Want to battle-test use cases? Open a discussion, raise an issue, or just drop by and say hi.  
Every chaos scenario makes the mesh stronger.

> _“We don’t panic. We playbook.”_

