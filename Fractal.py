from turtle import *
from random import randint
colormode(255)

speed(20)
#hideturtle()
bgcolor("black")

penup()
goto(-200,100)
pendown()

turtles1 = [getturtle()]
turtels2 = [getturtle()]

def tree(x):
    color(randint(0,255),randint(0,255),randint(0,255))
    for t in turtles1:
        #t.color(randint(0,255),randint(0,255),randint(0,255))
        t.left(60)
        t.forward(x)
        #turtels2.append(t.clone())

    for t in turtels2:
        #t.color(randint(0,255),randint(0,255),randint(0,255))
        t.right(120)
        t.forward(x)
        #turtles1.append(t.clone())

    x = x * 0.75
    turtles1.append(clone())
    turtels2.append(clone())
    tree(x)


tree(200)

done()
