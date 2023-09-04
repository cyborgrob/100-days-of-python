#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? $"))
total_people = int(input("How many people to split between? "))
tip = float(input("What percentage tip do you want to leave? "))
tip_modifier = 1 + (tip/100)
total_w_tip = "{:.2f}".format((total_bill / total_people) * tip_modifier)

print(f"Each person should pay ${total_w_tip}")
