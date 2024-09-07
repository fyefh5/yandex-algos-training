def big_count(arr):
    cnt = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            cnt += 1
    return cnt


assert big_count([1, 2, 3, 4, 5]) == 0
assert big_count([5, 4, 3, 2, 1]) == 0
assert big_count([1, 5, 1, 5, 1]) == 2


def main():
    arr = tuple(map(int, input().split()))
    print(big_count(arr))


if __name__ == "__main__":
    main()
