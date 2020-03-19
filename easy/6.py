def leap_year(a):
    b=bool
    if a % 4 == 0 and a % 100 != 0:
        b=True
        print(b)

    elif a % 400 == 0:
        # print("YES")
        b=True
        print(b)
    else:
        # print("NO")
        b=False
        print(b)


y = int(input())
leap_year(y)