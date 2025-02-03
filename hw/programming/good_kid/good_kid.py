import math
for _ in range(int(input())):
    input()
    arr = sorted([int(x) for x in input().split()])
    arr.append(arr.pop(0) + 1)
    print(math.prod(arr))
#BruteForce   (140 mc)
"""res = []
a = int(input())
for _ in range(a):
    _ = input()
    product_arr = []
    arr = [int(x) for x in input().split()]
    for i in range(len(arr)):
        arr1 = arr[:]
        arr1[i] = arr1[i] + 1
        product_arr.append(math.prod(arr1))
    res.append(max(product_arr))

print(*res, sep="\n")


"""

#Algorithm "add +1 to minimum"   (108 mc)
for _ in range(int(input())):
    input()
    arr = sorted([int(x) for x in input().split()])
    arr.append(arr.pop(0) + 1)
    print(math.prod(arr))


#Output
"""
16
2
432
430467210
"""

