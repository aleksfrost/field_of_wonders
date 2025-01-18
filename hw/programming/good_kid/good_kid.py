import math

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
res = []
a = int(input())
for _ in range(a):
    _ = input()
    product_arr = []
    arr = sorted([int(x) for x in input().split()])
    arr.append(arr.pop(0) + 1)
    res.append(math.prod(arr))
print(*res, sep="\n")


#Output
"""
16
2
432
430467210
"""

