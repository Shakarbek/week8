# a= int(input())
# n=int(input())
a, n = map(int, input().split())

#a, n = (int(i) for i in input().split())

def power(a1,n1):
    p=pow(a1,n1)
    print(p)

power(a, n)