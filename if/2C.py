a = int(input())
b = int(input())

a1=int((a/1000))%10
a2=int((a/100))%10
a3=int((a/10))%10
a4=a%10

if a1==a4 and a2==a3:
    if b==1:
        print("YES")
    else:
        print("NO")
else:
    if b!=1:
        print("YES")
    else:
        print("NO")