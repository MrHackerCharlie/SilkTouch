# ✨ SilkTouch: High-Velocity Stealth Username OSINT Framework

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![OSINT](https://img.shields.io/badge/Field-OSINT-purple.svg?style=for-the-badge)](https://en.wikipedia.org/wiki/Open-source_intelligence)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20WSL%20%7C%20Windows-orange.svg?style=for-the-badge&logo=linux)](https://www.kali.org/)

> **"Extracting delicate footprints cleanly from the deepest layers of the surface web—without shattering the environment."**

Just like the legendary Minecraft enchantment cleanly extracts fragile blocks without breaking them, `SilkTouch` is an optimized, lightweight command-line intelligence framework. It is engineered to smoothly audit, sweep, and harvest a target's digital footprint across hundreds of social networks, forums, public code repositories, and web applications simultaneously.

---

## 🔮 Core Architecture & "Enchantments"

Traditional username enumeration scripts spawn hundreds of isolated, heavy network requests that break connections, trigger web application firewalls (WAFs), or flood your console with false positives. `SilkTouch` avoids this by implementing an intelligent, state-conscious validation engine:

* **⚡ Connection Pooling & Session Persistence:** By utilizing persistent HTTP request sessions (`requests.Session`), the script reuses underlying TCP sockets (HTTP Keep-Alive). This minimizes latency overhead and boosts sweeping speeds by up to 300% compared to standard looping requests.
* **📡 Dynamic Matrix Mining:** Instead of relying on hardcoded, outdated target endpoints, `SilkTouch` streams fresh target validation matrices on-the-fly directly from the verified WebBreacher `WhatsMyName` tracking infrastructure.
* **🎯 True-Negative Filtering Engine:** Implements strict parsing of response states against data-set parameters. It filters out "ghost matches" by cross-examining both the explicit HTTP response code (`e_code`) and the presence of custom error strings (`e_string`) buried inside the HTML DOM body.
* **🍃 Absolute Zero Overhead:** Zero external database engines, zero commercial API keys, and zero configuration files. Run it natively from any terminal sandbox instantly.

---

## 🛠️ Installation & Blueprint Setup

### System Prerequisites
* **Python 3.8 or higher**
* Supported environments: **Kali Linux**, **Parrot Security OS**, **Ubuntu/Debian**, **macOS**, or **Windows (via WSL or PowerShell)**.

### 1. Clone the Realm Architecture
Bring the core codebase into your local development environment:
```bash
git clone [https://github.com/Y/SilkTouch.git](https://github.com/MrHackerCharlie/SilkTouch.git)
cd SilkTouch
