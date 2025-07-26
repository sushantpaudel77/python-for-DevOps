# List creation and access
servers = ["web1", "web2", "db1"]
servers.append("cache1")         # Add to end
servers.insert(0, "lb1")        # Insert at position
print(servers[0])                # First element
print(servers[-1])               # Last element

# List operations
servers.remove("web2")           # Remove by value
popped = servers.pop()           # Remove and return last
servers.extend(["web3", "web4"]) # Add multiple items

# List comprehension
ports = [80, 443, 8080, 9000]
open_ports = [p for p in ports if p > 443]  # [8080, 9000]
port_strings = [str(p) for p in ports]      # Convert to strings

# List methods
numbers = [3, 1, 4, 1, 5]
print(len(numbers))              # Length: 5
print(max(numbers))              # Maximum: 5
print(sorted(numbers))           # Sorted copy: [1, 1, 3, 4, 5]
numbers.sort()                   # Sort in place

# Slicing
services = ["nginx", "mysql", "redis", "postgres", "mongodb"]
print(services[1:3])             # ['mysql', 'redis']
print(services[:2])              # ['nginx', 'mysql']
print(services[2:])              # ['redis', 'postgres', 'mongodb']