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

restaurant = Restaurant('wenyan','chinese')
restaurant.set_number_served(500)
restaurant.print_number_served()

# Add something here

