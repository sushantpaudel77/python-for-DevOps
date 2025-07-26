# String Methods
text = "Hello world!"
print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("World", "Python"))
print(text.startswith("He"))
print(text.endswith("!"))
print(text.count("l"))
print(text.find("World"))


# String Slicing
msg = "Python"
print(msg[0])
print(msg[-1])
print(msg[0:3])
print(msg[::2])

# String Immutability
msg = "Hello"
# msg[0] = "J" This will raise an error
print(msg)


# String Iteration
for char in "Hello":
    print(char)

# Joining and Splitting
words = ["Python", "is", "fun"]
joined = " ".join(words)
split = joined.split()
print(split)

# Escape Sequences
print("Line1\nLine2")   # Newline
print("He said \"Hi\"") # Quotes
print("Tab\tSpace")     # Tab

# String Formatting Advanced
price = 49.995
print(f"Price: ${price:.2f}")

name = "Alice"
print(f"{name:>10}")

# ASCII & Unicode
print(ord('A'))
print(chr(65))

# Check if string is 
print("abc".isalpha())  
print("123".isdigit())  
print("abc123".isalnum())  
print("   ".isspace())  