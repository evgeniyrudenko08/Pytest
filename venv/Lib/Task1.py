import math
import collections
import string
import random
'''
#1

x=1
a= math.sin(x)
b= math.cos(x)
c=a/b
d=b/a

if c > d:
    print(str(c))
else:
    print(str(d))


#2
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for index, fibonacci_number in zip(range(7), fib()):
    if fibonacci_number % 2 == 0:
        print('{i:3}: {f:3}'.format(i=index, f=str(fibonacci_number) + " " + "is even"))
    elif fibonacci_number % 2 == 1:
        print('{i:3}: {f:3}'.format(i=index, f=str(fibonacci_number)))
'''
#6
'''
def list2(list1, text, text1):
    list1.remove(text)
    list1.append(text1)
    print(list1)
list2(['ttt', 'yyyy'],'yyyy','sometext')

#7

def login(d):
    result = True
    for u, p in d.items():
        if u.__eq__('Admin') + p.__eq__('sigma'):
            print("access denied with creds: " + u,p)
            print (result == False)
        elif u.__eq__('Addd')  + p.__eq__('Rrrr'):
            print("access ok with creds: " + u,p)
            print (result == True)

d = {"Admin":"sigma", "Addd": "Rrrr"}
login(d)
'''
def returnList():
    X = int(input("Enter X:"))
    Y = int(input("Enter Y:"))
    number = list(str(random.randrange(0, Y, X)))
    print(number)
returnList()








