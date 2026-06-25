# Automated Cisco Network State Auditor

Python automation tool utilizing the **Netmiko** library to programmatically connect to Cisco IOS-XE infrastructure via SSH, execute critical status audits, and serialize the output into structured text files.

## Project Architecture
* **Language:** Python 3.x
* **Core Library:** Netmiko (SSH Context Management)
* **Target Environment:** Cisco DevNet Always-On Sandbox (IOS-XE)
* **Security:** Implements `python-dotenv` for local environment variable abstraction, ensuring zero credential exposure on public version control.

## Automated Commands
The script automatically executes and logs the following network states for compliance auditing:
* `show version`
* `show running-config`
* `show ip interface brief`
* `show vlan brief`
* `show cdp neighbors`

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install netmiko python-dotenv`
3. Create a local `.env` file containing target host credentials (mirroring `.env.example`).
4. Execute the automation framework: `python backup_script.py`
