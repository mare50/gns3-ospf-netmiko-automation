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
     'port': int(os.getenv('PORT'))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_2'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT'))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_3'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT'))},

     {'device_type': 'cisco_ios', 
     'host': os.getenv('HOST_4'), 
     'username': os.getenv('USERNAME'), 
     'password': os.getenv('PASSWORD'), 
     'secret': os.getenv('SECRET'), 
     'port': int(os.getenv('PORT'))}
]

def generate_router_config(router):
  
    ip_parts = router['host'].split('.')
    router_id = ip_parts[-1]

    config = [
        'interface loopback 0',
        f'description Loopback Interface for Router {router_id}',
        f'ip address 10.0.0.{router_id} 255.255.255.255',
        'ip ospf 1 area 0', 
        'exit',
        'interface range ethernet 1/1 - 3', 
        'ip ospf 1 area 0',
        'ip ospf network point-to-point', 
        'exit',
        'router ospf 1',
        f'router-id {router_id}.{router_id}.{router_id}.{router_id}'
    ]

    return config


def run_network_audit():

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"device_audit_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        for router in routers:
            try:

                if not router['host']:
                    print("Skipping entry: Missing HOST string in environment configuration.")
                    continue

                with ConnectHandler(**router) as connection:
                    print(f"SSH Connection established successfully to {router['host']}!") 
                                
                    router_commands = generate_router_config(router)    
                    print(f"Pushing configuration set to {router['host']}...")
                    output = connection.send_config_set(router_commands)

                    print(f"{'='*50}\n")
                    file.write(f"Output from Device IP: {router['host']}\n")
                    file.write(f"{'='*50}\n{output}\n\n")

                    print(f"Saving running configuration on {router['host']}...")
                    connection.save_config()
                    file.write(f"SUCCESS: Running configuration saved on {router['host']}.\n\n")
                    print(f"Successfully processed {router['host']}.\n")
            
            except Exception as e:
                print(f"FAILURE: An error occurred during execution on {router['host']}: {e}")


if __name__ == "__main__":
    run_network_audit()
