import sys

n, m = map(int, sys.stdin.readline().split())
minSix, minOne = 1000, 1000

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    minSix = min(minSix, a)
    minOne = min(minOne, b)

result = min(minSix * (n // 6) + min(minSix, (n % 6) * minOne), n * minOne)
print(result)