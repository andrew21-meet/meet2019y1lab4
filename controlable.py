import turtle

turtle.bgcolor("grey")
turtle.shape("arrow")
turtle.left(120)
turtle.pensize(5)
turtle.pencolor("darkgreen")
def up() :
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x, y+50)
turtle.onkeypress(up, "w")
turtle.listen()

def down() :
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x, y-50)
turtle.onkeypress(down, "s")
turtle.listen()

def left() :
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x-50, y)
turtle.onkeypress(left, "a")
turtle.listen()

def right() :
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x+50, y)
turtle.onkeypress(right, "d")
turtle.listen()

def penup():
    turtle.penup()
turtle.onkeypress(penup, "k")
turtle.listen()

def pendown():
    turtle.pendown()
turtle.onkeypress(pendown, "l")

def eraser():
    turtle.pencolor("grey")
turtle.onkeypress(eraser, "j")

def reblack():
    turtle.pencolor("blue")
turtle.onkeypress(reblack, "i")

def color2():
    turtle.pencolor("yellow")
turtle.onkeypress(color2, "u")

def stamp():
    turtle.stamp()
turtle.onkeypress(stamp, "o")


turtle.mainloop()





