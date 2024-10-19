# The game is about drawing a number from a range provided by the user.
# After each attempt to guess the number, the user receives a message
# whether the number drawn is higher, lower, or outside the range.
# At the end, the user receives information about quantity of attempts
# and duration of the game.
import random
import time


def guessing(range_min, range_max):
    """Chooses random number within range and the game is played until the number is guessed."""
    if range_min > range_max:
        range_min, range_max = range_max, range_min
    x = random.randint(range_min, range_max)
    count = 1
    while True:
        shot_str = input(f"Guess number between {range_min} and {range_max}: ")
        try:
            shot = int(shot_str)
        except Exception:
            print("\nInvalid number. Insert again: ")
            continue
        if shot == x:
            print(f"\nGood job! The number is: {x}")
            print(f"Number of attempts: {count}")
            break
        elif x < shot <= range_max:
            print("\nThe drawn number is smaller. Try again.")
            count += 1
        elif range_min <= shot < x:
            print("\nThe drawn number is bigger. Try again.")
            count += 1
        else:
            print("\nNumber out of range. Try again.")
            count += 1


def inserting_limit(which):
    """Takes limit from user, validates and changes to int. Returns int value."""
    limit_str = input(f"\nInsert {which} limit of range: ")
    while True:
        try:
            limit = int(limit_str)
        except Exception:
            limit_str = input("\nInvalid number. Insert again: ")
        else:
            return limit


def instructions():
    """Shows instructions of the game"""
    print("""
    Instructions:
    1. Press 'y' if you want to play a game.
    2. Insert the first limit of the range - integer number.
    3. Insert the second limit of the range - integer number.
    4. Try to guess the drawn number within the range.
    Good luck!
    """)


def game():
    print("\n~~~~Welcome to the game GUESS NUMBER!~~~~")
    print("For instructions, press 'i'.")
    while True:
        is_ready = input("Are you ready to play? (Y/N): ")
        if is_ready == "y":
            start = time.time()
            guessing(inserting_limit('the first'), inserting_limit('the second'))
            end = time.time()
            print(f"Your game lasted for {int(end - start) // 60} min {int(end - start) % 60} sec.")
            played = True
            break
        elif is_ready == "n":
            played = False
            print("Maybe next time. Goodbye!")
            break
        elif is_ready == 'i':
            instructions()
        else:
            print("\nWrong key. Press 'y' for 'Yes' and 'n' for 'No' or 'i' for instructions.")
    return played


while True:
    played = game()
    if played:
        play_again = input("\nPlay again? (Y/N): ")
        if play_again == "y":
            continue
        elif play_again == "n":
            break
        else:
            print("\nWrong key. Press 'y' for 'Yes' and 'n' for 'No'.")
    else:
        break
