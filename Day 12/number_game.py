import random
num = random.choice(range(1, 101))

def checker(guess):
  global lives
  if guess > num:
    print("Your guess is too high.")
    lives -= 1
    print(f"You have {lives} lives left.")
  elif guess < num:
    print("Your guess is too low.")
    lives -= 1
    print(f"You have {lives} lives left.")
  elif guess == num:
    print("You got it right! Congratulations.")

mode = input("Welcome to the number guessing game. Hard/easy mode?: ").lower()
if mode == "hard":
  lives = 5
else:
  lives = 10

while lives > 0:
  user_guess = int(input("Guess a number: "))
  checker(guess=user_guess)
  if user_guess == num:
    break

if lives == 0:
  print("The number was {}.".format(num))
  print("You ran out of lives. You lose.")