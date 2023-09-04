from game_data import data
import random
from art import logo, vs
import os


def initializer():
    """This selects two random instagram accounts to start the game with"""
    selection1 = random.randint(0, len(data) - 1)
    selection2 = random.randint(0, len(data) - 1)
    # If the two random choices happen to be the same, it chooses again until they are not.
    while selection1 == selection2:
        selection2 = random.randint(0, len(data) - 1)
    return selection1, selection2


def new_random_choice():
    """This chooses a new random selection to go against the previous round's winner"""
    new_choice = random.randint(0, len(data) - 1)
    return new_choice


def compare_function():
    """This compares random1 & random2 and returns whichever has a greater follower count"""
    if data[random1].get('follower_count') > data[random2].get('follower_count'):
        return "A"
    else:
        return "B"


# initializer() returns two random, distinct selections and sets them as the variables random1 & random2.
random1, random2 = initializer()

# creates the variable to keep score
score = 0
run = True

while run:
    # Asking the user which person they think has more followers.
    print(logo)
    print(f"Your current score is {score}")
    print('Compare A:', data[random1].get('name') + ',', data[random1].get('description') + ', from',
          data[random1].get('country'))
    print(vs)
    print('Against B:', data[random2].get('name') + ',', data[random2].get('description') + ', from',
          data[random2].get('country'))
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # checks the user's choice against the result of the compare_function. if they're right, they score a point. if
    # not, they lose.
    if choice == compare_function():
        score += 1
        # If B is the answer, it switches the 'B' choice to the 'A' slot for the next round.
        if choice == "B":
            random1 = random2
        # Selects a new choice for the 'B'/random2 slot.
        random2 = new_random_choice()
        # This while loop prevents the two choices from being the same, just like in the initializer function.
        while random1 == random2:
            random2 = new_random_choice()
        # This clears the console for the next round.
        os.system('cls')
    else:
        # If the user's choice doesn't match the compare function, they lose and the game is over.
        print(f"Sorry, that's wrong. Final score: {score}")
        run = False

# this is a test line of code.
