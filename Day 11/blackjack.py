############### Blackjack Project #####################
import random
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this down of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
for card in range(2):
  user_cards.append(deal_card())
computer_cards.append(deal_card())
print(user_cards)
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  print(cards)
  score = sum(cards)  
  if len(cards)  == 2 and score == 21:
    return 0
  elif score > 21 and 11 in cards:
    print("alert")
    cards.remove(11)
    cards.append(1)
    print(cards)
    return(score)
  else:
    return score

print(calculate_score(user_cards))
user_cards.append(deal_card())
print(calculate_score(user_cards))
user_cards.append(deal_card())
print(calculate_score(user_cards))
user_cards.append(deal_card())


from art import logo
from replit import clear
import random

run = True

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_again():
  play_again = input("Would you like to play again? y/n: ").lower()
  if play_again == "y":
    clear()
    blackjack()
  else:
    global run
    run = False
    

def blackjack():  
  while run:
    user_hand = []
    cpu_hand = []  
    for card in range(2):
      user_hand.append(random.choice(cards))  
    cpu_hand.append(random.choice(cards))  
    user_score = sum(user_hand)
    cpu_score = sum(cpu_hand)
    print(f"Your cards: {user_hand}, your current score: {user_score}")
    print(f"Computer's first card: {cpu_hand}")
    
    if user_score == 21:
      print("Blackjack! You win.")
      continue
      
    while user_score < 21 and run:
      draw = input("Would you like to draw another card? y/n: ").lower()
      if draw == "y":
        user_hand.append(random.choice(cards))
        user_score = sum(user_hand)
        print(f"Your cards: {user_hand}, your current score: {user_score}")
        if user_score > 21:
          print("You went over 21. You bust. You're trash.")
          play_again()          
        elif user_score == 21:
          print("You're at 21. You stand.")
          while cpu_score <= 21:
            print("Computer draws:")
            cpu_hand.append(random.choice(cards))
            cpu_score = sum(cpu_hand)
            print(f"Computer's cards: {cpu_hand}, computer score: {cpu_score}")
            if cpu_score > 21:
              print("Computer busts. You win.")
              play_again()              
            elif cpu_score == 21:
              print("Computer has 21 also. It's a push.")
              play_again()
              
      else:
        print("You stand.")
        while cpu_score < user_score:        
          cpu_hand.append(random.choice(cards))
          cpu_score = sum(cpu_hand)
          print(f"Computer draws. Computer's cards: {cpu_hand}, computer score: {cpu_score}")
          if cpu_score > 21:
            print("Computer busts. You win.")
            play_again()            
          elif cpu_score == user_score:
            print(f"Computer has {user_score} also. It's a push.")
            play_again()            
          elif cpu_score > user_score:
            print(f"Computer has {cpu_score}. You lose.")
            play_again()
            
      
while run:
  blackjack()
    
print("Goodbye.")     
    
