def castle_if(a, b, c, d, e):
    a, b, c = sorted([a, b, c])
    d, e = sorted([d, e])
    if d >= a and b >= e:
        return "YES"
    return  "NO"


assert castle_if(1, 1, 1, 1, 1) == "YES"
assert castle_if(2, 2, 2, 1, 1) == "NO"


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = castle_if(a, b, c, d, e)
    print(ans)


if __name__ == "__main__":
    main()
