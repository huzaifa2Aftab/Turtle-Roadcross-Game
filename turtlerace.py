import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
racers = []
x = -280
y = -100
color_list = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "pink"]

for _ in range(5):
    turtle = Turtle("turtle")
    turtle.color(color_list[_])
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(x, y)
    y += 50
    racers.append(turtle)

my_bet = screen.textinput("Do you wanna bet", "Choose Color")
if my_bet:
    run = True
    while run:

        for turtle in racers:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            x, y = turtle.pos()
            if turtle.xcor() > 280 or turtle.ycor() < -280:
                winner = turtle.pencolor()
                print(f"The winner is: {winner}")
                if winner == my_bet:
                    print("You won!")
                run = False

screen.exitonclick()
