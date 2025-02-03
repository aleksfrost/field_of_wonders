def game(arr: list, turn = 0):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return (((arr.pop(0) + arr.pop(0)) // 2) * 2)
    else:
        is_worked = 0
        if turn == 0:
            for i in range(len(arr)):
                if arr[i] % 2 == 1:
                    for k in range(i + 1, len(arr)):
                        if arr[k] % 2 == 1:
                            arr.append(arr[i] + arr[k])
                            arr.pop(k)
                            arr.pop(i)
                            turn = 1
                            is_worked = 1
                            return(game(arr, turn))
            if not is_worked:
                for i in range(len(arr)):
                    if arr[i] % 2 == 0:
                        for k in range(i + 1, len(arr)):
                            if arr[k] % 2 == 0:
                                arr.append(arr[i] + arr[k])
                                arr.pop(k)
                                arr.pop(i)
                                turn = 1
                                is_worked = 1
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
            return(game(arr, turn))


for _ in range(int(input())):
    len_arr = int(input())
    arr = [int(num) for num in input().split()]
    result = [arr[0]]
    for ind in range(1, len_arr):
        result.append(game(arr[:ind+1]))
    print(*result, sep=" ")

