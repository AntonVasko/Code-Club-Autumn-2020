from turtle import *
from random import *

#Черепашки
shape("turtle")

def randomcolour():
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  color(red, green, blue)

def randomplace():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()
  
def randomheading():
  degrees = randint(1, 360)
  setheading(degrees)
#Черепашки
speed(10)  
for i in range(30):
  randomcolour()
  randomheading()
  randomplace()
  stamp()

#Квадрати  
clear()
setheading(0)

def drawrectangle():
  hideturtle()
  randomcolour()
  randomplace()
  lenght = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(lenght)
  right(90)
  forward(height)
  right(90)
  forward(lenght)
  right(90)
  forward(height)
  right(90)
  end_fill()

speed(10) 
for i in range(30):  
  drawrectangle()

#Кола
clear()

def drawcircle():
  hideturtle()
  dt = randint(5, 150)
  randomcolour()
  randomplace()
  dot(dt)
  
speed(10) 
for i in range(30):
  drawcircle()
  
#Зірки
clear()

def drawstar():
  hideturtle()
  randomcolour()
  randomplace()
  count = 1
  lenght = randint(10, 100)
  while count <= 5:
    begin_fill()
    forward(lenght)
    right(144)
    count = count + 1
    end_fill()

speed(10) 
for i in range(30):
  drawstar()
