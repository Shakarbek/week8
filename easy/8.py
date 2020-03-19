n= int(input())
a = [int(s) for s in input().split()]

for i in range(0,n):
    if a[i]==max(a):
        a[i]=0

m=max(a)
print(m)