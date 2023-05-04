import turtle

# Create turtle object
t = turtle.Pen()
t.speed(10)

# Draw Doraemon's face
t.penup()
t.goto(0, -150)
t.pendown()

t.begin_fill()
t.fillcolor('#0180c9')
t.circle(200)
t.end_fill()

t.penup()
t.goto(0, -165)
t.pendown()

t.begin_fill()
t.fillcolor('white')
t.circle(180)
t.end_fill()


# Draw Doraemon's eyes
# Left eye
t.penup()
t.goto(-50, 100)
t.pendown()

t.begin_fill()
t.fillcolor('white')
t.circle(50)
t.end_fill()

t.penup()
t.goto(-50, 125)
t.pendown()

t.begin_fill()
t.fillcolor('black')
t.circle(20)
t.end_fill()


t.penup()
t.goto(-55, 140)
t.pendown()

t.begin_fill()
t.fillcolor('white')
t.circle(5)
t.end_fill()


# Right eye
t.penup()
t.goto(50, 100)
t.pendown()

t.begin_fill()
t.fillcolor('white')
t.circle(50)
t.end_fill()

t.penup()
t.goto(50, 125)
t.pendown()

t.begin_fill()
t.fillcolor('black')
t.circle(20)
t.end_fill()


t.penup()
t.goto(45, 140)
t.pendown()

t.begin_fill()
t.fillcolor('white')
t.circle(5)
t.end_fill()


# Draw Doraemon's nose
t.penup()
t.goto(0, 68)
t.pendown()

t.begin_fill()
t.fillcolor('red')
t.circle(25)
t.end_fill()


t.penup()
t.goto(-15, 95)
t.pendown()

t.color('red')
t.begin_fill()
t.fillcolor('white')
t.circle(5)
t.end_fill()



# Draw Doraemon's mouth
t.color('black')
t.penup()
t.goto(0, 68)
t.pendown()

t.right(90)
t.forward(164)

t.penup()
t.goto(-95, 0)
t.pendown()

t.circle(95, 180)



# Draw Doraemon's whiskers
# left
t.penup()
t.goto(-80, 60)
t.pendown()

t.left(50)
t.forward(70)
t.right(50)

t.penup()
t.goto(-80, 50)
t.pendown()

t.left(90)
t.forward(70)
t.right(90)

t.penup()
t.goto(-80, 40)
t.pendown()

t.left(140)
t.forward(70)
t.right(140)

# right
t.penup()
t.goto(80, 60)
t.pendown()

t.right(50)
t.forward(70)
t.left(50)

t.penup()
t.goto(80, 50)
t.pendown()

t.right(90)
t.forward(70)
t.left(90)

t.penup()
t.goto(80, 40)
t.pendown()

t.right(140)
t.forward(70)
t.left(140)



# Draw Doraemon's bell
t.penup()
t.goto(28, -180)
t.pendown()

t.begin_fill()
t.fillcolor('yellow')
t.circle(30)
t.end_fill()

t.penup()
t.goto(8, -175)
t.pendown()

t.begin_fill()
t.fillcolor('black')
t.circle(10)
t.end_fill()

t.circle(10, 270)
t.right(90)
t.forward(27)





t.hideturtle()
turtle.done()
                  
