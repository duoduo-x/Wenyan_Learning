class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading +=miles

    def fill_gas_tank(self,full):
        self.gas_tank =full
        print("This car " + str(self.gas_tank) +"l gas .")

my_new_car = Car("audi", 'a4',2016)
print(my_new_car.get_descriptive())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(46)
my_new_car.read_odometer()
my_new_car.update_odometer(47)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.fill_gas_tank(200)


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

    def upgrade_battery(self):
        if self.bettery_size != 85:
            self.bettery_size = 85

new_battery = Battery()
new_battery.get_range()
new_battery.upgrade_battery()
new_battery.get_range()

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('This car does not need a gas tank')

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
