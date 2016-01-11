import Tkinter
import sys

class gridGUIDemo:
	board_dic = {}

	def __init__(self, rows, columns): 
		piece_row = 0
		piece_col = 0

		for row in range(0, rows):
			for col in range(0, columns):
				self.board_dic[row,col] = "0"

	def pressedUp(event):
		print("pressed up")
		self.piece_col-=1

	def pressedDown(event):
		print("pressed down")
		self.piece_col+=1

	def pressedLeft(event):
		print("pressed left")
		self.piece_row-=1

	def pressedRight(event):
		print("pressed right")
		self.piece_row+=1

	def setDirection(master):
		master.bind_all("<Up>", pressedUp)
		master.bind_all("<Down>", pressedDown)
		master.bind_all("<Left>", pressedLeft)
		master.bind_all("<Right>", pressedRight)

	def setPiece(row, column):
		self.board_dic[row,column] = "~"
		#board[row][column] = "~"

	def getPiece():
		# to access row: getPiece()[:1]
		# to access col: getPiece()[1:]
		return self.board_dic.keys()[self.board_dic.values().index("~")]
		
	def displayBoard(master):
		for k in self.board_dic:
			if(self.board_dic[k] == "~"):
				Tkinter.Label(master, bg="white", borderwidth=1, height=1,width=2).grid(row=k[:1], column=k[1:2])
			else:
				Tkinter.Label(master, bg="black", borderwidth=1, height=1,width=2).grid(row=k[:1],column=k[1:2])

	def clearBoard():
		for k in self.board_dic:
			self.board_dic[k] = "0"

	def updateBoard(master):
		clearBoard()
		setPiece(piece_row, piece_col)
		displayBoard(master)
		master.after(1000, updateBoard)

def main(argv):
	root = Tkinter.Tk()

	grid = gridGUIDemo(23, 43)
	setDirection(root)

	setPiece(11, 22)
	displayBoard(root)

	root.after(1000, updateBoard)
	root.mainloop()

if __name__ == "main":
	main(sys.argv)
