def can(a, b, c, d, e):
    cond1 = (d >= a, d >= b, d >= c)
    cond2 = (e >= a, e >= b, e >= c)
    fits = 0
    for i in range(3):
        if cond1[i] or cond2[i]:
            fits += 1
    if fits >= 2:
        return "YES"
    return "NO"


assert can(1, 1, 1, 1, 1) == "YES"
assert can(2, 2, 2, 1, 1) == "NO"


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = can(a, b, c, d, e)
    print(ans)


if __name__ == "__main__":
    main()
