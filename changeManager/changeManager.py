from netmiko import ConnectHandler


# Is capable of sending commands and marking where the error is in the command
def sendCommand(config_commands, router):
    try:
        net_connect = ConnectHandler(**router)
        print("----CONNECTED----")

        # Sending the configuration set
        output = net_connect.send_config_set(config_commands)
        print(output)

        net_connect.disconnect()
        print("----DISCONNECTED----")
    except Exception as e:
        print(f"Error: {e}")

def read_command(file_path):
    with open(file_path, 'r') as file:
        command = file.read().splitlines()
    return command


def sendChanges(device_list):
    print(" 1) Send a command to an specific device \n 2) Send a command to all devices\n")
    operation = input("Select an option>")
    if operation == '1':
        device_name = input("Device name:")
        file_path = input("file path of the command list: ")
        command = read_command(file_path)
        sendCommand(command, device_list[device_name])

    elif operation == '2':
        file_path = input("file path of the command list: ")
        command = read_command(file_path)
        for device in device_list.keys():
            sendCommand(command, device_list[device])


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

sendChanges(devices)
