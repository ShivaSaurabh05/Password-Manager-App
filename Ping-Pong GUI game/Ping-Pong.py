# --------------------------------- Shiva Saurabh --------------------------------- #
from turtle import Turtle
from turtle import Screen
import time

# --------------------------------- Screen Setup ---------------------------------- #

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


# ---------------------------------- Ball Class ---------------------------------- #

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()


# --------------------------------- Paddle Class ------------------------------------ #
class Paddle(Turtle):

    def __init__(self, poistion):
        super().__init__()
        self.shape("square", )
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(poistion)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# ---------------------------------- Score Counter --------------------------------------- #
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


# ----------------------------------- Paddle Movement ----------------------------------- #
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# --------------------------------------- collision detection ------------------------------------------------ #
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # ----------------------------- collision detection with wall ---------------------------- #
    if ball.ycor() > 280 or ball.ycor() < -200:
        ball.bounce_y()
    # ----------------------------- collision detection with paddles ---------------------------- #
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # ----------------------------- detect R paddle misses ---------------------------- #
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # ----------------------------- detect L paddle misses ---------------------------- #
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
