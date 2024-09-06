def details(n, k, m):
    count = 0
    while n // k > 0:
        remainder1 = n % k
        workpieces = n // k
        remainder2 = (k % m) * workpieces
        count += k // m * workpieces
        n = remainder1 + remainder2
    return count

# assert details(10, 5, 2) == 4
# assert details(13, 5, 3) == 3
# assert details(14, 5, 3) == 4

def main():
    n, k, m = map(int, input().split())
    ans = details(n,k,m)
    print(ans)

if __name__ == "__main__":
    main()