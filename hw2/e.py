# 1) Число метров, на которое он метнул лепешку, оканчивалось на 5
# 2) Один из победителей чемпионата метал лепешку до Василия
# 3) Участник, метавший лепешку сразу после Василия, метнул ее на меньшее количество метров
# Будем считать, что участник соревнования занял k-е место, если ровно (k − 1) участников чемпионата метнули лепешку строго дальше, чем он.
# Какое максимально высокое место мог занять Василий?


def place(arr):
    # find the most left winner position
    i_winner = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i_winner]:
            i_winner = i
    # find all possible positions of vasya in the tournament order
    i_vasya = []
    for i in range(len(arr)-1):
        if i_winner < i and arr[i] % 10 == 5 and arr[i] > arr[i+1]:
            i_vasya.append(i)
    if len(i_vasya) == 0:
        return 0
    # find max_score_vasya
    max_score_vasya = arr[i_vasya[0]]
    for i in i_vasya:
        if arr[i] > max_score_vasya:
            max_score_vasya = arr[i]
    # find vasya's place in the leadership board
    max_place_vasya = 1
    for score in arr:
        if score > max_score_vasya:
            max_place_vasya += 1
    return max_place_vasya


assert place([10, 20, 15, 10, 30, 5, 1]) == 6
assert place([15, 15, 10]) == 1
assert place([10, 15, 20]) == 0


def main():
    _ = input()
    arr = tuple(map(int, input().split()))
    print(place(arr))


if __name__ == "__main__":
    main()
