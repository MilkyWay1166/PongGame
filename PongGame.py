from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.title=("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

border = Turtle()
border.penup()
border.goto(0,300)
border.pendown()
border.color('white')
border.pensize(5)
border.hideturtle()
border.setheading(270)

for i in range(30):
    border.forward(10)
    border.penup()
    border.forward(10)
    border.pendown()
    

LEFT_OR_RIGHT = {"left" :-360,
                 "right": 360}

START_POSITION = 0

class Paddle(Turtle):
    
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color("white")
        self.goto(LEFT_OR_RIGHT[side], START_POSITION)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def stop_moving(self):
        if self.ycor() > 250:
            self.goto(self.xcor(), 250)
        if self.ycor() <  -250:
            self.goto(self.xcor(), -250)
    


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.pensize(5)
        self.color('white')
        self.setheading(random.choice([random.randint(-70, 70), random.randint(110, 250)]))
        self.move_speed = 1
    def move(self):
        self.forward(10)
    
    def bounce(self, paddle_left, paddle_right):
        if self.ycor() > 280 or self.ycor() < - 280:
            direction = self.heading()
            self.setheading(360 - direction)
            self.move_speed *= 0.9
        if (self.xcor() <-340 and self.xcor() >-345) or (self.xcor() > 340 and self.xcor() < 345):
            if self.distance(paddle_left) < 53.81 or self.distance(paddle_right) < 53.81:

                direction = self.heading()
                self.setheading(180 - direction)
                self.move_speed *= 0.9
    
    def refresh(self):
        if self.xcor() > 380 or self.xcor() < - 380:
            self.goto(0, 0)
            self.setheading(random.choice([random.randint(-70, 70), random.randint(110, 250)]))
            self.move_speed = 1


class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.side = side
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(LEFT_OR_RIGHT[self.side]/2, 200)
        self.write(f"{self.score}", font=["Courier", 60, "normal"])
    
    def update_score(self, ball_check):
        if self.side == "left" and ball_check.xcor() > 375:
            self.score +=1

        if self.side == "right" and ball_check.xcor() < -375:
            self.score +=1
        
        self.clear()
        self.write(f"{self.score}", font=["Courier", 60, "normal"])


left_side = Paddle('left')
right_side = Paddle('right')
ball = Ball()
left_score = Score("left")
right_score = Score("right")

screen.onkeypress(key="w", fun=left_side.move_up)
screen.onkeypress(key="s", fun=left_side.move_down)
screen.onkeypress(key="Up", fun=right_side.move_up)
screen.onkeypress(key="Down", fun=right_side.move_down)



while True:
    time.sleep(0.1*ball.move_speed)
    screen.update()
    left_side.stop_moving()
    right_side.stop_moving()
    ball.move()
    ball.bounce(left_side, right_side)
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.refresh()
        left_score.update_score(ball)
        right_score.update_score(ball)




screen.exitonclick()

