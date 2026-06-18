from netmiko import ConnectHandler
from datetime import datetime

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**device)

output = connection.send_command("show running-config")

filename = f"{device['host']}_{datetime.now().strftime('%Y%m%d')}.txt"

with open(filename, "w") as backup:
    backup.write(output)

connection.disconnect()

print("Configuration backup completed.")
