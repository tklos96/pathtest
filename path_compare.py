#!/usr/local/bin python
import numpy as np
import random
import argparse
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def load_path_array(filename):
    a=np.loadtxt(filename,delimiter=',',dtype=str)
    trimmed=a[:,[0,1]]
    return trimmed.astype(int)

def execute_turn(current_position,path_array,win_con):
    roll = random.randint(1,7)
    advance = min(current_position + roll,win_con)
    #print('advance:',advance)
    new_position = advance + path_array[advance,1]
    if new_position<0:
        new_position=0
    #print('new_position:',new_position)
    return new_position, path_array[advance,0]

def sample_game(path_array_file):
    path_array = load_path_array(path_array_file)
    length=path_array.shape[0]-1

    position = 0
    turn_count = 0
    while position<length:
        position,turn_mod = execute_turn(position,path_array,length)
        turn_count = turn_count + turn_mod + 1
    return turn_count

def main():
    parser=argparse.ArgumentParser(description='board game path tester')
    parser.add_argument('--file_short','-s',type=str,help='file for short path')
    parser.add_argument('--file_long','-l',type=str,help='file for long path')
    parser.add_argument('--num','-n',type=int,help='number of games')
    parser.add_argument('--graph',action='store_true',help='plot results')
    parser.add_argument('--output',type=str,help='outputfile')
    args=parser.parse_args()

    turn_array_short=[]
    turn_array_long=[]
    win_count_short=0
    win_count_long=0

    tenpct=int(args.num/10)
    for i in range(args.num):
        turn_count_short = sample_game(args.file_short)
        turn_array_short.append(turn_count_short)
        turn_count_long = sample_game(args.file_long)
        turn_array_long.append(turn_count_long)
        if turn_count_short<turn_count_long:
            win_count_short+=1
        if turn_count_short>turn_count_long:
            win_count_long+=1
        if i%tenpct==0:
            print(str(i/tenpct*10)+'% done')
    turn_array_short=np.array(turn_array_short)
    turn_array_long =np.array(turn_array_long)
    win_count_short = float(win_count_short)/args.num
    win_count_long = float(win_count_long)/args.num
    print('Win pct short: '+str(win_count_short))
    print('Win pct long: '+str(win_count_long))

    if args.graph:
        print('graphing...')
        plt.figure(1)
        plt.subplot(111)
        bins=np.arange(130)
        plt.hist(turn_array_short,bins=bins,density=True,histtype='step',color='red',label='short')
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
