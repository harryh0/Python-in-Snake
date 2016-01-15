import Tkinter

piece_row = [11]
piece_col = [22]

rows = 23
columns = 43

board = [[0 for x in range(0, columns)] for y in range(0, rows)]

for row in range(0, rows):
	for col in range(0, columns):
		board[row][col]="0"

def pressedUp(event):
	print("pressed up")
	piece_col[0]-=1

def pressedDown(event):
	print("pressed down")
	piece_col[0]+=1

def pressedLeft(event):
	print("pressed left")
	piece_row[0]-=1

def pressedRight(event):
	print("pressed right")
	piece_row[0]+=1

def setDirection():
	root.bind_all("<Up>", pressedUp)
	root.bind_all("<Down>", pressedDown)
	root.bind_all("<Left>", pressedLeft)
	root.bind_all("<Right>", pressedRight)

def setPiece(row, column):
	board[row][column] = "~"
"""
def getPiece():
	# to access row: getPiece()[:1]
	# to access col: getPiece()[1:]
	return board_dic.keys()[board_dic.values().index("~")]
"""
def displayBoard():
	for r in board:
		for c in board[r]:
			if(board[r][c] == "~"):
				Tkinter.Label(root, bg="white", borderwidth=1, height=1,width=2).grid(row=k[:1], column=k[1:])
			else:
				Tkinter.Label(root, bg="black", borderwidth=1, height=1,width=2).grid(row=k[:1],column=k[1:])
		
def clearBoard():
	for r in board:
		for c in board[r]:
			board[r][c] = "0"

def updateBoard():
	clearBoard()
	setPiece(piece_row[0], piece_col[0])
	displayBoard()
	root.after(1000, updateBoard)


root = Tkinter.Tk()

setDirection()

setPiece(piece_row[0], piece_col[0])
displayBoard()

root.after(1000, updateBoard)
root.mainloop()

# main issue: encounters lag when return
# prognosis: Tkinter module too extensive, consider paring down only essential imports. 
# for reference as main in snake game
