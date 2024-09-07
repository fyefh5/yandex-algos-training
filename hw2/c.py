def closest(arr, x):
    mindist = abs(arr[0] - x)
    imindist = 0
    for i in range(len(arr)):
        dist = abs(arr[i] - x)
        if dist < mindist:
            mindist = dist
            imindist = i
    return arr[imindist]

assert closest([1, 2, 3, 4, 5], 6) == 5
assert closest([5, 4, 3, 2, 1], 3) == 3


def main():
    lenarr = int(input())
    arr = tuple(map(int, input().split()))
    x = int(input())
    print(closest(arr, x))


if __name__ == "__main__":
    main()
