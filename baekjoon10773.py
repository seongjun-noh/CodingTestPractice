import sys

k = int(sys.stdin.readline())
scores = []
for i in range(k):
    score = int(sys.stdin.readline())
    if score == 0:
        scores.pop()
    else:
        scores.append(score)
print(sum(scores))