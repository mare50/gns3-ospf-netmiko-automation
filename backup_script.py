import os
import datetime
from netmiko import ConnectHandler
from dotenv import load_dotenv

# Load sensitive environment variables from .env file
load_dotenv()

# Build device dictionary dynamically from secure environment variables
devnet_switch = {
    'device_type': 'cisco_ios', 
    'host': os.getenv('DEVNET_HOST'),
    'username': os.getenv('DEVNET_USER'),
    'password': os.getenv('DEVNET_PASS'),
    'port': int(os.getenv('DEVNET_PORT', 22)), 
}

audit_commands = [
    'show version',
    'show running-config',
    'show ip interface brief',
    'show vlan brief',
    'show cdp neighbors',
]

def run_network_audit():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"device_audit_{timestamp}.txt"
    
    print(f"Initiating SSH connection to {devnet_switch['host']}...")
    
    try:
        with ConnectHandler(**devnet_switch) as connection:
            print("SSH Connection established successfully!")   
            
            with open(filename, 'w', encoding='utf-8') as file:
                for command in audit_commands:
                    print(f"Executing and logging: '{command}'")
                    output = connection.send_command(command)
                    
                    file.write(f"{'='*40}\n")
                    file.write(f"COMMAND: {command}\n")
                    file.write(f"{'='*40}\n")
                    file.write(output + "\n\n")
            
            print(f"SUCCESS: Audit logs successfully written to {filename}")
            
    except Exception as e:
        print(f"FAILURE: An error occurred during execution: {e}")

if __name__ == "__main__":
    run_network_audit()
