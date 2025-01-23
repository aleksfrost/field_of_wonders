
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    cows = []
    cows_1 = []
    for i in range(n):
        res = []
        cows.append(list(range(i, n*m, n)))
        cows_1.append(sorted([int(x) for x in input().split()], key=int))
    if sorted(cows) == sorted(cows_1):
        for i in range(n):
            count = 0
            for cow in cows_1:
                count += 1
                if cow[0] == i:
                    res.append(count)
        print(*res, sep=" ")
    else:
        print(-1)
