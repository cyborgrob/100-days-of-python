from replit import clear
from art import logo
print(logo + "\nWelcome to the Blind Auction.")
#HINT: You can call clear() to clear the output in the console.

bids = {}
run = True

while run:
  name = input("What is your name?: ")
  bid = input("What is your bid?: ")
  
  bids[name] = int(bid)
  
  again = input("Are there any other users who would like to bid? yes/no: ").lower()
  if again == "yes":
    clear() 
  else:
    run = False

highest_bid = 0
winner = ""
for bidder in bids:
  if bids[bidder] > highest_bid:
    highest_bid = bids[bidder]
    winner = bidder

print(f"The winner of the auction is {winner} with a bid of ${highest_bid}.")