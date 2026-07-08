import os
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

config_folder = r"configs"


def push_config():

    for router in routers:
        
        ip = router['host']
        print(ip)

        config_file_path = os.path.join(config_folder, f'{ip}.text')
        print(f"\nChecking for configuration file: {config_file_path}")

        if not os.path.exists(config_file_path):
            print(f"Skipping {ip}: No configuration file found at {config_file_path}")
            continue

        print(f"Connecting to router {ip}...")

        try:
            with ConnectHandler(**router) as connection:
                print(f"Pushing configuration from file...")

                output = connection.send_config_from_file(config_file_path)
                print(output)
                connection.save_config()

        except Exception as e:
            print(f"Error configuring {ip}: {e}")        



if __name__=="__main__":
    push_config()