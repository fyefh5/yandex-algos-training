a = float(input())
b = float(input())
c = float(input())

c1 = a + b
a1 = b + c
b1 = a + c

if c < c1 and a < a1 and b < b1:
    print("YES")
else:
    print("NO")