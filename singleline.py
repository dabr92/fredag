import random
x = 0
while random.randrange(0,100) != 20:
    print(end="")

'''
for i in range(0,11):
    print(i)

for i in range(0,11):
    print(i,"* 5 =",i*5)

for i in range(0,11):
    print(i,"^ ",i," =",i**i)
    

print("----------------------")
print("EXPONENTIELL BERÄKNING")
print("----------------------")
for i in range(10,-1,-1):
    print(i,"^ ",i," =",i**i)


def expo():
    exp1 = int(input("<från vilket nummer"))
    exp2 = int(input("till vilket nummer"))
    exp3 = int(input("hur stora steg"))
    print("----------------------")
    print("EXPONENTIELL BERÄKNING")
    print("----------------------")
    for i in range(exp1,exp2,exp3):
        print(i,"^ ",i," =",i**i)

expo()

x = 4
y = 3
matrix = [[0 for q in range (x)]for w in range(y)]
print(matrix)

x = 4
y = 3
z = 0
nummer = 0
for q in range(x):
    print()
    print(" ------------")
    print(end="|")
    for w in range(y):
        nummer = nummer +1
        print(q**4, end="|")
print("\n ------------")


p = 0
o = 1
nummer = 0
while p <= 3:
    print()
    p += 1
    o = o == 0
    while o <=3:
        nummer +=1
        o = o+ 1
        print("",nummer**4, end="")


x = 20
y = 10
z = x
x = y
y = z
print("x är",x,"\ny är",y)

x = 10
y = 20
x,y=y,x


print("x är",x,"\ny är",y)

import sys
print("Skriv ditt namn: ", end="")
print("Hej",sys.stdin.readline())

x = 0
while x <15:
    x +=1
    print("hello")
'''

ord1 = input("skriv första ordet\n")
ord2 = input("skriv andra order\n")
ord3 = ord1+ord2+"femton"
print(ord3)