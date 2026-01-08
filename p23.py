# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr_map = map(lambda x : x **2, num)
sqr_list = list(sqr_map)
print(sqr_list)