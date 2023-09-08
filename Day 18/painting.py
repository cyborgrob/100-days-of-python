from turtle import Turtle, Screen, colormode
from random import choice
from colors import color_list

draw_baby = Turtle()
draw_baby.hideturtle()
colormode(255)
draw_baby.speed(0)
draw_baby.penup()
x = -400
y = -350
draw_baby.setpos(x, y)

# Draws 10 circles using a random color from the color_list for 10 rows to create a 10x10 painting. Can also use the
# 'turtle.dot()' method as well
for row in range(10):
    for circle in range(10):
        draw_baby.color(choice(color_list))
        draw_baby.begin_fill()
        draw_baby.circle(20)
        draw_baby.end_fill()
        draw_baby.forward(75)
    y += 70
    draw_baby.setpos(x, y)

screen = Screen()
screen.exitonclick()
