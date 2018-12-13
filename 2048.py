import numpy as np
import msvcrt
import os
import random
def make_grid(x):
	return np.zeros(shape=(x,x))

def merger_d(x,y,xa,ya,board):
	board[x+xa][y+ya] = 2*board[x][y]
def mergel_u(x,y,xa,ya,board):
	board[x+xa][y+ya] = 2*board[x][y]

def make_move_up(board,xa,ya):
	ret = False
	for x in range(len(board)-1,-1,-1):
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
def make_move_down(board,xa,ya):
	ret = False
	for x in range(0,len(board)):
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
		for y in xrange(0,len(board)):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
def make_move_right(board,xa,ya):
	ret = False
	for x in range(0,len(board)):
		for y in xrange(len(board)-1,-1,-1):
			if(x+xa<len(board) and y+ya <len(board) and x+xa>=0 and y+ya>=0):
				if(board[x][y] == board[x+xa][y+ya]):
					board[x+xa][y+ya] *=2
					board[x][y]=0
					ret = True
	
	return ret
	
def move_over_down(board):
	ret = False
	for x in range(len(board)-1,-1,-1):
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
	for x in range(0,len(board)):
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
				print('yes',x,y)
				board[x-dist][y] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def move_over_left(board):
	ret = False
	for x in range(0,len(board)):
		for y in xrange(0,len(board)):
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
				print('yes',x,y)
				board[x][y-dist] = board[x][y];
				board[x][y]=0;
				ret = True
	return ret
def move_over_right(board):
	ret = False
	for x in range(0,len(board)):
		for y in xrange(len(board)-1,-1,-1):
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
		number = random.randint(1,2)
		if(number == 1):
			number = 4
		else:
			number = 2
		board[pos[position][0]][pos[position][1]] = number
		ret = True
	return ret

def main():
	board = make_grid(4);
	random.seed()
	input_char = 1
	board[2][1] = 2;
	board[2][2] = 4
	board[random.randint(0,3)][random.randint(0,3)] = 2;
	clear = lambda: os.system('cls')
	free = True
	ret = False
	print(board)
	while(input_char!='q' and free):
		input_char = msvcrt.getch()
		#clear()
		if (input_char == 'w'):
			ret = make_move_up(board,-1,0)
			slide =move_over_up(board)
		if (input_char == 'a'):
			ret = make_move_left(board,0,-1)
			slide =move_over_left(board)
		if (input_char == 's'):
			ret = make_move_down(board,1,0)
			slide =move_over_down(board)
		if (input_char == 'd'):
			ret = make_move_right(board,0,1)
			slide =move_over_right(board)
		if(ret or slide):
			free = place_random(find_free(board),board)
			

		print(board)
main()