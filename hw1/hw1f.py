a1, a2, b1, b2 = list(map(int, input().split()))

areas = [0]*4
# hstack
areas[0] = max(a1, b1) * (a2 + b2)
areas[1] = max(a1, b2) * (a2 + b1)
# vstack
areas[2] = (a1 + b1) * max(a2, b2)
areas[3] = (a1 + b2) * max(a2, b1)

minarea = areas[0]
iminarea = 0
for i, area in enumerate(areas):
    if area < minarea:
        minarea = area
        iminarea = i

match iminarea:
    case 0:
        print(f"{max(a1, b1)} {a2 + b2}")
    case 1:
        print(f"{max(a1, b2)} {a2 + b1}")
    case 2:
        print(f"{max(a2, b2)} {a1 + b1}")
    case 3:
        print(f"{max(a2, b1)} {a1 + b2}")