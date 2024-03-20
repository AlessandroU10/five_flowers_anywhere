from turtle import *
import random

hideturtle()
color('black', 'green')

def left_turn():
    for i in range(35):
        forward(4)
        left(3)

def make_petal():
    begin_fill()
    left_turn()
    left(75)
    left_turn()
    left(75)
    end_fill()

def flower():
    for _ in range(5):  # Avoid reusing 'i' variable
        penup()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        goto(x, y)
        pendown()
        for _ in range(5):  # Draw 5 petals per flower
            make_petal()
            right(72)  # Adjust for 5 petals; 360/5 = 72
        setheading(0)  # Reset the turtle's heading

    exitonclick()

flower()
