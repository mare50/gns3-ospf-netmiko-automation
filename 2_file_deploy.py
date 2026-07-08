import os
import datetime
from netmiko import ConnectHandler
from dotenv import load_dotenv

load_dotenv()

routers = [    
    {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_1'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT', 22))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_2'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT', 22))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_3'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT', 22))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_4'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT', 22))}
]

config_folder = "configs"

def run_file_deployment():

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"device_file_deployment_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"=== GNS3 FILE-BASED DEPLOYMENT LOG: {datetime.datetime.now()} ===\n\n")

        for router in routers:
            try:

                if not router['host']:
                    print("Skipping entry: Missing HOST string in environment configuration.")
                    continue

                config_file_path = os.path.join(config_folder, f"{router['host']}.text")
                print(f"\nChecking for configuration file: {config_file_path}")

                if not os.path.exists(config_file_path):
                    msg = f"Skipping {router['host']}: No configuration file found at {config_file_path}.\n"
                    print(msg)
                    file.write(msg)
                    continue

                with ConnectHandler(**router) as connection:
                    print(f"SSH Connection established successfully to {router['host']}!") 
                    print(f"Pushing configuration from file to {router['host']}...")
                    
                    output = connection.send_config_from_file(config_file_path)

                    print(f"{'='*50}\n")
                    file.write(f"Output from Device IP: {router['host']}\n")
                    file.write(f"{'='*50}\n{output}\n\n")

                    print(f"Saving running configuration on {router['host']}...")
                    connection.save_config()
                    file.write(f"SUCCESS: Running configuration saved on {router['host']}.\n\n")
                    print(f"Successfully processed {router['host']}.\n")
            
            except Exception as e:
                error_msg = f"FAILURE: An error occurred during execution on {router['host']}: {e}"
                print(error_msg)
                file.write(error_msg + "\n\n")


if __name__ == "__main__":
    run_file_deployment()
