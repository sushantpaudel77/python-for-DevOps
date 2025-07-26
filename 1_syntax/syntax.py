print("Hello World!")

x = 5
y = 6

add = x + y
sub = x - y
mul = x * y
print('Addition is:', add, 'Subtraction is:', sub, 'Multiply:', mul)

my_list = [1,2,3,4,5, 'Sushant']
print(my_list)

print(my_list[2])
print(my_list[5])


my_list[0] = 'DevOps'

print("MyList:", my_list)

for item in my_list:
    print(item)

print(' '.join(str(item) for item in my_list))


my_tuple = (1,2,3,4,5,6,7, "Python is awesome")
print(my_tuple)

print(my_tuple[4])

# my_tuple[4] = 77
print(my_tuple)


person = {'name': 'Alice', 'age': 22, 'city': 'London', 'gender': 'female'}
print('Person:', person)
print(person['name'])


my_set = {1,2,3,5,6,1,3,2,77,33,44,66,77,88,44}
print(my_set)

res = my_set.append(11)
print("Appended:", res)