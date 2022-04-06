from turtle import Turtle, done

raven: Turtle = Turtle()


def draw_square(turtle: Turtle, x: float, y: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red", "pink")
    turtle.begin_fill()
    i: int = 0
    while i < 4:
        turtle.forward(300)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_triangle(turtle: Turtle, x: float, y: float) -> None:
    turtle.left(55)
    turtle.forward(250)
    turtle.right(108)
    turtle.forward(260)


draw_square(raven, -100, 50)
draw_triangle(raven, -100, 50)
done()