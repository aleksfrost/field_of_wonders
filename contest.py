res = []
for _ in range(int(input())):
    fibb = 0
    arr = [int(x) for x in input().split()]
    if arr[1] == arr[2]:
        arr.insert(2, 0)
    else:
        arr.insert(2, arr[2] - arr[1])
    for i in range(0,3):
        if sum(arr[i:i+2]) == arr[i+2]:
            fibb += 1
    res.append(fibb)

print(*res, sep="\n")
