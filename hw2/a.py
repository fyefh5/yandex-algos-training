def monotonical(arr):
    if len(arr) == 0 or len(arr) == 1:
        return "YES"
    for i in range(1,len(arr)):
        if arr[i-1] >= arr[i]:
            return "NO"
    return "YES"

assert monotonical([1, 7, 9]) == "YES"
assert monotonical([1, 9, 7]) == "NO"
assert monotonical([2, 2, 2]) == "NO"

def main():
    arr = list(map(float, input().split()))
    print(monotonical(arr))

if __name__ == "__main__":
    main()