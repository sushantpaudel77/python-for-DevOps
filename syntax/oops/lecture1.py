class CloudProvider:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        print(f"Provisioning {self.name} in {self.region} region...")

    def info(self):
        return f"{self.name} operates in {self.region}"

# Creating instances of CloudProvider
provider1 = CloudProvider("Google Cloud", "us-central1")
print(provider1.info())

provider2 = CloudProvider("AWS", "eu-west-1")
print(provider2.info())

provider3 = CloudProvider("Azure", "asia-east")
print(provider3.info())

# Another example: Car class
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def description(self):
        return f"{self.color} {self.brand}"

car1 = Car("Blue", "Mercedes")
print(car1.description())

car2 = Car("Red", "Toyota")
print(car2.description())