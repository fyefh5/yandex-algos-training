g1 = input().strip()
g2 = input().strip()

pairs = set()
for i in range(len(g2)-1):
    pairs.add(g2[i:i+2])

cnt = 0

for i in range(len(g1)-1):
    pair = g1[i:i+2]
    if pair in pairs:
        cnt += 1

print(cnt)