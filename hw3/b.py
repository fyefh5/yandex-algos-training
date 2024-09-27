s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s = set.intersection(s1,s2)
print(" ".join(map(str, sorted(s))))