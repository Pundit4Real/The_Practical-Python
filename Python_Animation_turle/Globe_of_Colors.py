import turtle

turtle.bgcolor('black')
turtle.speed(0.02)
turtle.pensize(3)
turtle.backward(11)


colours = ['white','white', 'red','red','blue','blue','yellow','yellow','purple','purple','magenta','magenta','aqua','aqua']

for i in range(15):
    for color in colours:
        turtle.color(color)
        turtle.circle(140)
        turtle.right(10)

turtle.mainloop()