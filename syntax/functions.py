# Basic function
def check_service_status(service_name):
    """Check if a service is running."""
    print(f"Checking {service_name}...")
    return "active"

# Function with default parameters
def connect_database(host="localhost", port=5432, timeout=30):
    """Connect to a database with default host, port, and timeout."""
    return f"Connecting to {host}:{port} (timeout: {timeout}s)"

# Function with *args and **kwargs
def log_message(level, message, *tags, **metadata):
    """Log messages with flexible tagging and metadata."""
    print(f"[{level}] {message}")
    print(f"Tags: {tags}")
    print(f"Metadata: {metadata}")

log_message("INFO", "Server started", "web", "production", 
           timestamp="2024-01-01", user="admin")

# Return multiple values
def get_system_info():
    """Fetch system metrics: CPU, memory, and disk usage."""
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
    """Retry a function once if it fails."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function failed: {e}, retrying...")
            return func(*args, **kwargs)
    return wrapper

@retry_on_failure
def unreliable_function():
    """Simulate flaky function, like an unstable API call or service check."""
    import random
    if random.random() < 0.5:
        raise Exception("Random failure")
    return "Success"

# Function to simulate retry logic for restarting failed services
def restart_service(name, retries=3):
    """Restart a failed service with retry logic."""
    for attempt in range(1, retries + 1):
        print(f"Attempt {attempt}: Restarting {name}...")
        # Simulate restart attempt
        if attempt == retries:
            print(f"{name} restarted successfully.")
            return True
    return False

# Function to simulate checking available ports (instead of prime number logic)
def is_port_available(port):
    """
    Simulate checking if a given port is available.
    (Replaces prime check with port check logic.)
    """
    reserved_ports = [22, 80, 443, 5432]
    return port not in reserved_ports

# Example usage
print(f"Is port 8080 available? {is_port_available(8080)}")
