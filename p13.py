# program 25 :

# Define a class, which have a class parameter and have a same instance
# parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later

class MyClass:
    x = 10
    def __init__(self, x):
        self.x = x
obj = MyClass(20)
print(obj.x)
print(MyClass.x)