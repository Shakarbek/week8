n= int(input())
sum=0
a=[]
# for i in range(n):
    # a = [int(k) for k in input().split()]

    # a.append(int(input()))
# a = [ int(input()) for i in range(n) ]

# b= list(int(input().split()))

a = [int(s) for s in input().split()]

for i in range(0,n-1):
    if a[i+1]>a[i]:
        sum+=1

print(sum)