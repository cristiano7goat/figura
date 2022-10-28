import turtle
t= turtle.Turtle()
t.shape()
t.width(5)
t.color('red')


#НЕБО
t.penup()
t.goto(-500 ,-200)
t.pendown()
t.left(90)
t.color('cyan')

t.fillcolor('cyan')
t.begin_fill()
t.forward(600)
t.right(90)
t.forward(1200)
t.right(90)
t.forward(600)
t.end_fill()

#Речка
t.penup()
t.goto(-500 , -200)
t.pendown()
t.fillcolor('blue')


t.begin_fill()

t.goto(500 , -200)
t.goto(500 , -400)
t.goto(-500 , -400)
t.goto(-500 , -200)
t.end_fill()

t.color('green')
t.fillcolor('green')
t.begin_fill()
#ТРАВА
t.goto(-470 , -50)
t.goto(470 ,-50)
t.goto(470 ,-200)
t.end_fill()


t.penup()
t.goto(0, 0)
t.pendown()

#Стена

t.left(90)
t.fillcolor('red')
t.begin_fill()
t.backward(300)
t.right(90)
t.backward(150)
t.right(90)
t.backward(300)
t.right(90)
t.backward(150)
t.end_fill()

#Крыша
t.fillcolor('gold')
t.begin_fill()
t.goto(0, 150)
t.goto(-150, 300)
t.goto(-300, 150)
t.goto(0, 150)
t.end_fill()

t.penup()
t.goto(-150, 75)
t.pendown()

t.circle(30)






turtle.done()
