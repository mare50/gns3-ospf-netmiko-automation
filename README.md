# GNS3 Cisco OSPF Network Automation Project

This is a Python automation project I built to configure a 4-router full mesh topology inside GNS3. Instead of configuring each router manually, the script uses **Netmiko** to log in over SSH, configure loopback interfaces, and set up OSPF routing on all devices automatically.

## 🏗️ How the Lab is Set Up

I designed the network to have two separate traffic paths to keep things clean:
- **Management Network:** All routers are connected to a dedicated GNS3 switch on the `192.168.88.0/24` subnet. My Network Automation container uses this path to SSH into the routers.
- **Data Network:** The routers are cabled together in a full mesh layout using links in the `192.168.90.0/30` subnet.
- **Routing Engine:** The script turns on OSPF Area 0 on all interfaces and automatically sets up point-to-point network types for fast neighbor connections.

## 🚀 Cool Features of the Script

- **Smart Config Generator:** The script reads the router's IP address, splits it up, grabs the last number, and uses it as the Router ID and Loopback IP. I don't have to hardcode any configurations!
- **Secure Passwords:** I used `python-dotenv` so that all router passwords and secrets are hidden inside a private `.env` file instead of being visible in the main Python code.
- **Automatic Logging:** Every time the script runs, it automatically creates a `.txt` log file with a timestamp. It saves the exact terminal outputs from all four routers so I can see what was pushed.

## 🛠️ How to Run It

1. Put the `cisco_automation.py` script into your GNS3 Network Automation container.
2. Install the necessary libraries if you don't have them:
   ```bash
   apt-get update
   apt-get install -y python3-dotenv
   ```
3. Create a `.env` file right next to the script using the template below:
   ```text
   HOST_1=192.168.88.1
   HOST_2=192.168.88.2
   HOST_3=192.168.88.3
   HOST_4=192.168.88.4
   USERNAME=admin
   PASSWORD=your_password
   SECRET=your_enable_secret
   ```
4. Run the script:
   ```bash
   python3 cisco_automation.py
   ```
