k1_flat, m, k2_flat, i2, j2 = list(map(int, input().split()))
k1_flat -= 1  # index of apartment for event 1
k2_flat -= 1  # index of apartment for event 2
i2 -= 1  # index of entry for event 2
j2 -= 1  # index of floor for event 2
# m is the number of floors in the building

# model:
# house is the 3d-array where 1d - entries, 2d - floor, 3d - apt
# house.shape = (entries, floors, apts)= (l, m, n), where only m is known
# with coordinates for each dimension = i, j, k
# flattened version for each apt is referred as k_flat
# for each floor - j_flat


def solve(k1_flat, m, k2_flat, i2, j2):
    if any([k1_flat < 0, m < 1, k2_flat < 0, i2 < 0, j2 < 0]):
        return -2, -2
    if j2 >= m:
        return -2, -2  # controversal
    j2_flat = i2 * m + j2
    if j2_flat > 0:
        # from the 3d flattening formula, it is possible to find n
        # k2_flat = i2 * m * n + j2 * n + k2
        # k2_flat = (i2 * m + j2) * n + k2
        # n = k2_flat // (i2 * m + j2)
        if k2_flat < j2_flat:
            return -2, -2  # controversal
        n = k2_flat // j2_flat
        k2 = k2_flat % j2_flat
        if k2_flat != i2 * m * n + j2 * n + k2:
            return -2, -2  # controversal
        # k1_flat = i1 * m * n + j1 * n + k1
        # k1_flat // n = i1*m + j1
        j1 = k1_flat // n % m
        i1 = k1_flat // n // m
        return i1, j1
    i1 = 0 if k1_flat <= m else -1
    j1 = 0 if m == 1 else -1
    return i1, j1


i1, j1 = solve(k1_flat, m, k2_flat, i2, j2)
print(" ".join(map(str, [i1 + 1, j1 + 1])))
