# https://github.com/kais2503/Turtle-mini-project/blob/master/flower.py

import turtle


def draw_square(few_turtle):
    for i in range(4):
        few_turtle.forward(200)
        few_turtle.right(90)


def draw_triangle_art(few_turtle):
    for i in range(3):
        few_turtle.forward(100)
        few_turtle.right(120)


def draw_circle_art(few_turtle):
    for i in range(1):
        few_turtle.circle(100)


def draw_hexagon_art(few_turtle):
    for i in range(6):
        few_turtle.forward(300)
        few_turtle.right(60)


def draw_mosaique_art():
    window = turtle.Screen()
    window.bgcolor("black")

    mosaique = turtle.Turtle()
    mosaique.shape('classic')
    mosaique.speed('fastest')
    mosaique.color('#ff0000', '#AFEEEE')
    #mosaique.shapesize(2, 2)
    mosaique.width(2)
    mosaique.begin_fill()

    for i in range(40):
        mosaique.color('#00FFFF')
        draw_hexagon_art(mosaique)
        mosaique.left(10)
        
    for i in range(40):
        mosaique.color('#FF0000')
        draw_square(mosaique)
        mosaique.right(10)   
        
    for i in range(40):
        mosaique.color('#FFFFFF')
        draw_circle_art(mosaique)
        mosaique.left(20)        
               
    for i in range(70):
        mosaique.color('#FEEE00')
        draw_triangle_art(mosaique)
        mosaique.left(5)

 


    mosaique.end_fill

    mosaique.home()

    window.exitonclick()


draw_mosaique_art()
