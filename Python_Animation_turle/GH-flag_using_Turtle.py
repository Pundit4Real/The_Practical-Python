import turtle
from tkinter import *
from time import strftime

turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor('black')
turtle.speed(0.1)

colours = ['red','red','yellow', 'green','green']

for i in range(7):
    for color in colours:
        turtle.color(color)
        turtle.circle(70)
        turtle.backward(10)
        turtle.window_height()

# turtle.bgcolor("black")
# turtle.pensize(3)
# turtle.pencolor('black')
# turtle.speed(0.1)

picks = ['red','red','yellow', 'yellow','green','green']



for i in range(7):
    for pick in picks:
        turtle.color(pick)
        turtle.circle(100)
        turtle.right(13)
        
picks = ['red','red','yellow', 'yellow','green','green']



for i in range(7):
    for pick in picks:
        turtle.color(pick)
        turtle.circle(-100)
        turtle.left(13)
        turtle.position()

picks = ['red','red','yellow', 'yellow','green','green']