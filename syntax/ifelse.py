# Basic if-else
cpu_usage = 85
if cpu_usage > 90:
    print("Critical CPU usage!")
elif cpu_usage > 75:
    print("High CPU usage")
else:
    print("Normal CPU usage")

# Multiple conditions
memory = 70
disk = 50
if cpu_usage > 80 and memory > 80:
    print("System overloaded!")
elif cpu_usage > 80 or memory > 80:
    print("System stressed!")
    

# Checking existence
config = {"host": "localhost", "port": 8080}
if "host" in config:
    print(f"Host: {config['host']}")
    
# Terenay operator
status = "active" if cpu_usage < 80 else "stressed"

# Checking none and empty values
data = []
if not data:  # Checks for empty list, None, False, 0, ""
    print("No data available")

if data is None:
    print("Data is None")