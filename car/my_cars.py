from car import Car
from car.electric_car import ElectricCar

my_beetle = Car('volvo','beetle',2014)
print(my_beetle.get_descriptive())

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive())
