income = [[int(x) for x in input().split()] for _ in range(int(input()))]
for data in income:
    print(data[0]*(data[1]//2))
