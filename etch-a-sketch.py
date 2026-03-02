from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    #tim.tilt(15)
    tim.left(15)

def turn_right():
    #tim.tilt(-15)
    tim.right(15)

def clearscreen():
    tim.clear()
    tim.teleport(0,0)



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clearscreen)


screen.exitonclick()