def castle_if(brick, hole):
    brick = sorted(brick)
    hole = sorted(hole)
    return "YES" if brick[0] <= hole[0] and brick[1] <= hole[1] else "NO"


assert castle_if([1, 1, 1], [1, 1]) == "YES"
assert castle_if([2, 2, 2], [1, 1]) == "NO"


def main():
    brick = [int(input()) for _ in range(3)]
    hole = [int(input()) for _ in range(2)]
    ans = castle_if(brick, hole)
    print(ans)


if __name__ == "__main__":
    main()
