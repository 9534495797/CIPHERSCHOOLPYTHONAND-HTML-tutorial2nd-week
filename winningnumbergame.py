winning_number=43
guess=1
number=int(input("guess between 1 to 100: "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"u win and guessed number in{guess} time")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
        else:
            print("too high")
        guess+=1
        number=int(input("guess again: "))