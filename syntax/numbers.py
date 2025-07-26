# Integer operations
count = 10
total = count + 5
print(total // 3)  # Floor division: 5
print(total % 3)  # Modulo: 0
print(total**2)  # Power: 225


# Float operations
cpu_usage = 45.7
memory_usage = 54.2
average = (cpu_usage + memory_usage) / 2

# Number conversion
port = "8080"
port_num = int(port)  # string to int
cpu_str = str(cpu_usage)  # int to string

# Math operations
import math

print(math.ceil(45.2))
print(math.floor(45.8))
print(round(45.534, 2))

# Numbers checking
x = 42
print(isinstance(x, int))
print(type(x).__name__)
