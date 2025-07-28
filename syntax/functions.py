# Basic function
def check_service_status(service_name):
    """Check if a service is running."""
    print(f"Checking {service_name}...")
    return "active"

# Function with default parameters
def connect_database(host="localhost", port=5432, timeout=30):
    return f"Connecting to {host}:{port} (timeout: {timeout}s)"

# Function with *args and **kwargs
def log_message(level, message, *tags, **metadata):
    print(f"[{level}] {message}")
    print(f"Tags: {tags}")
    print(f"Metadata: {metadata}")

log_message("INFO", "Server started", "web", "production", 
           timestamp="2024-01-01", user="admin")

# Return multiple values
def get_system_info():
    cpu = 45.2
    memory = 67.8
    disk = 30.1
    return cpu, memory, disk

cpu, mem, disk = get_system_info()

# Lambda functions (anonymous functions)
servers = ["web1", "web2", "db1"]
web_servers = list(filter(lambda x: x.startswith("web"), servers))
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))

# Decorator example
def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function failed: {e}, retrying...")
            return func(*args, **kwargs)
    return wrapper

@retry_on_failure
def unreliable_function():
    import random
    if random.random() < 0.5:
        raise Exception("Random failure")
    return "Success"


# Function to calculate the factorial of a number
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Returns 1 for n=0.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(f"Factorial of 5 is {factorial(5)}")


# Function to check if a number is prime
def is_prime(n):
    """
    Check if a given number n is a prime number.
    Returns True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(f"Is 7 prime? {is_prime(7)}")