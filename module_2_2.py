a=first=int(input())
b=second=int(input())
c=third=int(input())
if a==b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)
