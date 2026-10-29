import turtle
import random
window = turtle.Screen()
t = turtle.Turtle()
t.pensize(7)
t.shape('turtle')
def up():
 t.color(random.choice(['red','blue','yellow','green']))
 t.forward(100)
def left():
 t.left(30)
def right():
 t.right(30)

def powrot():
 t.undo()

def wracaj():
 t.goto(0,0)
def sq():
 for i in range(4):
  t.forward(40)
  t.left(90)
def circle():
 t.circle(90)
def bye():
 turtle.bye()
def click(x,y):
 t.color(random.choice(['red','blue','yellow','green']))
 t.goto(x,y)
window.onkey(sq, 'k')
window.onkey(circle,'c')
window.onkey(up,'Up') # strzałka w górę
window.onkey(left,'Left') # strzałka w lewo
window.onkey(right,'Right')
window.onkey(bye,'q')
window.onkey(wracaj, 'x')
window.onkey(powrot, 'Down')
window.onclick(click)
window.listen()
window.mainloop()