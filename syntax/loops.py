# For loop with list
servers = ["web1", "web2", "db1"]
for server in servers:
    print(f"Checking {server}")

for i in range(5):
    print(f"Iteration {i}")

for i in range(1, 6):
    print(f"Number {i}")

for i in range(0, 10, 2):
    print(f"Even: {i}")

# New loop example 1: Looping through dictionary
server_status = {"web1": "active", "web2": "inactive", "db1": "active"}
for server, status in server_status.items():
    print(f"{server} is {status}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# New loop example 2: While loop with break condition
attempts = 0
max_attempts = 3
while True:
    print(f"Attempt {attempts + 1}")
    attempts += 1
    if attempts >= max_attempts:
        print("Max attempts reached")
        break

# Enumerate (get index and value)
services = ["nginx", "mysql", "redis"]
for index, service in enumerate(services):
    print(f"{index}: {service}")

# Loop with else (runs if loop completes normally)
for i in range(3):
    print(i)
else:
    print("Loop completed")

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(i)