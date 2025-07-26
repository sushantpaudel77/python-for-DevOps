# Tuple creation (immutable)
coordinates = (10.5, 20.3)
server_info = ("web1", "192.168.1.10", 80)

# Tuple unpacking
name, ip, port = server_info
print(f"Server: {name} at {ip}:{port}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))      # Count occurrences: 3
print(numbers.index(3))      # Find index: 2

# Named tuples (more readable)
from collections import namedtuple
Server = namedtuple('Server', ['name', 'ip', 'port'])
web_server = Server('web1', '192.168.1.10', 80)
print(web_server.name)       # Access by name
print(web_server.ip)

# Tuple vs List choice
# Use tuple for: coordinates, database records, function returns
# Use list for: dynamic collections that change