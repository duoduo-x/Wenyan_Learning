class Restaurant() :
    """一个模拟餐馆的尝试"""

    def __init__(self,name,type):
        """初始化餐馆的信息"""
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is" + self.name.title() + ", " + "type is " + self.type.upper() + "." )

    def open_restaurant(self):
        print("The restaurant" + self.name.title() + "is open.")

    def print_number_served(self):
        print('the restaurant have ' + str(self.number_served) + '.')

    def set_number_served(self,number):
        self.number_served = number

    def increment_served(self,add_number):
        self.number_served += add_number

restaurant = Restaurant('wenyan','chinese')
restaurant.number_served = 500
restaurant.print_number_served()
restaurant.set_number_served(600)
restaurant.print_number_served()
restaurant.increment_served(200)
restaurant.print_number_served()


class IceCreamStand(Restaurant):
    def __init__(self,name,type,):
        super().__init__(name,type)
        self.flavors = []

    def set_flavors(self,smell):
        self.flavors = smell

my_icecream = IceCreamStand('luo','swedish')
my_icecream.set_flavors(['strawberry','banana','chocklate'])
print(my_icecream.flavors)