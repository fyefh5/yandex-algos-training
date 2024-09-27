with open("hw3/input_g.txt", "r") as f:
    n = int(f.readline())
    cnt = 0
    was = set()
    for i in range(n):
        a, b = tuple(map(int, f.readline().split()))
        if a >= 0 and b >= 0 and a + b == n - 1 and ((a, b) not in was):
            was.add((a, b))
            cnt += 1
    print(cnt)