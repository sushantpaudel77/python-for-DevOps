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
