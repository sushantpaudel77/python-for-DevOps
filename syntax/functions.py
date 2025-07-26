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