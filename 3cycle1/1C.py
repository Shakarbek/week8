import math

a=int(input())
b=int(input())

for i in range(a,b+1):
    if i**2>=a and i**2<=b:
        print(i**2)