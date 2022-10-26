import turtle

class Ball:
    def __init__(self):
        self.ball=turtle.Turtle()
        self.inix=1
        self.iniy=1
    def balls(self):
        self.ball.shapesize(0.5,0.5,1)
        self.ball.shape('square')
        self.ball.color('blue')
        self.ball.pu()
        self.ball.goto(-4,0)
        self.ball.speed('normal')
    def ballmov(self):
        self.ball.goto(self.ball.xcor()+self.inix,self.ball.ycor()+self.iniy)

