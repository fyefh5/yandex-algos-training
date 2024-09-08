def add_mine(field, n, m, i_mine, j_mine):
    field[i_mine][j_mine] = "*"
    i1 = i_mine if i_mine == 0 else i_mine - 1
    j1 = j_mine if j_mine == 0 else j_mine - 1
    i2 = i_mine if i_mine == n - 1 else i_mine + 1
    j2 = j_mine if j_mine == m - 1 else j_mine + 1
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if field[i][j] != "*":
                field[i][j] += 1
    return field


def field2string(field):
    return "\n".join(map(lambda x: " ".join(map(str, x)), field))


def saper(n, m, mines):
    field = [[0] * m for _ in range(n)]
    for i_mine, j_mine in mines:
        field = add_mine(field, n, m, i_mine, j_mine)
    return field


def main():
    n, m, k = list(map(int, input().split()))
    mines = []
    for _ in range(k):
        mine = list(map(int, input().split()))
        mine[0] -= 1
        mine[1] -= 1
        mines.append(mine)
    field = saper(n, m, mines)
    print(field2string(field))


if __name__ == "__main__":
    main()
