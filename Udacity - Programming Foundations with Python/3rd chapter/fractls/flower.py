import turtle

def draw_triangle(some_turtle):
    some_turtle.forward(100)
    some_turtle.left(60)
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(100)
    some_turtle.left(60)
    some_turtle.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(5)
    for i in range (0,36):
        draw_triangle(brad)
        brad.right(10)

    brad.color("yellow")
    brad.right(90)
    brad.forward(300)



    window.exitonclick()

draw_art()
