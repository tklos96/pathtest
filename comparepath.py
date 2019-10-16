#!/usr/local/bin python
import numpy as np
import random
import argparse
import matplotlib
import matplotlib.pyplot as plt

from game import Game

def main():
    parser=argparse.ArgumentParser(description='board game path tester')
    parser.add_argument('--file_short','-s',type=str,help='file for short path')
    parser.add_argument('--file_long','-l',type=str,help='file for long path',required=False)
    parser.add_argument('--num','-n',type=int,help='number of games',default=1000)
    parser.add_argument('--graph','-g',action='store_true',help='plot results')
    parser.add_argument('--output','-o',type=str,help='outputfile')
    args=parser.parse_args()

    turn_array_short=[]
    win_count_short=0
    game1 = Game(args.file_short)
    if args.file_long is not None:
        turn_array_long=[]
        win_count_long=0
        game2 = Game(args.file_long)

    tenpct=int(args.num/10)
    for i in range(args.num):
        turn_count_short = game1.runGame()
        turn_array_short.append(turn_count_short)
        if (args.file_long is not None):
            turn_count_long = game2.runGame() 
            turn_array_long.append(turn_count_long)
            if turn_count_short<turn_count_long:
                win_count_short+=1
            if turn_count_short>turn_count_long:
                win_count_long+=1
        
        if i%tenpct==0:
            print(str(i/tenpct*10)+'% done')
    
    turn_array_short=np.array(turn_array_short)
    win_count_short = float(win_count_short)/args.num
    if(args.file_long is not None):
        turn_array_long =np.array(turn_array_long)
        win_count_long = float(win_count_long)/args.num
        print('Win pct short: '+str(win_count_short))
        print('Win pct long: '+str(win_count_long))

    if args.graph:
        print('graphing...')
        plt.figure(1)
        plt.subplot(111)
        bins=np.arange(130)
        plt.hist(turn_array_short,bins=bins,density=True,histtype='step',color='red',label='short')
        if(args.file_long is not None):
            plt.hist(turn_array_long,bins=bins,density=True,histtype='step',color='blue',label='long')
            plt.text(70,.02,'short win %: '+str(win_count_short))
            plt.text(70,.015,'long win %: '+str(win_count_long))
        
        plt.legend()
        plt.xlabel('# of Turns')
        plt.ylabel('density')
        if not (args.output is None):
            plt.savefig(args.output+'.pdf')
        plt.show()


if __name__ == '__main__':
    main()
