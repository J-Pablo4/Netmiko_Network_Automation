from netmiko import ConnectHandler
import datetime
import os

#Funtions
def writeFile(hostname, running_output):
    file = open(hostname + '_running-config.txt', 'w')
    file.write(running_output)



def gatherConfigs(router):
    net_Connect = ConnectHandler(**router)
    print("----CONNECTED----")
    net_Connect.enable()
    print("----ENABLED----")
    hostname = net_Connect.send_command('sh run | i host').split()[1]
    running_config = net_Connect.send_command('show running-config')
    writeFile(hostname, running_config)
    print("----FILE WROTTEN----")



# Devices
r1 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.34',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r2 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.6',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r3 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.2',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r4 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.10',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r5 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.13',
    'username': 'netadmin',
    'password': 'Passw0rd'
}

test_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.232.168',
    'username': 'cisco',
    'password': 'cisco'
}
gatherConfigs(test_router)
