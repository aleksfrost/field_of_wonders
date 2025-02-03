def game(arr: list, turn = 0):
    print(arr)
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return (((arr.pop(0) + arr.pop(0)) // 2) * 2)
    else:
        is_worked = 0
        if turn == 0:
            first = arr.pop(0)
            if first % 2 == 1:
                for _ in range(len(arr)):
                    second = arr.pop(0)
                    if second % 2 == 1:
                        arr.append(first + second)
                        is_worked = 1
                        break
                    else:
                        arr.append(second)
            elif first % 2 == 0:
                for _ in range(len(arr)):
                    second = arr.pop(0)
                    if second % 2 == 0:
                        arr.append(first + second)
                        is_worked = 1
                        break
                    else:
                        arr.append(second)
            if not is_worked:
                arr.append(first)
                arr.append(arr.pop(0) + arr.pop(0))
            turn = 1
            print(f"arr{arr}")
            return(game(arr, turn))
        else:
            first = arr.pop(0)
            if first % 2 == 1:
                for _ in range(len(arr)):
                    second = arr.pop(0)
                    if second % 2 == 0:
                        arr.append(((first + second) // 2) * 2)
                        is_worked = 1
                        break
                    else:
                        arr.append(second)
            elif first % 2 == 0:
                for _ in range(len(arr)):
                    second = arr.pop(0)
                    if second % 2 == 1:
                        arr.append(((first + second) // 2) * 2)
                        is_worked = 1
                        break
                    else:
                        arr.append(second)
            if not is_worked:
                arr.append(first)
                arr.append(arr.pop(0) + arr.pop(0))
            turn = 0
            print(f"arr{arr}")
            return(game(arr, turn))

res = []

for _ in range(int(input())):
    len_arr = int(input())
    arr = [int(num) for num in input().split()]
    result = [arr[0]]
    for ind in range(1, len_arr):
        print("SLICE")
        result.append(game(arr[:ind+1]))
    res.append(result)

print(*res, sep="\n")

