import random
import sys

# global variable
high_score = 0


def dice_game():
    global high_score  # modify global variable
    print("Current High Score: ", high_score)
    print("Your choices are: \n 1) Roll Dice \n 2) Leave Game")
    while True:
        user_input = input("Enter your choice: ")
    # pair of dice being "thrown"
    # can use type method in python
        if user_input == "1":  # figure out how to parse to an int instead of a string
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            print("You roll a ", a)
            print("You roll a ", b)
            total_score = a + b
            print('You have rolled a total of ', total_score)
            if total_score > high_score:
                high_score = total_score
                print("New High Score!")
            else:
                continue
        else:
            print("Goodbye!")
            sys.exit()


dice_game()

# questions:
# global variaable scope for example high score
# doing a for loop for the double random rolls
