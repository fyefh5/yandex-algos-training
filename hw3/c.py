def main():
    n, m = tuple(map(int, input().split()))
    anya = set()
    borya = set()
    for _ in range(n):
        anya.add(int(input()))
    for _ in range(m):
        borya.add(int(input()))
    common = anya.intersection(borya)
    print(len(common))
    print(" ".join(map(str, sorted(common))))
    rest_anya = anya.difference(borya)
    rest_borya = borya.difference(anya)
    print(len(rest_anya))
    print(" ".join(map(str, sorted(rest_anya))))
    print(len(rest_borya))
    print(" ".join(map(str, sorted(rest_borya))))


if __name__ == "__main__":
    main()