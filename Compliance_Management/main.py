import time
from netmiko import ConnectHandler


# Routers
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


# Router 1
net_connect = ConnectHandler(**r1)
print("**Successfully Connected to Router 1**\n")
time.sleep(1)
print("**Gathering All Router 1 Interface Information**")
time.sleep(1)
print("Router 1 Interfaces>")
time.sleep(1)
sh_output = net_connect.send_command("show ip int brief")
print(sh_output)
time.sleep(1)

# Router 2
net_connect = ConnectHandler(**r2)
print("**Successfully Connected to Router 2**\n")
time.sleep(1)
print("**Gathering All Router 2 Interface Information**")
time.sleep(1)
print("Router 2 Interfaces>")
time.sleep(1)
sh_output2 = net_connect.send_command("show ip int brief")
print(sh_output2)
time.sleep(1)

# Router 3
net_connect = ConnectHandler(**r3)
print("**Successfully Connected to Router 3**\n")
time.sleep(1)
print("**Gathering All Router 3 Interface Information**")
time.sleep(1)
print("Router 3 Interfaces>")
time.sleep(1)
sh_output3 = net_connect.send_command("show ip int brief")
print(sh_output3)
time.sleep(1)

# Router 4
net_connect = ConnectHandler(**r4)
print("**Successfully Connected to Router 4**\n")
time.sleep(1)
print("**Gathering All Router 4 Interface Information**")
time.sleep(1)
print("Router 4 Interfaces>")
time.sleep(1)
sh_output4 = net_connect.send_command("show ip int brief")
print(sh_output4)
time.sleep(1)

# Router 5
net_connect = ConnectHandler(**r5)
print("**Successfully Connected to Router 5**\n")
time.sleep(1)
print("**Gathering All Router 5 Interface Information**")
time.sleep(1)
print("Router 5 Interfaces>")
time.sleep(1)
sh_output5 = net_connect.send_command("show ip int brief")
print(sh_output5)
time.sleep(1)
print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
