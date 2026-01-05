#1.
'''l =[]
for i in range(2000,3201):
    if(i% 7 ==0) and (i%5!=0):
        l.append(str(i))
print(" ".join(l))'''
#2.
'''def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)
x = input("Enter number")
print(fact())'''
#3.
'''n = int(input("enter number in coma seprated"))
d = dict()
for i in range(1, n + 1):
    d[i]=i*i
print(d)'''
#4.
'''txt = input("Enter here:")
list1 = txt.split(",")
tuple1 = tuple(list1)
print(list1)
print(tuple1)'''
#5.
'''class Person:
    def __init__(self,name=none):
        self.name = name
    def info(self):
        print(self.name)
riya = Person('riya')
riya.info()'''
#6.
'''class Person:
    name = "Person"
    def __init__(self,name=None):
        self.name=name
riya = Person('riya')
#print("Name is",riya.name)
print("%s Name is %",(Person.name,riya.name))
jiya = Person()
jiya.name = ('jiya')
print("%s Name is %s",(Person.name,jiya.name))'''
#7.
'''def printlist():
    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])
printlist()'''
#8
'''class Circle(object):
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
acircle = Circle(5)
print("Area of circle",acircle.area())'''

#9.
'''def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)
n = int(input("Enter here"))
print(f(n))'''
#10.

