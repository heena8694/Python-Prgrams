# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values
# in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl1 = tuple1[:5]
tpl2 = tuple1[5:]
print(tpl1)
print(tpl2)