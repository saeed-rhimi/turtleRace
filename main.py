from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet!", prompt="which turtle will win the race? enter the color: ")
print(user_bet)
colors = ["red", "green", "blue", "cyan", "black", "pink"]
y_position = [15, 45, 75, -15, -45, -75]
all_turtles = []
game_over = False

for n in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.setposition(x=-230, y=y_position[n])
    all_turtles.append(new_turtle)

while game_over == False:
    for item in all_turtles:
        item.forward(random.randint(0, 10))
        if item.xcor() > 230 and game_over == False:
            game_over = True
            winner = item.pencolor()
            if user_bet == winner:
                print("You Win")
            else:
                print("You Lost!")

screen.exitonclick()
