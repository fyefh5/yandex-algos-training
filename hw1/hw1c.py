numbers = set(list("1234567890"))

def standardize(phone):
    standard = ""
    for char in phone:
        if char not in numbers:
            continue
        standard = "".join([standard, char])
    if len(standard) == 7:
        standard = "".join(["+7495",standard])
    if phone[:2] == "+7":
        standard = "".join(["+",standard])
    if standard[0] == "8":
        standard = "".join(["+7",standard[1:]])
    return standard

new = standardize(input())
book = []
for _ in range(3):
    phone = standardize(input())
    if new == phone:
        print("YES")
    else:
        print("NO")
