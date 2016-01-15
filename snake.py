import Tkinter

class Snake(object):
	def __init__(self):
		self.rows = 11
		self.cols = 11
		self.board = [[0 for x in range(0, self.cols)] for y in range(0, self.rows)]
		self.Right = False
		self.Left = True
		self.Up = False
		self.Down = False
		self.can_move = False

		for r in range(0, len(self.board)):
			for c in range(0, len(self.board[r])):
				self.board[r][c]="~"

		self.snake = {	0	:	[5,5],
						1	:	[6,5],	
						2	:	[7,5],
						3	:	[8,5]	}

		self.temp = [5,5]

		self.board[self.snake[0][0]][self.snake[0][1]] = "0"
		self.board[self.snake[1][0]][self.snake[1][1]] = "1"
		self.board[self.snake[2][0]][self.snake[2][1]] = "2"
		self.board[self.snake[3][0]][self.snake[3][1]] = "3"

	def keyPressed(self, event):
		if event.keysym == 'Escape':
			root.destroy()
		elif event.keysym == 'Right':
			self.Right = True
			self.Up = False
			self.Down = False
			self.Left = False
		elif event.keysym == 'Left':
			self.Right = False
			self.Up = False
			self.Down = False
			self.Left = True
		elif event.keysym == 'Up':
			self.Right = False
			self.Up = True
			self.Down = False
			self.Left = False
		elif event.keysym == 'Down':
			self.Right = False
			self.Up = False
			self.Down = True
			self.Left = False
	
	def moveHead(self):
		nex_coor = self.snake[0]
		if(self.Up):
			nex_coor[0]-=1
		elif(self.Down):
			nex_coor[0]+=1
		elif(self.Right):
			nex_coor[1]+=1
		else:
			nex_coor[1]-=1
		
		if(self.board[nex_coor[0]][nex_coor[1]] == "~"):
			self.temp = self.snake[0] 
			self.snake[0] = nex_coor
			self.can_move = True
		else:
			self.can_move = False

	def moveBody(self):
		if(self.can_move):
			for segment in self.snake.keys()[1:]:
				aTemp = self.snake[segment]
				self.snake[segment] = self.temp
				self.temp = aTemp

	def move(self):
		self.moveHead()
		self.moveBody()

	def clear(self):
		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				self.board[r][c] = "~"

	def display(self):
		for seg in self.snake.keys():
			self.board[self.snake[seg][0]][self.snake[seg][1]] = str(seg)

		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				Tkinter.Label(root, borderwidth = 1, text=self.board[r][c]).grid(row=r, column=c)

	def update(self):
		if(self.snake[0][0]==0&(self.snake[0][1]==0&(self.snake[0][0]==self.rows-1&(self.snake[0][1]==self.cols-1)))):
			print("you died!")
		else:
			self.clear()
			self.move()
			self.display()
			root.after(1000, self.update)

python = Snake()
root = Tkinter.Tk()

root.bind_all("<Key>", python.keyPressed)

python.display()

root.after(1000, python.update)
root.mainloop()
