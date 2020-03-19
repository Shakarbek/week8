n= int(input())
sum=0
a=[]
# for i in range(n):
    # a = [int(k) for k in input().split()]
    # k=int(input())
    # a.append(k)

a = [int(s) for s in input().split()]

for i in range(0,n):
    if a[i]>0:
        sum+=1

print(sum)