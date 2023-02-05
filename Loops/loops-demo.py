import random

number = random.randint(1, 10)
trying = 5
count = 0

while trying > 0:
    count += 1
    trying -= 1
    choice = int(input("Your guess: "))
    if(choice == number):
        print(f"Congrats! You guessed correctly at {count}")
        break
    elif number > choice:
        print("You should guess higher")
    else:
        print("You should guess lower")
    if trying == 0:
        print("You have no more choice!")