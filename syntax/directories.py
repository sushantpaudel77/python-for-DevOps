# Dictionary creation and access
server_config = {"host": "localhost", "port": 8080, "ssl": True}

# Accessing values
print(server_config["host"])  # Direct access
print(server_config.get("port", 80))  # Safe access with default

# Dictionary operations
server_config["timeout"] = 30  # Add/update
del server_config["ssl"]  # Delete key
popped_value = server_config.pop("timeout", 0)  # Remove and return

# Dictionary methods
print(server_config.keys())  # Get all keys
print(server_config.values())  # Get all values
print(server_config.items())  # Get key-value pairs

# Looping through dictionary
for key, value in server_config.items():
    print(f"{key}: {value}")

# Dictionary comprehension
ports = [80, 443, 8080]
port_status = {port: "open" for port in ports}
# {80: 'open', 443: 'open', 8080: 'open'}

# Nested dictionaries
infrastructure = {
    "web_servers": {
        "web1": {"ip": "192.168.1.10", "status": "active"},
        "web2": {"ip": "192.168.1.11", "status": "inactive"},
    },
    "databases": {"db1": {"ip": "192.168.1.20", "status": "active"}},
}

# Update dictionaries
config1 = {"host": "localhost", "port": 80}
config2 = {"port": 8080, "ssl": True}
config1.update(config2)  # Merges config2 into config1
