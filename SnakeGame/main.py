from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segment_1 = Turtle(shape="square")
segment_1.color("pink")

segment_2 = Turtle(shape="square")
segment_2.color("pink")


segment_3 = Turtle(shape="square")
segment_3.color("white")


screen.exitonclick()