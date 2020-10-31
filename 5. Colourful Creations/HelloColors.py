#!/bin/python3
from turtle import *
screen = Screen()
screen.setup(400, 400)
colours = {'verylime':'#A7E30E', 'reallyraspberry':'#FA057F'}
screen.bgcolor('#DBC286')
hight = input("Введіть розмір шрифту")
color('#6063EB')
style = ('Arial', hight, 'bold')
write('Привіт, Світ', font=style, align='center')
hideturtle()
