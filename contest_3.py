from itertools import product


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    numbers = [int(x) for x in input().split()]
    score = 0
    if k > 2:
        pairs = [[i, k-i] for i in range(1, k+1)]
        for pair in pairs:
            if pair[0] in numbers and pair[1] in numbers:
                score += 1
                numbers.remove(pair[0])
                numbers.remove(pair[1])
    else:
        score = 0
    print(score)