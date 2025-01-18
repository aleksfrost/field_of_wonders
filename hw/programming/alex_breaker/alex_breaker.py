_ = input()
arr = [int(x) for x in input().split()]


if len(set(arr)) == 1 and sum(arr) == 0:
    print("NO")
elif sum(arr) != 0:
    print("YES")
    print(1)
    print(f"{1} {len(arr)}")
else:
    for i in range(len(arr) - 1):
        if sum(arr[: i + 1]) != 0 and sum(arr[i + 1: ]) != 0:
            print("YES")
            print(2)
            print(f"{1} {i + 1}")
            print(f"{i+2} {len(arr)}")
            break
