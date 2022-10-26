from time import time
from paddle_screen import Paddle,Screen
from ball_prop import Ball
import time


scrz=Screen()
scrz.setup()
scrz.outline()
ballz=Ball()
ballz.balls()
firstpadd=Paddle((350,0))
secpadd=Paddle((-357,0))
while scrz.vl==0:    
    scrz.start()
scrz.pr.clear()
firstpadd.spaddlemov()
secpadd.fpaddlemov()
game_is_not_over=True
scrz.pr.color('red')
scrz.pr.write(f'{secpadd.score}\t\t{firstpadd.score}',font=('verdana',17,'bold'),align='center')
while game_is_not_over:
    if firstpadd.score <10 and secpadd.score <10:
        scrz.scr.delay(2)
        ballz.ballmov()
        if ballz.ball.ycor()>235 :
            if ballz.inix==1 and ballz.iniy == 1:
                ballz.inix,ballz.iniy=1,-1
            elif ballz.inix==-1 and ballz.iniy == 1:
                ballz.inix,ballz.iniy=-1,-1
        elif ballz.ball.ycor()<-235:
            if ballz.inix==-1 and ballz.iniy == -1:
                ballz.inix,ballz.iniy=-1,1
            elif ballz.inix==1 and ballz.iniy == -1:
                ballz.inix,ballz.iniy=1,1
        elif ballz.ball.xcor()>332 and ballz.ball.distance(firstpadd.padd)<50:
            if ballz.inix==1 and ballz.iniy == 1:
                ballz.inix,ballz.iniy=-1,1
            elif ballz.inix==1 and ballz.iniy == -1:
                ballz.inix,ballz.iniy=-1,-1
        elif ballz.ball.xcor()<-335 and ballz.ball.distance(secpadd.padd)<50:
            if ballz.inix==-1 and ballz.iniy == -1:
                ballz.inix,ballz.iniy=1,-1
            elif ballz.inix==-1 and ballz.iniy == 1:
                ballz.inix,ballz.iniy=1,1
        elif ballz.ball.xcor()>352 or ballz.ball.xcor()<-360:
            if ballz.ball.xcor()>352:
                secpadd.score+=1
            elif ballz.ball.xcor()<-360:
                firstpadd.score+=1
            scrz.pr.clear()
            scrz.pr.write(f'{secpadd.score}\t\t{firstpadd.score}',font=('verdana',17,'bold'),align='center')
            time.sleep(2)
            ballz.ball.ht()
            ballz.ball.goto(-4,0)
            ballz.inix=1
            ballz.iniy=1
            ballz.ball.st()
            time.sleep(2)
        else:
            pass
                 
    else:
        if firstpadd.score == 10:
            scrz.pr.goto(175,0)
            scrz.pr.color('green')
            scrz.pr.write(f'YOU WON!',font=('verdana',17,'normal'),align='center')
        else:
            scrz.pr.goto(-175,0)
            scrz.pr.color('green')
            scrz.pr.write(f'YOU WON!',font=('verdana',17,'normal'),align='center')
scrz.pr.clear()
scrz.gameover()
scrz.scr.exitonclick()












