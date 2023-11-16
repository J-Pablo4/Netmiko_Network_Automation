from netmiko import ConnectHandler

r1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.60.162',
    'username': 'netadmin',
    'password': 'Passw0rd'
}

net_connect = ConnectHandler(**r1)
print("**Connected Successfully**")
print(dir(net_connect))
sh_output = net_connect.send_command("show run")
print(sh_output)

print("*** Disconnecting ")
# Disconnect from the device
net_connect.disconnect()
