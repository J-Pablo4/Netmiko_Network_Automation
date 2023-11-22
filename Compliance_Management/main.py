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
loopback1_is_up = False
loopback1_has_ip = False
banner_exist = False
telnet_is_up = False
print("**Successfully Connected to Router 1**\n")
time.sleep(1)
# telnet
print("**Checking that Telnet is Disabled**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('transport input ssh') == -1:
        telnet_is_up = True
if telnet_is_up:
    print("**Telnet is Enabled**\n")
    time.sleep(1)
    print("**Disabling Telnet**\n")
    time.sleep(1)
    commands = ['line vty 0 4', 'transport input ssh']
    sh_output = net_connect.send_config_set(commands)
    print("**Telnet has been Disabled. Only SSH Connections are Permitted****\n")
    time.sleep(1)
else:
    print("**Telnet is Disabled. Only SSH Connections are Permitted**\n")
    time.sleep(1)
# banner-motd
print("**Confirming that there is a Message of the Day in Router 1**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('banner motd') != -1:
        banner_exist = True
if not banner_exist:
    print("**The Message of the Day has not been Set**\n")
    time.sleep(1)
    command = ("banner motd #Access is restricted. Only authorized persons can view and/or modify the settings of "
               "this Router.#")
    net_connect.config_mode()
    sh_output = net_connect.send_command(command, read_timeout=200)
    print("**The Message of the Day has been Set Correctly**\n")
    time.sleep(1)
    print(command+'\n')
    time.sleep(1)
else:
    print("**The Message of the Day is Already Set**\n")
    time.sleep(1)
# Loopback1
print("**Confirming that the Loopback1 is Up**\n")
time.sleep(1)
if net_connect.check_config_mode():
    net_connect.exit_config_mode()
sh_output = net_connect.send_command("show ip int brief", use_textfsm=True)
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output[i]['interface'] == 'Loopback1' and sh_output[i]['status'] == 'up':
        loopback1_is_up = True
    if sh_output[i]['ip_address'] != 'unassigned' and sh_output[i]['interface'] == 'Loopback1':
        loopback1_has_ip = True
if loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 1 is Up and it has an IP Address Assigned**\n')
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif not loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 1 is Down but it has an IP Address Assigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up**\n")
    commands = ['interface loopback1', 'no shutdown']
    net_connect.send_config_set(commands)
    time.sleep(1)
    print("**Loopback1 is Up**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif loopback1_is_up and not loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 1 is Up but the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '11.11.11.11'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}']
    net_connect.send_config_set(commands)
    print("**The IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
else:
    print('**The Loopback1 Interface of the Router 1 is Down and the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up and Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '11.11.11.11'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}', 'no shutdown']
    net_connect.send_config_set(commands)
    print("**Loopback1 is Up and the IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(2)


# Router 2
net_connect = ConnectHandler(**r2)
loopback1_is_up = False
loopback1_has_ip = False
banner_exist = False
telnet_is_up = False
print("**Successfully Connected to Router 2**\n")
time.sleep(1)
# telnet
print("**Checking that Telnet is Disabled**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('transport input ssh') == -1:
        telnet_is_up = True
if telnet_is_up:
    print("**Telnet is Enabled**\n")
    time.sleep(1)
    print("**Disabling Telnet**\n")
    time.sleep(1)
    commands = ['line vty 0 4', 'transport input ssh']
    sh_output = net_connect.send_config_set(commands)
    print("**Telnet has been Disabled. Only SSH Connections are Permitted****\n")
    time.sleep(1)
else:
    print("**Telnet is Disabled. Only SSH Connections are Permitted**\n")
    time.sleep(1)
# banner-motd
print("**Confirming that there is a Message of the Day in Router 2**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('banner motd') != -1:
        banner_exist = True
if not banner_exist:
    print("**The Message of the Day has not been Set**\n")
    time.sleep(1)
    command = ("banner motd #Access is restricted. Only authorized persons can view and/or modify the settings of "
               "this Router.#")
    net_connect.config_mode()
    sh_output = net_connect.send_command(command, read_timeout=200)
    print("**The Message of the Day has been Set Correctly**\n")
    time.sleep(1)
    print(command+'\n')
    time.sleep(1)
else:
    print("**The Message of the Day is Already Set**\n")
    time.sleep(1)
# Loopback1
print("**Confirming that the Loopback1 is Up**\n")
time.sleep(1)
if net_connect.check_config_mode():
    net_connect.exit_config_mode()
sh_output = net_connect.send_command("show ip int brief", use_textfsm=True)
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output[i]['interface'] == 'Loopback1' and sh_output[i]['status'] == 'up':
        loopback1_is_up = True
    if sh_output[i]['ip_address'] != 'unassigned' and sh_output[i]['interface'] == 'Loopback1':
        loopback1_has_ip = True
if loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 2 is Up and it has an IP Address Assigned**\n')
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif not loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 2 is Down but it has an IP Address Assigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up**\n")
    commands = ['interface loopback1', 'no shutdown']
    net_connect.send_config_set(commands)
    time.sleep(1)
    print("**Loopback1 is Up**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif loopback1_is_up and not loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 2 is Up but the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '12.12.12.12'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}']
    net_connect.send_config_set(commands)
    print("**The IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
else:
    print('**The Loopback1 Interface of the Router 2 is Down and the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up and Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '12.12.12.12'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}', 'no shutdown']
    net_connect.send_config_set(commands)
    print("**Loopback1 is Up and the IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(2)


# Router 3
net_connect = ConnectHandler(**r3)
loopback1_is_up = False
loopback1_has_ip = False
banner_exist = False
telnet_is_up = False
print("**Successfully Connected to Router 3**\n")
time.sleep(1)
# telnet
print("**Checking that Telnet is Disabled**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('transport input ssh') == -1:
        telnet_is_up = True
if telnet_is_up:
    print("**Telnet is Enabled**\n")
    time.sleep(1)
    print("**Disabling Telnet**\n")
    time.sleep(1)
    commands = ['line vty 0 4', 'transport input ssh']
    sh_output = net_connect.send_config_set(commands)
    print("**Telnet has been Disabled. Only SSH Connections are Permitted****\n")
    time.sleep(1)
else:
    print("**Telnet is Disabled. Only SSH Connections are Permitted**\n")
    time.sleep(1)
# banner-motd
print("**Confirming that there is a Message of the Day in Router 3**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('banner motd') != -1:
        banner_exist = True
if not banner_exist:
    print("**The Message of the Day has not been Set**\n")
    time.sleep(1)
    command = ("banner motd #Access is restricted. Only authorized persons can view and/or modify the settings of "
               "this Router.#")
    net_connect.config_mode()
    sh_output = net_connect.send_command(command, read_timeout=200)
    print("**The Message of the Day has been Set Correctly**\n")
    time.sleep(1)
    print(command+'\n')
    time.sleep(1)
else:
    print("**The Message of the Day is Already Set**\n")
    time.sleep(1)
# Loopback1
print("**Confirming that the Loopback1 is Up**\n")
time.sleep(1)
if net_connect.check_config_mode():
    net_connect.exit_config_mode()
sh_output = net_connect.send_command("show ip int brief", use_textfsm=True)
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output[i]['interface'] == 'Loopback1' and sh_output[i]['status'] == 'up':
        loopback1_is_up = True
    if sh_output[i]['ip_address'] != 'unassigned' and sh_output[i]['interface'] == 'Loopback1':
        loopback1_has_ip = True
if loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 3 is Up and it has an IP Address Assigned**\n')
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif not loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 3 is Down but it has an IP Address Assigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up**\n")
    commands = ['interface loopback1', 'no shutdown']
    net_connect.send_config_set(commands)
    time.sleep(1)
    print("**Loopback1 is Up**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif loopback1_is_up and not loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 3 is Up but the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '13.13.13.13'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}']
    net_connect.send_config_set(commands)
    print("**The IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
else:
    print('**The Loopback1 Interface of the Router 3 is Down and the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up and Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '13.13.13.13'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}', 'no shutdown']
    net_connect.send_config_set(commands)
    print("**Loopback1 is Up and the IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(2)


# Router 4
net_connect = ConnectHandler(**r4)
loopback1_is_up = False
loopback1_has_ip = False
banner_exist = False
telnet_is_up = False
print("**Successfully Connected to Router 4**\n")
time.sleep(1)
# telnet
print("**Checking that Telnet is Disabled**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('transport input ssh') == -1:
        telnet_is_up = True
if telnet_is_up:
    print("**Telnet is Enabled**\n")
    time.sleep(1)
    print("**Disabling Telnet**\n")
    time.sleep(1)
    commands = ['line vty 0 4', 'transport input ssh']
    sh_output = net_connect.send_config_set(commands)
    print("**Telnet has been Disabled. Only SSH Connections are Permitted****\n")
    time.sleep(1)
else:
    print("**Telnet is Disabled. Only SSH Connections are Permitted**\n")
    time.sleep(1)
# banner-motd
print("**Confirming that there is a Message of the Day in Router 4**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('banner motd') != -1:
        banner_exist = True
if not banner_exist:
    print("**The Message of the Day has not been Set**\n")
    time.sleep(1)
    command = ("banner motd #Access is restricted. Only authorized persons can view and/or modify the settings of "
               "this Router.#")
    net_connect.config_mode()
    sh_output = net_connect.send_command(command, read_timeout=200)
    print("**The Message of the Day has been Set Correctly**\n")
    time.sleep(1)
    print(command+'\n')
    time.sleep(1)
else:
    print("**The Message of the Day is Already Set**\n")
    time.sleep(1)
# Loopback1
print("**Confirming that the Loopback1 is Up**\n")
time.sleep(1)
if net_connect.check_config_mode():
    net_connect.exit_config_mode()
sh_output = net_connect.send_command("show ip int brief", use_textfsm=True)
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output[i]['interface'] == 'Loopback1' and sh_output[i]['status'] == 'up':
        loopback1_is_up = True
    if sh_output[i]['ip_address'] != 'unassigned' and sh_output[i]['interface'] == 'Loopback1':
        loopback1_has_ip = True
if loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 4 is Up and it has an IP Address Assigned**\n')
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif not loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 4 is Down but it has an IP Address Assigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up**\n")
    commands = ['interface loopback1', 'no shutdown']
    net_connect.send_config_set(commands)
    time.sleep(1)
    print("**Loopback1 is Up**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif loopback1_is_up and not loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 4 is Up but the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '14.14.14.14'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}']
    net_connect.send_config_set(commands)
    print("**The IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
else:
    print('**The Loopback1 Interface of the Router 4 is Down and the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up and Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '14.14.14.14'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}', 'no shutdown']
    net_connect.send_config_set(commands)
    print("**Loopback1 is Up and the IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(2)


# Router 5
net_connect = ConnectHandler(**r5)
loopback1_is_up = False
loopback1_has_ip = False
banner_exist = False
telnet_is_up = False
print("**Successfully Connected to Router 5**\n")
time.sleep(1)
# telnet
print("**Checking that Telnet is Disabled**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('transport input ssh') == -1:
        telnet_is_up = True
if telnet_is_up:
    print("**Telnet is Enabled**\n")
    time.sleep(1)
    print("**Disabling Telnet**\n")
    time.sleep(1)
    commands = ['line vty 0 4', 'transport input ssh']
    sh_output = net_connect.send_config_set(commands)
    print("**Telnet has been Disabled. Only SSH Connections are Permitted****\n")
    time.sleep(1)
else:
    print("**Telnet is Disabled. Only SSH Connections are Permitted**\n")
    time.sleep(1)
# banner-motd
print("**Confirming that there is a Message of the Day in Router 5**\n")
time.sleep(1)
sh_output = net_connect.send_command("show run")
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output.find('banner motd') != -1:
        banner_exist = True
if not banner_exist:
    print("**The Message of the Day has not been Set**\n")
    time.sleep(1)
    command = ("banner motd #Access is restricted. Only authorized persons can view and/or modify the settings of "
               "this Router.#")
    net_connect.config_mode()
    sh_output = net_connect.send_command(command, read_timeout=200)
    print("**The Message of the Day has been Set Correctly**\n")
    time.sleep(1)
    print(command+'\n')
    time.sleep(1)
else:
    print("**The Message of the Day is Already Set**\n")
    time.sleep(1)
# Loopback1
print("**Confirming that the Loopback1 is Up**\n")
time.sleep(1)
if net_connect.check_config_mode():
    net_connect.exit_config_mode()
sh_output = net_connect.send_command("show ip int brief", use_textfsm=True)
sh_output_length = len(sh_output)
for i in range(0, sh_output_length):
    if sh_output[i]['interface'] == 'Loopback1' and sh_output[i]['status'] == 'up':
        loopback1_is_up = True
    if sh_output[i]['ip_address'] != 'unassigned' and sh_output[i]['interface'] == 'Loopback1':
        loopback1_has_ip = True
if loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 5 is Up and it has an IP Address Assigned**\n')
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif not loopback1_is_up and loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 5 is Down but it has an IP Address Assigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up**\n")
    commands = ['interface loopback1', 'no shutdown']
    net_connect.send_config_set(commands)
    time.sleep(1)
    print("**Loopback1 is Up**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
elif loopback1_is_up and not loopback1_has_ip:
    print('**The Loopback1 Interface of the Router 5 is Up but the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '15.15.15.15'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}']
    net_connect.send_config_set(commands)
    print("**The IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(1)
else:
    print('**The Loopback1 Interface of the Router 5 is Down and the IP Address is Unassigned**\n')
    time.sleep(1)
    print("**Changing Loopback1 State to Up and Assigning a new IP Address**\n")
    time.sleep(1)
    ip_address = '15.15.15.15'
    netmask = '255.255.255.0'
    time.sleep(1)
    commands = ['interface loopback1', f'ip address {ip_address} {netmask}', 'no shutdown']
    net_connect.send_config_set(commands)
    print("**Loopback1 is Up and the IP Address has been Assigned**\n")
    time.sleep(1)
    sh_output = net_connect.send_command('show ip int br Loopback 1')
    print(sh_output)
    time.sleep(2)

print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
