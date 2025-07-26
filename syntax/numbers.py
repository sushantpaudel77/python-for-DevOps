# Integer operations
count = 10
total = count + 5
print(total // 3)        # Floor division: 5
print(total % 3)         # Modulo: 0
print(total ** 2)        # Power: 225

# Float operations
cpu_usage = 45.7
memory_usage = 67.2
average = (cpu_usage + memory_usage) / 2

# Number conversions
port = "8080"
port_num = int(port)     # String to int
cpu_str = str(cpu_usage) # Float to string

# Math operations
import math
print(math.ceil(45.2))   # 46
print(math.floor(45.8))  # 45
print(round(45.567, 2))  # 45.57

# Number checking
x = 42
print(isinstance(x, int))    # True
print(type(x).__name__)      # 'int'