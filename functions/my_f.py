def money_with_bonus(a,b):
    res=int(a+a*b/100)
    print(str(res)+"$")

a, b = map(int, input().split())

money_with_bonus(a,b)