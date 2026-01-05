#1.
# program010 :

# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

# Suppose the following input is supplied to the
# program:
# hello world and practice makes perfect and hello world again

# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it
# should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then
# use sorted() to sort the data.

'''txt= input("Enter sequence of whitespace separated words:")
txt =sorted(set(txt.split()))
print(" " .join(txt))'''

#2.
# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# all logic should be in side main method only

'''def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)
x = int(input("Enter a number"))
print(factorial(x))'''
#3.
# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98s

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# tuple() method can convert list to tuple
# all logic should be in side main method only
'''txt =input("Enter a sequence of comma-separated numbers: ")
list1 = txt.split(",")
tuple1 = list(list1)
print(list1)
print(tuple1)'''
#4.
# Write a program that calculates and prints the value according to the
# given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a
# comma-separated sequence.

# Example
# Let us assume the following comma separated input sequence
# is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form,
# it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
import math
c =50
h = 30
input_value = input("enter a value")
d = input_value.split(",")
q = []
for values in d:
    input_value = int(values)
    q.append(str(int(math.sqrt(2 * c * values)/h)))

print(" ".join(q))
