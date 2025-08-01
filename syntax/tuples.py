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

# Tuple as dictionary key (hashable)
location = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
print(location[(40.7128, -74.0060)])  # Output: New York

# Returning multiple values from a function
def get_user():
    return ("sushant", 25)

username, age = get_user()
print(f"User: {username}, Age: {age}")

# Employee data tuple (new example)
employee_data = ("John Doe", "Software Engineer", 75000, "Engineering", True)
emp_name, position, salary, department, is_active = employee_data
print(f"Employee: {emp_name}")
print(f"Position: {position} in {department}")
print(f"Salary: ${salary:,}")
print(f"Status: {'Active' if is_active else 'Inactive'}")

# Nested tuple for storing RGB color values
colors = (
    ("Red", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Blue", (0, 0, 255)),
    ("Purple", (128, 0, 128))
)

for color_name, rgb_values in colors:
    r, g, b = rgb_values
    print(f"{color_name}: RGB({r}, {g}, {b})")
