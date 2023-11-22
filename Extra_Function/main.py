from netmiko import ConnectHandler
import time

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
print("Menu")
time.sleep(1)
print("---------------")
time.sleep(1)
print("[1] Router 1")
time.sleep(1)
print("[2] Router 2")
time.sleep(1)
print("[3] Router 3")
time.sleep(1)
print("[4] Router 4")
time.sleep(1)
print("[5] Router 5")
time.sleep(1)
print(' ')
time.sleep(1)
option = input('Select an option>')

# Monitoring
# Router 1
if option == '1':
    net_connect = ConnectHandler(**r1)
    print("**Successfully Connected to Router 1**\n")
    time.sleep(1)
    print("**Gathering All Router 1 CPU Information**")
    time.sleep(1)

    time_r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\nTime: {time_r}")
    time.sleep(1)
    cpu_output = net_connect.send_command('show processes cpu')

    print("\n**Router 1 CPU Usage**:\n")
    print(cpu_output)
    time.sleep(1)

# Router 2
if option == '2':
    net_connect = ConnectHandler(**r2)
    print("**Successfully Connected to Router 2**\n")
    time.sleep(1)
    print("**Gathering All Router 2 CPU Information**")
    time.sleep(1)

    time_r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\nTime: {time_r}")
    time.sleep(1)
    cpu_output = net_connect.send_command('show processes cpu', read_timeout=200)

    print("\n**Router 2 CPU Usage**:\n")
    print(cpu_output)
    time.sleep(1)

# Router 3
if option == '3':
    net_connect = ConnectHandler(**r3)
    print("**Successfully Connected to Router 3**\n")
    time.sleep(1)
    print("**Gathering All Router 3 CPU Information**")
    time.sleep(1)

    time_r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\nTime: {time_r}")
    time.sleep(1)
    cpu_output = net_connect.send_command('show processes cpu', read_timeout=200)

    print("\n**Router 3 CPU Usage**:\n")
    print(cpu_output)
    time.sleep(2)

# Router 4
if option == '4':
    net_connect = ConnectHandler(**r4)
    print("**Successfully Connected to Router 4**\n")
    time.sleep(1)
    print("**Gathering All Router 4 CPU Information**")
    time.sleep(1)

    time_r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\nTime: {time_r}")
    time.sleep(1)
    cpu_output = net_connect.send_command('show processes cpu', read_timeout=200)

    print("\n**Router 4 CPU Usage**:\n")
    print(cpu_output)
    time.sleep(2)

# Router 5
if option == '5':
    net_connect = ConnectHandler(**r5)
    print("**Successfully Connected to Router 5**\n")
    time.sleep(1)
    print("**Gathering All Router 5 CPU Information**")
    time.sleep(1)

    time_r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\nTime: {time_r}")
    time.sleep(1)
    cpu_output = net_connect.send_command('show processes cpu', read_timeout=200)

    print("\n**Router 5 CPU Usage**:\n")
    print(cpu_output)
    time.sleep(2)

print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
