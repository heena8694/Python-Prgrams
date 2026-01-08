#program004:
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
txt = input("Enter a accepts a sequence of comma-separated numbers")
list1 = txt.split(",")
tuple1 = tuple(list1)
print(list1)
print(tuple1)