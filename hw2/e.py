# 1) Число метров, на которое он метнул лепешку, оканчивалось на 5
# 2) Один из победителей чемпионата метал лепешку до Василия
# 3) Участник, метавший лепешку сразу после Василия, метнул ее на меньшее количество метров
# Будем считать, что участник соревнования занял k-е место, если ровно (k − 1) участников чемпионата метнули лепешку строго дальше, чем он.
# Какое максимально высокое место мог занять Василий?


def place(scores):
    # find the best vasya's score in 1 loop
    i_winner = 0
    i_best = None
    for i in range(1, len(scores) - 1):
        score = scores[i]
        if score > scores[i_winner]:
            i_winner = i
            i_best = None # need to restart counting because previous one is invalid now
        elif score % 10 == 5 and scores[i + 1] < score:
            if i_best is None:
                i_best = i
            elif scores[i_best] < score:
                i_best = i
    # case when all requirements can't be met
    if i_best is None:
        return 0
    # find vasya's place in 1 loop
    best_place = 1
    best_score = scores[i_best]
    for score in scores:
        if score > best_score:
            best_place += 1
    return best_place


assert place([10, 20, 15, 10, 30, 5, 1]) == 6
assert place([15, 15, 10]) == 1
assert place([10, 15, 20]) == 0
assert place([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5


def main():
    _ = input()
    arr = tuple(map(int, input().split()))
    print(place(arr))


if __name__ == "__main__":
    main()
