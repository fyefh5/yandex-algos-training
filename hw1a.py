troom, tcond = list(map(int, input().split()))
mode = input()

match mode:
    case "freeze":
        if troom <= tcond:
            print(troom)
        else:
            print(tcond)
    case "heat":
        if troom >= tcond:
            print(troom)
        else:
            print(tcond)
    case "auto":
        print(tcond)
    case "fan":
        print(troom)
    case _:
        raise ValueError("Incorrect mode")
