rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = input("What do you throw? Choose 0 for Rock, 1 for Paper, or 2 for Scissors: ")

if float(player_choice) > 2 or float(player_choice) < 0:
  print("You picked an invalid number, dumbass. You lose!")

comp_choice = random.randint(0, 2)

if player_choice == "0":
  print(rock)
  if comp_choice == 0:
    print(rock)
    print("The computer also threw Rock. Draw!")
  elif comp_choice == 1:
    print(paper)
    print("The computer threw Paper. You lose!")
  else:
    print(scissors)
    print("The computer threw Scissors. You win!")

if player_choice == "1":
  print(paper)
  if comp_choice == 0:
    print(rock)
    print("The computer threw Rock. You win!")
  elif comp_choice == 1:
    print(paper)
    print("The computer also threw Paper. Draw!")
  else:
    print(scissors)
    print("The computer threw Scissors. You lose!")

if player_choice == "2":
  print(scissors)
  if comp_choice == 0:
    print(rock)
    print("The computer threw Rock. You lose!")
  elif comp_choice == 1:
    print(paper)
    print("The computer threw Paper. You win!")
  else:
    print(scissors)
    print("The computer also threw Scissors. Draw!")
