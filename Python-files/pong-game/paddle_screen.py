import turtle

class Paddle:
    def __init__(self,position):
        self.padd=turtle.Turtle('square')
        self.score=0
        self.padd.pu()
        self.padd.goto(position)
        self.padd.color('white')
        self.padd.shapesize(4,1)
    def up(self):
        if self.padd.ycor()<200:
            self.padd.goto(self.padd.xcor(),self.padd.ycor()+40)
        else:
            pass
    def down(self):
        if self.padd.ycor()>-200:
            self.padd.goto(self.padd.xcor(),self.padd.ycor()-40)
        else:
            pass
    def fpaddlemov(self):
        turtle.listen()
        turtle.onkeypress(self.up,'w')
        turtle.onkeypress(self.down,'s')
    def spaddlemov(self):
        turtle.listen()
        turtle.onkeypress(self.up,'o')
        turtle.onkeypress(self.down,'k')


class Screen():
    def __init__(self):
        self.vl=0
        self.scr=turtle.Screen()
        self.line=turtle.Turtle()
        self.pr=turtle.Turtle()
    def setup(self):
        self.scr.bgcolor('black')
        self.scr.setup(800,600)
        self.scr.title('pong game')
    def outline(self):
        self.line.ht()
        self.line.pu()
        self.line.speed('normal')
        self.line.pensize(2)
        self.line.color('grey')
        self.line.goto(-368,-243)
        self.line.pd()
        self.line.setheading(90)
        for i in range(2):
            self.line.fd(485)
            self.line.rt(90)
            self.line.fd(730)
            self.line.rt(90)
        self.line.rt(90)
        self.line.fd(730//2)
        self.line.setheading(90)
        for i in range(98//2):
            self.line.fd(5)
            self.line.pu()
            self.line.fd(5)
            self.line.pd()
    def st(self):
        self.vl=1
    def start(self):
        self.pr.pu()
        self.pr.ht()
        self.pr.color('indigo')
        self.pr.goto(0,260)
        self.pr.write(f'PRESS \'s\' TO START',font=('arial',17,'normal'),align='center')
        turtle.listen()
        turtle.onkeypress(self.st,'s')
    def gameover(self):
        self.pr.color('red')
        self.pr.write(f'GAME OVER',font=('arial',15,'normal'),align='center')
