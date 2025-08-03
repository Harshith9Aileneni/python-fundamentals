import random

dice_roll = random.randint(1,6)



while True:
    try:
        guess = int(input("guess the number between(1-6)"))
        if guess == dice_roll:
            print(f"you have guess is correct {dice_roll}")
            break
        else:
            print(f"wrong your answer is {guess}")
    except ValueError:
        print("try again with correct value")









