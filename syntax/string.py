# String creation and basic operations
name = "DevOps Engineer"
message = f"Hello, {name}!"  
old_style = "Hello, {}!".format(name)  

# String methods
text = "  Python DevOps  "
print(text.strip())           
print(text.lower())          
print(text.upper())           
print(text.replace("Python", "Java"))  

# String checking
email = "admin@company.com"
print(email.startswith("admin"))     
print(email.endswith(".com"))        
print("@" in email)                  
print(email.isdigit())              

# String splitting and joining
path = "/var/log/app.log"
parts = path.split("/")              # ['', 'var', 'log', 'app.log']
new_path = "/".join(parts)           # Rejoin with /

# Multiline strings
config = """
server:
  host: localhost
  port: 8080
"""