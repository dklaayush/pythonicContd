import turtle

# Setup screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Simple Turtle Star")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw spiral
for x in range(180):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

# Keep open until you click the window
win.exitonclick()