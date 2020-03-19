s=str(input())
for i in (0, len(s)-1):
    if s[i].isupper()==True:
        s[i].lower()
    else:
        s[i].upper()
    print(s[i])
