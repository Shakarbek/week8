n= int(input())

a=[]
for i in range(n):
    k=int(input())
    a.append(k)

for i in range(0,n):
    if a[i]%2==0:
        print(a[i])