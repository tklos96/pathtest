from game import Game
import numpy as np
import argparse
import matplotlib
import matplotlib.pyplot as plt


def main():
    parser=argparse.ArgumentParser(description='board game path tester')
    parser.add_argument('--file','-f',type=str,help='filename')
    parser.add_argument('--num','-n',type=int,help='number of games',default=1000)
    parser.add_argument('--graph','-g',action='store_true',help='plot results')
    parser.add_argument('--output','-o',type=str,help='outputfile')
    parser.add_argument('--landed','-l',action='store_true',help='print most/least landed')
    parser.add_argument('--ended','-e',action='store_true',help='print most/least ended')
    parser.add_argument('--printnum','-p',default=5,help='number to print most/least ended/landed')
    parser.add_argument('--figid','-i',type=int,default=1,help='1=graph landed, 2=graph ended')
    args=parser.parse_args()


    game1 = Game(args.file)
    spacesHit = np.zeros(game1.spaces)
    spacesEnd = np.zeros(game1.spaces)
    totalTurns = 0

    for i in range(args.num):
      totalTurns += game1.runGame()
      for j in range(game1.spaces):
        if (game1.landed[j]>0):
          spacesHit[j] += 1
        if (game1.ended[j]>0):
          spacesEnd[j] += 1

    avgTurns = totalTurns/float(args.num)
    spacesHit = spacesHit/float(args.num)
    spacesEnd = spacesEnd/float(args.num)


    print("Games played: "+str(args.num))
    print("Average turns to win: "+str(avgTurns))

    if(args.landed):
        print("Most landed on spaces: ")
        mostCommon = np.argsort(-spacesHit)
        for k in range(args.printnum):
          argout = mostCommon[k]
          outstr = "  Space: "+str(argout)
          outstr += ", Land pct: "+str(spacesHit[argout])
          outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

          print (outstr)

        print("Least landed on spaces: ")
        leastCommon = np.argsort(spacesHit)
        for k in range(args.printnum):
          argout = leastCommon[k]
          outstr = "  Space: "+str(argout)
          outstr += ", Land pct: "+str(spacesHit[argout])
          outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

          print (outstr)

    if(args.ended):
        print("Most ended on spaces: ")
        mostCommon = np.argsort(-spacesEnd)
        for k in range(args.printnum):
          argout = mostCommon[k]
          outstr = "  Space: "+str(argout)
          outstr += ", Land pct: "+str(spacesEnd[argout])
          outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

          print (outstr)
        
        print("Least ended on spaces: ")
        leastCommon = np.argsort(spacesEnd)
        offset = np.sum(spacesEnd==0)
        for k in range(args.printnum):
          argout = leastCommon[k+offset]
          outstr = "  Space: "+str(argout)
          outstr += ", Land pct: "+str(spacesEnd[argout])
          outstr += ", Description: "+str(game1.turnmod[argout]) + ","+str(game1.spacemod[argout])+","+game1.description[argout]

          print (outstr)

    if(args.graph):
        if(args.figid==1):
          plt.figure(figsize = (20,6))
          h = plt.bar(xrange(game1.spaces),spacesHit,label=game1.description)
          plt.subplots_adjust(bottom=0.3)
          plt.xticks(np.arange(game1.spaces)+0.75,game1.description,ha='right',rotation=90)
          if not (args.output is None):
            plt.savefig(args.output+'.pdf')
          plt.show()
        elif(args.figid==2):
          plt.figure(figsize = (20,6))
          h = plt.bar(xrange(game1.spaces),spacesEnd,label=game1.description)
          plt.subplots_adjust(bottom=0.3)
          plt.xticks(np.arange(game1.spaces)+0.75,game1.description,ha='right',rotation=90)
          if not (args.output is None):
            plt.savefig(args.output+'.pdf')
          plt.show()

if __name__ == '__main__':
    main()
