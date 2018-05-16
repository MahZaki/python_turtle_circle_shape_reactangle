from turtle import *

speed(0)	
bgcolor("Black")
color("White")
pensize(5)

def hex(side):
	for count in range(2):
		forward(side)
		left(120)

def rotation():

    n = 0
    colormode(255)
    c = 0
    pencolor(c,c,c)

    for count in range(500):
        if c != 255:
            c += 255.0/120
        pencolor(c,c,c)
        hex(n)
        n += 4
        left(2)

penup()
goto(0,0)
pendown()

rotation()

hideturtle()
done()
