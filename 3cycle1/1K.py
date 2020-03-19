n=int(input())
a=[]
sum=0
for i in range(n):
    x=int(input())
    a.append(x)

for i in range(0, n):
    sum=sum+a[i]

print(sum)