# String is sequence of characters enclosed within quotes

str1 = "Python is awesome!"
print("\u0061")
print("\U0001f600")


name1 = "Python"
name2 = "Python"

print(name1 == name2)

# Triple quotes
poem = """In silent nights, a dream takes flight, 
A spark within the calmest light. Though small it seems, 
it dares to glow, And lights the path you didn’t know."""
print(poem)

directory = "C:\\Users\Sushan\Documents"
print(directory)


# String concatenation

# a = "lal"
# b = "mohan"

# print(a + " " + b)

age = 22
message = "My age is " + str(age)
print(message)

city = "New York"
temp = 30

weatherReport = "The temperature in " + city + " is " + str(temp) + " degrees."
print(weatherReport)

weatherReport = f"The temperature in {city} is {temp} degrees."
print(weatherReport)

weatherReport = "The temperature in {} is {} degrees.".format(city, temp)
print(weatherReport)

star = "*"
print((star * 5 + "\n") * 5)

print("apple" == "apple")
print("apple" == "Apple")
print("apple" == "orange")
print("apple" != "orange")

print()

msg = "Hello"
res = len(msg)
print(res)





