import turtle


def draw_eyeCat(some_turtle):
    some_turtle.circle(120)
    for i in range(60):
        some_turtle.circle(90-i)
        #print(i)


def draw_twoEyeCat(some_turtle):
    some_turtle.left(90)
    some_turtle.forward(50)
    some_turtle.left(90)
    some_turtle.forward(50)
    some_turtle.right(90)
    draw_eyeCat(some_turtle)
    some_turtle.left(90)
    some_turtle.backward(100)
    some_turtle.left(90)
    draw_eyeCat(some_turtle)
    some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.right(90)
    some_turtle.backward(50)


def draw_noseCat(some_turtle):
    # some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.right(120)
    for i in range(90):
        some_turtle.forward(100-i)
        some_turtle.right(120)
        #print(i)
    some_turtle.home()


def draw_mountCat(some_turtle):
    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(30)
    some_turtle.forward(100)
    some_turtle.backward(100)
    some_turtle.left(60)
    some_turtle.forward(100)
    some_turtle.backward(100)
    some_turtle.home()


def draw_art():
    window = turtle.Screen()
    window.bgcolor('#ff8c00')

    angie = turtle.Turtle()
    ryan = turtle.Turtle()
    sofia = turtle.Turtle()

    angie.shape("turtle")
    angie.color('#c71585')
    angie.width(5)
    angie.speed("fastest")

    ryan.shape("circle")
    ryan.color('#FF0000')
    ryan.width(10)
    ryan.speed("normal")

    sofia.shape("classic")
    sofia.color('#ff1493')
    sofia.width(5)
    sofia.speed("fastest")

    draw_twoEyeCat(angie)
    draw_mountCat(ryan)
    draw_noseCat(sofia)

    turtle.exitonclick()


draw_art()
