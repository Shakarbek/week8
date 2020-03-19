a=[]
n=int(input())

a = [int(s) for s in input().split()]
i=0
for o in range(n):
    a[n-i-1], a[i] = a[i], a[n-i-1]
    i+=1
    if i>n/2-1:
        break

print(' '.join([str(i) for i in a]))