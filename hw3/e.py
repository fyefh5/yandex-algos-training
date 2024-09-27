buttons = set(map(int, input().split()))
s = set()
number = int(input())
while number > 0:
    digit = number % 10
    if digit not in buttons:
        s.add(digit)
    number = number // 10
print(len(s))
