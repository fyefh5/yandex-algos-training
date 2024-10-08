def solve(a, b, c, d, e, f):
    if (a, b, c, d, e, f) == (0, 0, 0, 0, 0, 0):
        return [5]  # whole space

    if (a, b) == (0, 0) and e != 0:
        return [0]  # error, no answer

    if (c, d) == (0, 0) and f != 0:
        return [0]  # error, no answer

    if (a, b) == (0, 0):
        if c == 0:
            return [4, f / d]  # imposition horizontally
        if d == 0:
            return [3, f / c]  # imposition vertically
        return [1, -c / d, f / d]  # imposition angled

    if (c, d) == (0, 0):
        if a == 0:
            return [4, e / b]  # imposition horizontally
        if b == 0:
            return [3, e / a]  # imposition vertically
        return [1, -a / b, e / b]  # imposition angled

    if (a, c) == (0, 0):
        if e / b == f / d:
            return [4, e / b]  # imposition vertically
        return [0]  # parallel vertically

    if (b, d) == (0, 0):
        if e / a == f / c:
            return [3, e / a]  # imposition horizontally
        return [0]  # parallel horizontally

    if b == 0 or d == 0:
        x0 = (b * f - e * d) / (b * c - a * d)
        y0 = (e * c - a * f) / (b * c - a * d)
        return [2, x0, y0]  # intersection

    if a / b == c / d:
        if e / b == f / d:
            return [1, -a / b, e / b]  # imposition angled
        return [0]  # parallel angled

    x0 = (b * f - e * d) / (b * c - a * d)
    y0 = (e * c - a * f) / (b * c - a * d)
    return [2, x0, y0]  # intersection


assert solve(1, 0, 0, 1, 3, 3) == [2, 3, 3]
assert solve(1, 1, 2, 2, 1, 2) == [1, -1, 1]
assert solve(0, 2, 0, 4, 1, 2) == [4, 0.5]

assert solve(1, 0, 0, 1, 3, 3) ==   [2, 3, 3              ]
assert solve(2, 2, 3, -3, 6, -3) == [2, 1, 2              ]
assert solve(1, 1, 1, -1, 3, -1) == [2, 1, 2              ]
assert solve(1, 1, 2, 2, 1, 2) ==   [1, -1, 1             ]
assert solve(1, 1, 1, 1, 1, 2) ==   [0                    ]
assert solve(0, 1, 0, 1, 2, 3) ==   [0                    ]
assert solve(0, 1, 0, 2, 2, 4) ==   [4, 2                 ]
assert solve(1, 0, 2, 0, 2, 4) ==   [3, 2                 ]
assert solve(0, 0, 0, 0, 0, 0) ==   [5                    ]
assert solve(0, 0, 0, 0, 1, 0) ==   [0                    ]
assert solve(0, 2, 0, 4, 1, 2) ==   [4, 0.5               ]
assert solve(0, 2, 0, 4, 1, 2) ==   [4, 0.5               ]
assert solve(0, 0, 2, 4, 0, 2) ==   [1, -0.50000, 0.50000 ]
assert solve(2, 4, 0, 0, 2, 0) ==   [1, -0.50000, 0.50000 ]
assert solve(2, 0, 3, 0, 2, 3) ==   [3, 1.00000           ]
assert solve(2, 2, 3, 0, 6, 3) ==   [2, 1.00000, 2.00000  ]
assert solve(1, 1, 1.5, 0, 3, 1.5) == [2, 1.00000, 2.00000]


def main():
    a, b, c, d, e, f = [float(input()) for _ in range(6)]
    ans = solve(a, b, c, d, e, f)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
