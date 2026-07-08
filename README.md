# GNS3 Cisco OSPF Network Automation Project

This is a Python automation project built to configure and audit a 4-router full mesh topology inside GNS3 over SSH using **Netmiko** and `python-dotenv`.

## 🏗️ How the Lab is Set Up

I designed the network to have two separate traffic paths to keep things clean:
- **Management Network:** All routers are connected to a dedicated GNS3 switch on the `192.168.88.0/24` subnet. My Network Automation container uses this path to SSH into the routers.
- **Data Network:** The routers are cabled together in a full mesh layout using links in the `192.168.90.0/30` subnet.
- **Routing Engine:** The scripts turn on OSPF Area 0 on all interfaces and automatically set up point-to-point network types for fast neighbor connections.

## 📂 Project Directory Layout

GNS3_OSPF_Automation/
│
├── .env                       # Private network credentials 
├── 1_dynamic_deploy.py        # Script #1: Automated baseline deployment
├── 2_file_deploy.py           # Script #2: Custom file configuration deployment
└── configs/                   # Folder holding node-specific configurations
    ├── 192.168.0.1.text       # Custom commands for R1
    └── 192.168.0.2.text       # Custom commands for R2

## 🚀 Cool Features of the Scripts

- **Strategy 1 (Dynamic Parsing):** `1_dynamic_deploy.py` automatically parses each router's management IP, extracts the last octet, and uses it to mathematically configure the Loopback IP and Router-ID on the fly.
- **Strategy 2 (File Targeting):** `2_file_deploy.py` targets the `configs/` directory, checks if a file matching the node's IP exists, and streams manual targeted configurations straight to that device.
- **Secure Credentials:** All router passwords and secrets are completely isolated inside a private `.env` file instead of being visible inside the main Python code.
- **Automatic Audit Trail Logging:** Every time a script runs, it automatically auto-generates a timestamped `.txt` log file capturing the exact terminal output from all routers for post-deployment analysis.

## 🛠️ How to Run It

1. Move your execution files into your GNS3 Network Automation container.
2. Install the necessary libraries if you don't have them:
   ```bash
   apt-get update
   apt-get install -y python3-dotenv
   ```
3. Create a `.env` file right next to the scripts using the template below:
   ```text
   HOST_1=192.168.0.1
   HOST_2=192.168.0.2
   HOST_3=192.168.0.3
   HOST_4=192.168.0.4
   USERNAME=admin
   PASSWORD=your_password
   SECRET=your_enable_secret
   PORT=22
   ```

### Running Script 1: Dynamic OSPF Baseline Deployment
```bash
python3 1_dynamic_deploy.py
```

### Running Script 2: Custom File-Based Configuration Deployment
Ensure you place targeted command text files inside the `configs/` folder matching your node IPs first.
```bash
python3 2_file_deploy.py
```
