import turtle
t = turtle.Turtle()
t.shape()
t.width(5)
t.color('grey')

#Фамилия
t.forward(30)
t.left(90)
t.forward(100) 
t.right(90)  
t.forward(50)  
t.right(90)  
t.forward(100) 

#Имя
t.penup()
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.pendown()


t.right(180)  
t.forward(100)
t.right(215)  
t.forward(120)
t.left(215)
t.forward(100)


#Отчество
t.penup()
t.right(-90)
t.forward(50)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)


turtle.done()