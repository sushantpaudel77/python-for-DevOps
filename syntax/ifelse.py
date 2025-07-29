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

# New condition 1: Check disk space
if disk > 90:
    print("Warning: Disk space critically low!")
elif disk > 75:
    print("Warning: Disk space running low")

# Checking existence
config = {"host": "localhost", "port": 8080}
if "host" in config:
    print(f"Host: {config['host']}")

# Ternary operator
status = "active" if cpu_usage < 80 else "stressed"

# Checking none and empty values
data = []
if not data:  # Checks for empty list, None, False, 0, ""
    print("No data available")

if data is None:
    print("Data is None")

# New condition 2: Combined resource check
if cpu_usage > 75 and memory > 75 and disk > 75:
    print("Warning: Multiple resources under heavy load")
elif cpu_usage > 75 or memory > 75 or disk > 75:
    print("Warning: At least one resource under heavy load")