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

my_restaurant = Restaurant('WENYAN','CHINESE')
print(my_restaurant.name.title() + "\n" + my_restaurant.type.upper())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

luo_restaurant = Restaurant('luo','tai')
xiao_restaurant = Restaurant('xiao','yuenan')
luo_restaurant.describe_restaurant()
xiao_restaurant.describe_restaurant()