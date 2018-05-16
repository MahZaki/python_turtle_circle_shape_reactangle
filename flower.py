import turtle
def draw_f(turtle):
	for i in range(4):
		turtle.forward(100)
		turtle.left(45)
		turtle.forward(100)
		turtle.left(135)
def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	
	brad = turtle.Turtle()
	brad.speed(100)
	brad.color("black")
	brad.pensize(5)
	for i in range(36):
		draw_f(brad)
		brad.left(10)
		
	window.exitonclick()
	
draw_art()