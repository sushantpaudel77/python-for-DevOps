class Cloud:
    # name = "google cloud"
    def __init__(self, fullname):
        # print(self)
        self.name = fullname
        print("adding new student in databases..")

newCloud1 = Cloud("Google Cloud")
print(newCloud1.name)

newCloud2 = Cloud("AWS")
print(newCloud2.name)

# class Car:
#     color = "Blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)