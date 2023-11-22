from netmiko import ConnectHandler
import datetime
import os
import filecmp

# start of writeFile function
def writeFile(hostname, running_output):
    # Define a file path before using this function
    base_path = r"/home/nms"
    folder_path = os.path.join(base_path, hostname)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' found.")

    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the date and time to include in the file name
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Construct the file path with the formatted date and time
    file_path = os.path.join(folder_path, f"{hostname}_{formatted_time}_running-config.txt")

    with open(file_path, 'w') as file:
        file.write(running_output)


# End of writeFile function
# Start of gatherConfigs function

def gatherConfigs(router):

    net_Connect = ConnectHandler(**router)
    print("----CONNECTED----")
    net_Connect.enable()
    print("----ENABLED----")
    hostname = net_Connect.send_command('sh run | i host').split()[1]
    running_config = net_Connect.send_command('show running-config')
    writeFile(hostname, running_config)
    print("----FILE WROTTEN----")

# End of gatherConfigs function

# Devices
devices = {

    'r1': {
        'device_type': 'cisco_ios',
        'host': '3.3.0.34',
        'username': 'netadmin',
        'password': 'Passw0rd'
    },
    'r2': {
        'device_type': 'cisco_ios',
        'host': '3.3.0.6',
        'username': 'netadmin',
        'password': 'Passw0rd'
    },
    'r3': {
        'device_type': 'cisco_ios',
        'host': '3.3.0.2',
        'username': 'netadmin',
        'password': 'Passw0rd'
    },
    'r4': {
        'device_type': 'cisco_ios',
        'host': '3.3.0.10',
        'username': 'netadmin',
        'password': 'Passw0rd'
    },
    'r5': {
        'device_type': 'cisco_ios',
        'host': '3.3.0.13',
        'username': 'netadmin',
        'password': 'Passw0rd'
    }
}

gatherConfigs(devices['r1'])
gatherConfigs(devices['r2'])
gatherConfigs(devices['r3'])
gatherConfigs(devices['r4'])
gatherConfigs(devices['r5'])
