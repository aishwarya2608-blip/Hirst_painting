import turtle as t
import random 

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,  255)
    g = random.randint(0,  255)
    b = random.randint(0,  255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.color(random_color())
    tim.dot(20)
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

