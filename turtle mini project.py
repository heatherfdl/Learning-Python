# drawing with package turtle (built into python)

# import turtle package
import turtle

# set up in turtle
turtle.bgcolor("black") #sets background color
turtle.pensize(2) # sets pen size
turtle.color("brown") # sets color
turtle.speed(0) # sets speed to do commands instantaneously (0 seconds)

# draw a square
# turtle.forward(50) # moves forward that amount according to what you have set above
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done() #allows turtle to stay on screen
## press CMND and / to hashtage everything in a selection

# creating a different drawing
# for colours in ("red", "orange", "yellow", "green", "blue", "purple"):
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# lets make it cooler
for i in range(12):
    for colours in ("red", "orange", "yellow", "green", "blue", "purple"):
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()

