#!/bin/python3

from random import randint

playerName = input('Hello, player. Type, please, Your name\n')# Вводимо ім'я гравця
player = input('rock (r), paper (p) or scissors (s)?')# гравець робить свій вибір
playerASCII = '' #змінна в яку буде зебережно відповідність літера - ASCII символ
chosen = randint(1,3)# змінна для збереження "вибору" комп'ютера
if chosen == 1: #домовляємося, що кожен "вибір" ком'ютера відповідає відповідає ASCII символу, 1 це камінь 'O' і т.д.
  computer = 'O'
elif chosen == 2:
  computer = '______'
else:
  computer = '>8'

if player == 'r': #домовляємося, що кожен вибір гравця відповідає ASCII символу, r камінь це 'O' і т.д.
  playerASCII = 'O'
elif player == 'p':
  playerASCII = '______'
else:
  playerASCII = '>8'
  
if playerASCII == computer: #якщо нічия
  print(playerName, "обрав", playerASCII, 'vs', "вибір комп'ютера", computer)
  print('DRAW!') #якщо нічия
elif playerASCII == 'O' and computer == '>8': #камінь псує ножиці
  print(playerName, "обрав", playerASCII, 'vs', "вибір комп'ютера", computer) #друкуємо вибір гравця і комп'ютера
  print('Player WINS!') #і кажемо хто переможець
elif playerASCII == 'O' and computer == '______':
  print(playerName, "обрав", playerASCII, 'vs', "вибір комп'ютера",  computer)
  print('Computer WINS')
elif playerASCII == '______' and computer == 'O':
  print(playerName, "обрав", playerASCII, 'vs', "вибір комп'ютера",  computer)
  print('Player WINS')
elif playerASCII == '>8' and computer == '______':
  print(playerName, "обрав", playerASCII, 'vs', "вибір комп'ютера",  computer)
  print('Player WINS')
elif playerASCII == '______' and computer =='>8':
  print(playerName, "обрав", playerASCII, 'vs', computer)
  print('Computer WINS')
