# program 33 :
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
def sqr_dict():
    result_dict = {}
    for num in range(1, 4):
        result_dict[num] = num **2
    print(" Dictionary",result_dict)
sqr_dict()