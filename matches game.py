matches = 23
print("You see " f" {matches} matches on the table.")
while matches > 0:
    move = 0
    while move < 1 or move > 3 or move > matches:
        move = int(input("How many matches you are taking (1–3)?"))
        if 1 > move or move > 3 or move > matches:
            print(
                "Wrong turn! You can take from 1 to 3,but not more than left."
            )
        else:
            matches -= move
            print(f"You took {move}," f" matches left: {matches}")
            if matches == 0:
                print("You died.")
                print('I mean, great game, lets try one more time')
                break

            move = (matches - 1) % 4
            if move == 0:
                move = 1
            matches -= move
            print(f"I take {move}, " f" matches left {matches}.")
            if matches == 0:
                print("You won")
                break