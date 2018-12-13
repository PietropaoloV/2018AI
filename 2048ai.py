def decide_move(board,prob):
	left = 0
	up = 0
	down = 0
	right = 0
	for x in range(1,len(board)-1):
		for y in range(1,len(board)-1):
			if(board[x][y]!=0):

				ret = pick_direction(board,x,y)
				print(ret)
				temps = ret[0]
				weight = ret[1]
				r = random.randint(0,9)
				if(temps==1):
					if(r<=8):
						down+=1+weight
					else:
						up+=1
				if(temps==2):
					if(r<=8):
						right+=1+weight
					else:
						left+=1
				if(temps==3):
					if(r<=8):
						left+=1+weight
					else:
						right+=1
				if(temps==4):
					if(r<=8):
						up+=1+weight
					else:
						down+=1

	maximums = max(left,up,down,right)
	if(right == maximums):
		return 'd'
	elif(left == maximums):
		return 'a'
	elif(up == maximums):
		return 'w'
	else:
		return 's'
def pick_direction(board,x,y):
	current = board[x][y]
	if(board[x][y]!=0):
		if(board[x+1][y] == current):
			return (1,math.log(current,2.0))
		elif(board[x][y-1] == current):
			return (3,math.log(current,2.0))
		elif(board[x][y+1] == current):
			return (2,math.log(current,2.0))
		elif(board[x-1][y] == current):
			return (4,math.log(current,2.0))
		return (random.randint(1,4),math.log(current,2.0))
	return (0,0);