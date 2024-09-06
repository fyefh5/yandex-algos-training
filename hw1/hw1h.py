def waiting(a, b, n, m):
    time1min = 1 + (a+1)*(n-1)
    time1max = (a+1)*n + a
    time2min = 1 + (b+1)*(m-1)
    time2max = (b+1)*m + b
    if time2min > time1max or time1min > time2max:
        return -1
    timemin = max(time1min, time2min)
    timemax = min(time1max, time2max)
    return timemin, timemax


assert waiting(1, 3, 3, 2) == (5, 7)
assert waiting(1, 5, 1, 2) == -1


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())
    ans = waiting(a, b, n, m)
    print(-1 if ans == -1 else " ".join(map(str, ans)))


if __name__ == "__main__":
    main()
