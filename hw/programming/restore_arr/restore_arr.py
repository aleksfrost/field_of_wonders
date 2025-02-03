for _ in range(int(input())):
    k = int(input())
    arr = [int(num) for num in input().split()]
    for i in (range(k)):
        if arr[i] == arr[i+1]:
            continue

    print(arr)