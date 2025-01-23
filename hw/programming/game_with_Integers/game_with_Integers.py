
ivan = "First"
bob = "Second"
winner = bob
for number in [int(input()) for _ in range(int(input()))]:
    if (number + 1) % 3 == 0 or (number - 1) % 3 == 0:
        winner = ivan
    else:
        winner = bob
    print(winner)
