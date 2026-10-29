import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.shape('turtle')
t.pensize(3)
t.speed(100)
t.color('blue')


def rysuj(ile_bokow, dlugosc_boku):
    t.begin_fill()

    kat = 360 / ile_bokow
    for i in range(ile_bokow):
        t.forward(dlugosc_boku)
        t.right(kat)
    t.end_fill()

boki = int(screen.numinput("Wielokąt", "Podaj liczbę kątów:", 3, minval=3, maxval=12))
dlugosc_boku = 100
rysuj(boki, dlugosc_boku)

t.hideturtle()
turtle.exitonclick()