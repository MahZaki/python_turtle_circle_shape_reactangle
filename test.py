import turtle
def draw_square(some_turtle,angle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(angle)

	
	
def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("yellow")
	brad.fillcolor("red")
	brad.speed(1000)
	for i in range(1,1000):
		draw_square(brad,90)
		brad.right(5)
		draw_square(brad,90)
	
	window.exitonclick()
	
draw_art()