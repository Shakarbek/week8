n= int(input())
sum=0
a=[]


a = [int(s) for s in input().split()]

i=1
while i<n-1:

    if a[i+1]<a[i] and a[i-1]<a[i]:
        sum+=1
    i+=1

print(sum)