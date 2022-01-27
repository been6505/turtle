#https://stackoverflow.com/questions/38119618/turtle-mini-project-udacity-python-drawing-moving-a-shape-around-another

import turtle

def draw_flower(ink):
    ink.up()
    ink.home()
    for degrees in range(5, 550, 5):
        
        ink.down()
        ink.forward(200-degrees)
        ink.up()
        ink.home()  # resets angle to 0 degrees
        ink.right(degrees)  # so absolute angle, not relative
        
def draw_smallFlower(ink):
    ink.up()
    ink.home()
    for degrees in range(5, 400, 5):
        ink.down()
        ink.forward(100)
        ink.up()
        ink.home()  # resets angle to 0 degrees
        ink.right(degrees)  # so absolute angle, not relative    
        
def draw_triangle(ink):
    ink.forward(100)
    ink.right(120)
    for i in range(200):
        ink.forward(200-i)
        ink.right(120)
    ink.home()

def draw_stem(ink):
    ink.goto(1, -400)
    ink.home()
    ink.goto(5, -400)
    ink.home()
    ink.goto(3, -200)
    draw_triangle(ink)

def Draw():
    window = turtle.Screen()
    window.bgcolor("#fa1234")

    stem = turtle.Turtle()
    stem.color("#006000")
    stem.speed("fastest")
    stem.width(2)

    draw_stem(stem)


    flower = turtle.Turtle()
    flower.color("#11cff9")
    flower.speed("fastest")
    flower.width(3)

    draw_flower(flower)
    
    smallFlower = turtle.Turtle()
    smallFlower.color("#ffff30")
    smallFlower.speed("fastest")
    smallFlower.width(5)
    
    draw_smallFlower(smallFlower)
    
    

Draw()
turtle.done()