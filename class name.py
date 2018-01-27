class User():

    def __init__(self,first_name,last_name,sex,age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print('The people name is ' + self.first_name.title() + " " +self.last_name + ", sex is" + self.sex + ", age is " + str(self.age) + ".")

    def greet_user(self):
        print("hello," + self.first_name.title() +" " + self.last_name.lower() + "." )

first_user = User('geng','wenyan','女',30)
first_user.describe_user()
first_user.greet_user()

second_user = User('luo','xiao','男',35)
second_user.greet_user()
second_user.describe_user()