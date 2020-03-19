n= int(input())
sum=0
a=[]


a = [int(s) for s in input().split()]

# for i in range(1,n-1):
#     if a[i+1]>0 and a[i]>0 and a[i-1]>0:
#         break
#         print("YES")
#     elif a[i+1]<0 and a[i]<0 and a[i-1]<0:
#         break
#         print("YES")
#     else:
#         print("NO")
i=1
while i<n-1:

    if a[i+1]>0 and a[i]>0 and a[i-1]>0:
        print("YES")
        break
    elif a[i+1]<0 and a[i]<0 and a[i-1]<0:
        print("YES")
        break
    elif a[i + 1] == 0 and a[i]== 0 and a[i - 1] == 0:
        print("YES")
        break
    else:
        i+=1
        if i==n-1:
            print("NO")
