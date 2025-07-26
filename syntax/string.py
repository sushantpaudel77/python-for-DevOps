# String creation and basic operations
name = "DevOps Engineer"
message = f"Hello, {name}!"  # f-string (preferred)
old_style = "Hello, {}!".format(name)  # format method

# String methods
text = "  Python DevOps  "
print(text.strip())  # Remove whitespace
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.replace("Python", "Java"))  # Replace substring

# String checking
email = "admin@company.com"
print(email.startswith("admin"))  # True
print(email.endswith(".com"))  # True
print("@" in email)  # True
print(email.isdigit())  # False

# String splitting and joining
path = "/var/log/app.log"
parts = path.split("/")  # ['', 'var', 'log', 'app.log']
new_path = "/".join(parts)  # Rejoin with /

# Multiline strings
config = """
server:
  host: localhost
  port: 8080
"""
