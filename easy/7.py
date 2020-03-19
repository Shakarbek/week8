n=int(input())
a=[]
def my_func(n):
    for i in range(1,n+1):
        a.append(i)
    print(''.join([str(i) for i in a]))

my_func(n)