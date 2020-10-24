#!/bin/python3
from random import choice

players = ['Harry', 'Hermione', 'Anton', 'Kseniya', 'A', 'B', 'C', 'D'] 
print('Початковий список гравців-претендентів', players)
teamA = []
teamB = []

while len(players)>0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)

  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)

print('Гравець-капітан команди А', playerA)
print('Команда А: ', teamA)

print('Гравець-капітан команди В', playerB)
print('Команда В: ', teamB)

print('Залишок гравців-претендентів: ', players)
