# integer operations
count = 10
total = count + 5
print(total // 3)  # floor division: 5
print(total % 3)  # modulo: 0
print(total**2)  # power: 225

# float operations
cpu_usage = 45.7
memory_usage = 67.2
average = (cpu_usage + memory_usage) / 2

# number conversions
port = "8080"
port_num = int(port)  # string to int
cpu_str = str(cpu_usage)  # float to string

# math operations
import math

print(math.ceil(45.2))  # 46
print(math.floor(45.8))  # 45
print(round(45.562, 2))  # 45.57w

# number checking
x = 42
print(isinstance(x, int))  # true
print(type(x).__name__)  # 'int'

# absolute value and sign check
temperature = -12
print(abs(temperature))  # 12
print(math.copysign(1, temperature))  # -1.0 (returns sign of value)

# random number generation
import random
print(random.randint(1, 100))  # random integer between 1 and 100
print(round(random.uniform(1.5, 5.5), 2))  # random float between 1.5 and 5.5 rounded to 2 decimal


# random number generation
import random
print(random.randint(0, 100))  # random integer between 1 and 100
print(round(random.uniform(1.5, 5.5), 2))  # random float between 1.5 and 5.5 rounded to 2 decimal