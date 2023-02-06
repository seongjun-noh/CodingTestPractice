import sys

arr = [i + 1 for i in range(30)]
for i in range(28):
    arr.pop(arr.index(int(sys.stdin.readline())))
arr.sort()
for i in range(2):
    print(arr[i])