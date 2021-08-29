import random

print("Welcome to rolling the dice")


def main():
    dice = random.randint(1, 6)

    print("The number on the dice is", dice)
    restart()


def restart():
    replay = str(input("Do you want to roll the dice again? (y/n): "))
    if replay == "y":
        main()
    elif replay == "n":
        print("Goodbye!")
        quit()
    else:
        print("Please enter a correct input!")
        restart()


while True:
    main()
