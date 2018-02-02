class User():

    def __init__(self,first_name,last_name,sex,age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print('The people name is ' + self.first_name.title() + " " +self.last_name + ", sex is" + self.sex + ", age is " + str(self.age) + ".")

    def greet_user(self):
        print("hello," + self.first_name.title() +" " + self.last_name.lower() + "." )

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0

first_user = User('geng','wenyan','女',30)
first_user.describe_user()
first_user.greet_user()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.reset_login_attempts()
print(first_user.login_attempts)

class Admin(User):

    def __init__(self,first_name,last_name,sex,age):
        super().__init__(first_name,last_name,sex,age)
        self.privieges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(self.privieges)

new_admin = Admin('luo','xiao','男','35')
new_admin.show_privileges()