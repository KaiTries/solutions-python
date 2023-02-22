import random
import math
import stdio
import sys

stake = int(input("stake:"))
goal = int(input("goal:"))
trials = int(input("trials:"))
probability = float(input("probability:"))

bets = 0
wins = 0
for t in range(trials):
    cash = stake
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.random() < probability:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

stdio.writeln(str(100*wins//trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets//trials))
