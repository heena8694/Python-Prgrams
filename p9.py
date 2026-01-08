# program005:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class IOstring():
    def getString(self):
        self.s = input("Enter a text:")
    def printString(self):
        print(self.s.upper())

str_obj = IOstring()
str_obj.getString()
str_obj.printString()