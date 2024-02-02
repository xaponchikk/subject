# def get_user_info():
#     age = 10
#     name = 'Arthur'
#     return name, age
#
#
# def get_user_image():
#     picture_url = '123'
#     return picture_url
#
# def get_user_friends():
#     friends = ['Alice', 'Mike', 'George']
#     return len(friends)
#
#
# def main():
#     name, age = get_user_info()
#     picture_url = get_user_image()
#     friends = get_user_friends()
#
#     print('==== USER INFO ====')
#     print('Name:', name)
#     print('Age', age)
#     print('Profile picture:', picture_url)
#     print('Friends: ', friends)
#
#
# main()

# def function_to_decorade():
#     pass
#
# def my_shiny_decorator(function_to_decorate):
#
#     def the_wrapper_around_function():
#         print(f'я код, который сработает до вызова')
#         function_to_decorate()
#         print(f'я сработаю после')
#     return the_wrapper_around_function()
#
#
# def stand_alone_function():
#     print(f'я одинокая функция')
#
# stand_alone_function()





# @my_shiny_decorator
# def stand_alone_another_func():
#     print(f'Оставь меня в покое')


# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#
#
#     def display_info(self):
#         print(f'Name: {self.name}\nAge: {self.age}')
#
# tom = Person('Tom')
#
# tom.display_info()
# print('-----------------------')
#
# bob = Person('Bob')
# bob.age = 41
# bob.display_info()

# class SomeClass:
#     pass
#
# class MyDict(dict):
#     def get(self, key, default = 0):
#         return dict.get(self, key, default)
#
#
# b = MyDict(a=1, b = 4, l = 6)
# b['k'] = 4
# b['V'] = 6
# print(b)
# print(b.get('V'))

class RegistryClass(type):
    registry = {}

    def __new__(typ, name, bases, dct):
        new_class = super().__new__(typ, name, bases, dct)
        typ.registry[name] = new_class
        return new_class


class Base(metaclass=RegistryClass):
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

print(RegistryClass.registry)

