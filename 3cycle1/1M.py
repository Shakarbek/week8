n=int(input())
a=[]
sum=0
for i in range(n):
    x=int(input())
    a.append(x)

for i in range(0, n):
    if a[i]==0:
        sum=sum+1

print(sum)