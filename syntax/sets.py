# import random

# def random_number(min_val, max_val):
#     """Generatges an integer between min_val and max_val  
    
#     Args:
#         min_val (int): Minimum value
#         max_val (int): Maximum value
        
#     Returns:
#         int: Random integer between min_val and max_val
#     """

#     return random.randint(min_val, max_val)

# generated_number = random_number(0, 100)
# print(f"Generated number: {generated_number}")

# def check_service_status(service_name, expected_status):
#     print(f"Checking {service_name} for {expected_status} status...")
#     return True

# check_service_status("nginx", "active")
# check_service_status("active", "nginx")

# check_service_status(service_name="nginx", expected_status="active")
# check_service_status(expected_status="active", service_name="nginx")

def connect(host, port, timeout):
    print(f"Connect to host {host} on port {port} with timeout {timeout}")

connect(host="web01",port=443, timeout=40)
