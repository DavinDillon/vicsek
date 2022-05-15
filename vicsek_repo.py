import turtle
import random

D = (-250, 250)
A = (250, 250)
B = (-250,-250)
C = (250,-250)
M = (0,0)



t = turtle.Turtle()
scn = turtle.Screen()
scn.tracer(False)
scn.colormode(255)
scn.bgcolor('black')
t.speed(0)
t.hideturtle()
t.pencolor(255,255,51)

t.penup()
temp = 0
turtle.title('Vicsek Chaos')
colors = ['red', 'orange', 'yellow', 'green', 'blue','indigo', 'purple']

for i in range(8000):
    x = random.randint(1,5)
    y = random.randint(0,6)
    t.pencolor(colors[y])

    if x == 1:
        dist = t.distance(A)
        t.setheading(t.towards(A))
    elif x ==2:
        dist = t.distance(B)
        t.setheading(t.towards(B))
    elif x == 3:
        dist = t.distance(C)
        t.setheading(t.towards(C))
    elif x == 4:
        dist = t.distance(D)
        t.setheading(t.towards(D))
    elif x == 5:
        dist = t.distance(M)
        t.setheading(t.towards(M))
    t.forward(2*dist/3)
    t.pendown()
    t.dot(3)
    t.penup()
    scn.update()
    temp = x
scn.tracer(True)
scn.mainloop()
