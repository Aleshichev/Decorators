# class Person:
#     # конструктор
#     def __init__(self):
#         print("Создание объекта Person")
#
#     def say_hello(self):
#         print("Hello")
#
#
# tom = Person()
# can = Person()
# can.say_hello()
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name  # имя человека
#         self.age = 1  # возраст человека
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom")
# tom.age = 4
#
# tom.display_info()

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
      if args[0].is_logged_in == True:
          function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Igor")
new_user.is_logged_in = True
create_blog_post(new_user)
