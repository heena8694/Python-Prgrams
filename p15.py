# program 31 :
# Define a function that can accept two strings as input
# and print the string with maximum length in console.
# If two strings have the same length, then the function
# should print all strings line by line.

# Hints:
# Use len() function to get the length of a string

def check_length(str1, str2):
    return len(str1) == len(str2)
s1 = "hello"
s2 = "world"
s3 = "python"
print(check_length(s1, s2))
print(check_length(s1, s3))