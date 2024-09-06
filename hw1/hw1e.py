apt_test, n_floors, apt, entry, floor = list(map(int, input().split()))


def solve(apt_test, n_floors, apt, entry, floor) -> tuple:
    """
    returns (i1, j1) \n
    if controversal, then (-2, -2) \n
    if amiguous i1, then (-1, j1) \n
    if ambiguous j1, then (i1, -1) \n
    """
    # k_flat = i * n_floors * n_perfloor + j * n_perfloor + k
    k_flat_test = apt_test - 1  # index of apartment for event 1
    k_flat = apt - 1  # index of apartment for event 2
    i = entry - 1  # index of entry for event 2
    j = floor - 1  # index of floor for event 2
    # print(f"i: {i}")
    # print(f"j: {j}")
    # print(f"k_flat: {k_flat}")
    # print(f"k_flat_test: {k_flat_test}")

    # wrong case
    if floor > n_floors:
        return -1, -1
    # easy case
    if n_floors == 1 and apt_test <= n_floors:
        return 1, 1
    cum_floor = i * n_floors + floor
    # wrong case
    if apt < cum_floor:
        return -1, -1
    # ambiguous n_perfloor
    if cum_floor == 1:
        if apt_test > apt:
            return 0, 1
        return 1, 1

    # general case
    n_perfloor_min = (apt - 1) // cum_floor + 1
    max_last_floor_population = n_perfloor_min
    if apt % n_perfloor_min > 0:
        max_last_floor_population = apt % n_perfloor_min
    delta = 0
    if max_last_floor_population > (cum_floor - 1):
        delta = max_last_floor_population // (cum_floor - 1)
        if max_last_floor_population % (cum_floor - 1) == 0:
            delta -= 1
    n_perfloor_max = n_perfloor_min + delta
    if n_perfloor_min == n_perfloor_max:
        # no ambiguity
        n_perfloor = n_perfloor_max
        entry_test = k_flat_test // n_perfloor // n_floors + 1
        floor_test = k_flat_test // n_perfloor % n_floors + 1
        return entry_test, floor_test
    # ambiguous case
    entry_test = k_flat_test // n_perfloor_min // n_floors + 1
    floor_test = k_flat_test // n_perfloor_min % n_floors + 1
    for n_perfloor in range(n_perfloor_min+1, n_perfloor_max+1):
        if k_flat_test // n_perfloor // n_floors + 1 != entry_test:
            entry_test = 0
        if k_flat_test // n_perfloor % n_floors + 1 != floor_test:
            floor_test = 0
    return entry_test, floor_test


ans = solve(apt_test, n_floors, apt, entry, floor)
print(" ".join(map(str, ans)))
