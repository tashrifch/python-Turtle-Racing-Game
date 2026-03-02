from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=900, height = 700)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []



for turtle_index in range(0,6):
    turtle= Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x= -250,y=-100+(turtle_index*50))
    all_turtles.append(turtle)


if user_bet:
     is_race_on = True

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor()> 250:
            winning_color = turtle.pencolor() +"has won"
            is_race_on = False
            if winning_color == user_bet.lower():
                print("You won the bet")
                turtle.write("You win")
            else:
                print("you lost the bet")
                turtle.write("Game Over You lost")
        


screen.exitonclick()