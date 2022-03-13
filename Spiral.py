#imports the turtle libraray. Enables users to create pictures and shapes with a virtual canvas.
import turtle


turtle.bgcolor("black") #background color
turtle.pensize(2) #line thickness
turtle.speed(0) # sets speed, 0 = fastest, no animation

#nested for loops
#colours = an array of colors
for i in range(6):
    for colours in ["red", "Magenta", "blue", "cyan", "green", "yellow", "white" ] :
        turtle.color(colours)
        turtle.circle(150) #sets circle size
        turtle.left(10) #Creates next circle to the left

turtle.hideturtle() #Makes the turtle invisible