#program002 :
# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# all logic should be in side main method only'''
def factorial(x):
	if x == 0:
		return 1
	return x * factorial(x - 1)
x = int(input("Enter a number"))
print(factorial(x))