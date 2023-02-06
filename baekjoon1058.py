import sys

n = int(sys.stdin.readline())
result = 0

a = list(sys.stdin.readline() for _ in range(n))

for i in range(n):
    b = [0 for _ in range(n)]
    for j in range(n):
        if a[i][j] == 'Y':
            b[j] = 'Y'
            for k in range(n):
                if a[j][k] == 'Y':
                    b[k] = 'Y'
    b[i] = 'N'
    result = max(result, b.count('Y'))

print(result)

n = int(sys.stdin.readline())
arr = [None] * n

for i in range(n):
    string = sys.stdin.readline()
    for j in range(j):
        if string[j] == 'Y':
            arr.append(j)

for i in range(n):
    a = set(arr[i])