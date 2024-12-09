import turtle

sides_answer = int(input('Number of sides? --> ')) # Prompt user question

t = turtle.Turtle() # Init Turtle
t.screen.title('Drawing your shape..')

t.color('red') # Colour of line drawn

def shape(num_of_sides): # Calculation for deciding shape 
    total = 360
    shape_angle = (total / num_of_sides)
    for _ in range(num_of_sides):
        t.speed(1)
        t.forward(30)
        t.left(shape_angle)

shape(sides_answer)

turtle.done() # Keeps screen running
