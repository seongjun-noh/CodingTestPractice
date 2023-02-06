import sys
tempRank = -1
rank = -1
n, score, p = map(int, sys.stdin.readline().split())
if n > 0:
    scores = list(map(int, sys.stdin.readline().split()))
    scores.append(score)
    scores.sort(reverse=True)
    rank = scores.index(score) + 1
    if rank > p:
        print(-1)
    else:
        if n == p and score == scores[-1]:
            print(-1)
        else:
            print(rank)
else:
    print(1)

