import turtle

t=turtle.Turtle()

screen = turtle.Screen()
screen.setup(800,800)
screen.bgcolor('hotpink')

t2=turtle.Turtle()
t2.penup()
t2.hideturtle()

t3=turtle.Turtle()
t3.penup()
t3.hideturtle()

t4=turtle.Turtle()
t4.penup()
t4.hideturtle()

t5=turtle.Turtle()
t5.penup()
t5.hideturtle()

t.penup()
t.goto(0,50)
t.pendown()
t.write("Turtle Presentation", font=("arial", 30, "bold"),align="center")

t.penup()
t.goto(0,-50)
t.write("Gianna Regec", font=("arial", 20, "bold"),align="center")
t.pendown()

enter = input("Press Enter to Continue: ")

t.clear()
screen.bgcolor('teal')

turtle.addshape("icecream.gif")
t2.shape("icecream.gif")
t2.goto(-100,100)
a = t2.stamp()
t2.goto(-100,100)

turtle.addshape("chicken.gif")
t2.shape("chicken.gif")
t2.goto(200,-100)
a = t2.stamp()
t2.goto(200,-100)

turtle.addshape("mac.gif")
t2.shape("mac.gif")
t2.goto(200,50)
a = t2.stamp()
t2.goto(200,50)

t.penup()
t.goto(0,-50)
t.write("Favorite Foods", font=("arial", 15, "bold"),align="center")
t.pendown()

t.penup()
t.goto(-100,-100)
t.pendown()
t.fillcolor('hotpink')
t.begin_fill()
t.circle(32)
t.end_fill()

t.clear()
t2.clear()

enter = input("Press Enter to Continue: ")
screen.bgcolor('red')

t.penup()
t.goto(0,-50)
t.write("Hobbies", font=("arial", 15, "bold"),align="center")
t.pendown()

turtle.addshape("drums.gif")
t3.shape("drums.gif")
t3.goto(250,175)
b = t3.stamp()
t3.goto(250,175)

turtle.addshape("sleeping.gif")
t3.shape("sleeping.gif")
t3.goto(0,50)
b = t3.stamp()
t3.goto(0,50)

turtle.addshape("spotify.gif")
t3.shape("spotify.gif")
t3.goto(0,-200)
b = t3.stamp()
t3.goto(0,-200)

square= 50

t.penup()
t.goto(100,100)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)



t.clear()
t2.clear()
t3.clear()

enter = input("Press Enter to Continue: ")
screen.bgcolor('green')

t.penup()
t.goto(0,80)
t.write("Favorite Movie", font=("arial", 15, "bold"),align="center")
t.pendown()

turtle.addshape("favmovie.gif")
t4.shape("favmovie.gif")
t4.goto(100,-200)
a = t4.stamp()
t4.goto(100,-200)

t.fillcolor('blue')
t.begin_fill()
#octagon
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()

t.clear()
t2.clear()
t3.clear()
t4.clear()

enter = input("Press Enter to Continue: ")
screen.bgcolor('orange')

t.penup()
t.goto(0,50)
t.write("Favorite Sports", font=("arial", 15, "bold"),align="center")
t.pendown()

turtle.addshape("waterpolo.gif")
t5.shape("waterpolo.gif")
t5.goto(-100,150)
a = t5.stamp()
t5.goto(-100,150)

turtle.addshape("hockey.gif")
t5.shape("hockey.gif")
t5.goto(100,270)
a = t5.stamp()
t5.goto(100,270)




turtle.done()