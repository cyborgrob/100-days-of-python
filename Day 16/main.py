from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("CadetBlue")
# timmy.forward(100)
# print(my_screen)
# my_screen.exitonclick()
#
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "l"
print(table)
