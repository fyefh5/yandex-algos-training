with open("hw3/input_h.txt", "r") as f:
    n = int(f.readline())
    birds = set()

    for _ in range(n):
        x, y = tuple(map(int, f.readline().split()))
        birds.add(x)

    print(len(birds))



# надо проверить есть ли птица с таким же x, что у новой
# если есть, то заменить на птицу повыше