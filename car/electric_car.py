from car import Car

class Battery():
    def __init__(self, battery_size=70):
        self.bettery_size = battery_size

    def describe_battery(self):
        print("this car " + str(self.bettery_size) + ".")

    def get_range(self):
        if self.bettery_size ==70:
            range = 240
        elif self.bettery_size ==85:
            range = 270
        message = "This car can go qpproximately " + str(range)
        message += "miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
