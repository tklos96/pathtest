from game import Game
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

FILENAME = 'geyserhilllower.txt'
#FILENAME = 'towertrek.txt'
NUMGAMES = 1000
OUTNUM1 = 5
OUTNUM2 = 5
OUTNUM3 = 0
OUTNUM4 = 0
figid=0


game1 = Game(FILENAME)
spacesHit = np.zeros(game1.spaces)
spacesEnd = np.zeros(game1.spaces)
totalTurns = 0

for i in range(NUMGAMES):

  game1.newGame()
  while(not game1.won):
    game1.advanceTurn()

  totalTurns += game1.turn
  for j in range(game1.spaces):
    if (game1.landed[j]>0):
      spacesHit[j] += 1
    if (game1.ended[j]>0):
      spacesEnd[j] += 1

avgTurns = totalTurns/float(NUMGAMES)
spacesHit = spacesHit/float(NUMGAMES)
spacesEnd = spacesEnd/float(NUMGAMES)


print("Games played: "+str(NUMGAMES))
print("Average turns to win: "+str(avgTurns))

print("Most landed on spaces: ")
mostCommon = np.argsort(-spacesHit)
for k in range(OUTNUM1):
  argout = mostCommon[k]
  outstr = "  Space: "+str(argout)
  outstr += ", Land pct: "+str(spacesHit[argout])
  outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

  print (outstr)

print("Least landed on spaces: ")
leastCommon = np.argsort(spacesHit)
for k in range(OUTNUM2):
  argout = leastCommon[k]
  outstr = "  Space: "+str(argout)
  outstr += ", Land pct: "+str(spacesHit[argout])
  outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

  print (outstr)

print("Most ended on spaces: ")
mostCommon = np.argsort(-spacesEnd)
for k in range(OUTNUM3):
  argout = mostCommon[k]
  outstr = "  Space: "+str(argout)
  outstr += ", Land pct: "+str(spacesEnd[argout])
  outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

  print (outstr)
print("Least ended on spaces: ")
leastCommon = np.argsort(spacesEnd)
offset = np.sum(spacesEnd==0)
for k in range(OUTNUM4):
  argout = leastCommon[k+offset]
  outstr = "  Space: "+str(argout)
  outstr += ", Land pct: "+str(spacesEnd[argout])
  outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

  print (outstr)


if(figid==1):
  plt.figure(figsize = (20,6))
  h = plt.bar(xrange(game1.spaces),spacesHit,label=game1.description)
  plt.subplots_adjust(bottom=0.3)
  plt.xticks(np.arange(game1.spaces)+0.75,game1.description,ha='right',rotation=90)
  plt.show()
elif(figid==2):
  plt.figure(figsize = (20,6))
  h = plt.bar(xrange(game1.spaces),spacesEnd,label=game1.description)
  plt.subplots_adjust(bottom=0.3)
  plt.xticks(np.arange(game1.spaces)+0.75,game1.description,ha='right',rotation=90)
  plt.show()
