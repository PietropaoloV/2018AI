
import numpy as np
import msvcrt
import os
import random
import math
from time import sleep
import time
Max_Depth  = 10
def get_move_value(turn,di):
	ret = 0;
	board = turn.copy()
  	if(di == 1):
  		ret = make_move_upcount(board,-1,0)
	if(di == 2):
  		ret = make_move_downcount(board,0,-1)
	if(di == 3):
  		ret = make_move_leftcount(board,-1,0)
	if(di == 4):
  		ret = make_move_rightcount(board,0,1)
  	return ret


def execute_move(board,input_char):
	if (input_char == 1):
		make_move_up(board,-1,0)
		move_over_up(board)
	if (input_char == 2):
		make_move_left(board,0,-1)
		move_over_left(board)
	if (input_char == 3):
		make_move_down(board,1,0)
		move_over_down(board)
	if (input_char == 4):
		make_move_right(board,0,1)
		move_over_right(board)
	return board

def _is_terminal_state(b,size):
	board=b.copy()
	u = get_move_value(board,1)
	d = get_move_value(board,2)
	l = get_move_value(board,3)
	r = get_move_value(board,4)
	temp = np.count_nonzero(np.array(board))
	if(temp== math.pow(size,2)and u ==0 and d ==0 and l ==0 and r ==0):
		return True
	return False

def minimax(board,size,depth,turn,newboard):
	maxval = -2
	minval = size*size
	di = -1
	change = 0;
	newboard = []
	if(_is_terminal_state(board,size) or depth>Max_Depth):
		return(newboard,-1)
	if(turn > 0):
		vals=[]
		val1 = get_move_value(board,1)
		val2 = get_move_value(board,2)
		val3 = get_move_value(board,3)
		val4 = get_move_value(board,4)
		if(val1>0):
			vals.append(1)
		if(val2>0):
			vals.append(2)
		if(val3>0):
			vals.append(3)
		if(val4>0):
			vals.append(4)
		if(len(vals)== 0):
			b=board
			place_random(find_free(b),b)
			return (b,0)
		for x in range(0,len(vals)):
			cop2 = board.copy()
			teststate = execute_move(cop2,vals[x])
			testval = minimax(teststate,size,depth+1,turn*-1,newboard)[1]
			if(maxval<testval):
				maxval = testval
				newboard = teststate
			return(newboard,maxval)
		return (newboard,maxval)
	else:
		cop = board.copy()
		free = find_free(board)
		for x in range(0,len(free)):
			cop[free[x][0]][free[x][1]]=2
			testval = minimax(cop,size,depth+1,turn*-1,newboard)[1]
			if(minval>testval):
				minval=testval
				newboard=cop
			return (newboard,minval)
		return(newboard,minval)

#########################################################################
def make_grid(x):
	return np.zeros(shape=(x,x))

def make_move_upcount(board,xa,ya):
	ret = 0
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya] and board[x][y]!=0):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret +=1
	return ret
def make_move_downcount(board,xa,ya):
	ret = 0
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]and board[x][y]!=0):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret +=1
	return ret
def make_move_leftcount(board,xa,ya):
	ret = 0
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]and board[x][y]!=0):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret +=1
	return ret
def make_move_rightcount(board,xa,ya):
	ret = 0
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]and board[x][y]!=0):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret +=1
	return ret



















def make_move_up(board,xa,ya):
	ret = False
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	return ret
def make_move_down(board,xa,ya):
	ret = False
	for x in range(len(board)-1,-1,-1):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
def make_move_left(board,xa,ya):
	ret = False
	for x in range(0,len(board)):
		for y in range(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
def make_move_right(board,xa,ya):
	ret = False
	for x in range(0,len(board)):
		for y in range(len(board)-1,-1,-1):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
	
def move_over_down(board):
	ret = False
	for x in xrange(0,len(board)):
		for y in xrange(0,len(board)):
			dist = 1
			while(x+dist<len(board) and board[x][y]!=0):
				if(board[x+dist][y]==0):
					dist += 1
				else:
					dist -= 1
					break
			if(x+dist>=len(board)):
				dist=len(board)-1-x
			if(dist>0 and board[x][y]!=0):
				board[x+dist][y] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def move_over_up(board):
	ret = False
	for x in range(len(board)-1,-1,-1):
		for y in xrange(0,len(board)):
			dist = 1
			while(x-dist>=0 and board[x][y]!=0):
				if(board[x-dist][y]==0):
					dist += 1
				else:
					dist -= 1
					break
			if(x-dist<=0):
				dist=x
			if(dist>0 and board[x][y]!=0):
				board[x-dist][y] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def move_over_left(board):
	ret = False
	for x in range(0,len(board)):
		for y in range(0,len(board)):
			dist = 1
			while(y-dist>=0 and board[x][y]!=0):
				if(board[x][y-dist]==0):
					dist += 1
				else:
					dist -= 1
					break
			if(y-dist<=0):
				dist=y
			if(dist>0 and board[x][y]!=0):
				board[x][y-dist] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def move_over_right(board):
	ret = False
	for x in range(0,len(board)):
		for y in range(len(board)-1,-1,-1):
			dist = 1
			while(y+dist<len(board) and board[x][y]!=0):
				if(board[x][y+dist]==0):
					dist += 1
				else:
					dist -= 1
					break
			if(y+dist>=len(board)):
				dist=len(board)-1-y
			if(dist>0 and board[x][y]!=0):
				
				board[x][y+dist] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def find_free(board):
	tempx = 0
	tempy = 0
	ret = []
	for x in range(0,len(board)):
		for y in xrange(0,len(board)):
			if(board[x][y] == 0):
				ret.append([x,y])
	return ret
def place_random(pos,board):
	ret = False
	if(len(pos)>0):
		position = 	random.randint(0,len(pos)-1)
		number = 2
		board[pos[position][0]][pos[position][1]] = number
		ret = True
	return ret

def main():
	size = 4
	board = make_grid(size);
	random.seed()
	input_char = 1
	board[random.randint(0,3)][random.randint(0,3)] = 2;
	clear = lambda: os.system('cls')
	free = True
	ret = False
	slide = False
	print(board)
	start = time.time()
	while(input_char!='q' and free):
		if(_is_terminal_state(board,size)):
			print(board)
			break
		clear()
		input_char= minimax(board.copy(),size,0,1,[])
		board = input_char[0]
		print(board)
		#sleep(0.1)
		
	end = time.time()
	print(end - start)
main()

