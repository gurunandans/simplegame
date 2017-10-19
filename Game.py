from tkinter import *
from random import *

class CleanSweeper:
	
	def __init__(self):
		self.count=0
		self.score={"player1":0,"player2":0}
		self.matrix=[]																	

		#Creating a 2-Dimensional list for storing random integers
		for i in range(10):
			l=[]
			for j in range(10):
				l.append(str(randint(1,6)))
			self.matrix.append(l)
		
		root=Tk()
		root.geometry('500x750')
		root.resizable(0,0)
		root.title("Cleansweeper")

		self.canvas=Canvas(root,width=500,height=500)
		self.canvas.pack()

		#Top frame contains Buttons and Result 
		tframe=Frame(root)
		tframe.pack(side=TOP,pady=20)
		self.b1=Button(tframe,text='1',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(1))
		self.b2=Button(tframe,text='2',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(2))
		self.b3=Button(tframe,text='3',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(3))
		self.b4=Button(tframe,text='4',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(4))
		self.b5=Button(tframe,text='5',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(5))
		self.b6=Button(tframe,text='6',bg='black',fg='yellow',font='bold',command=lambda:self.checkbutton(6))
		
		self.b1.pack(side=LEFT,padx=22)
		self.b2.pack(side=LEFT,padx=22)
		self.b3.pack(side=LEFT,padx=22)
		self.b4.pack(side=LEFT,padx=22)
		self.b5.pack(side=LEFT,padx=22)
		self.b6.pack(side=LEFT,padx=22)

		self.displayres=Label(tframe,font='bold',fg='blue',bg='orange')

		#Left and Right frames contain labels to display player scores
		lframe=Frame(root)
		lframe.pack(side=LEFT,padx=40,pady=10)
		self.pl1=Label(lframe,text="Player 1 :   "+str(self.score["player1"]),font='bold',fg='green')
		self.pl1.pack()
		
		rframe=Frame(root)
		rframe.pack(side=RIGHT,padx=40,pady=10)
		self.pl2=Label(rframe,text=str(self.score["player2"])+"   : Player 2",font='bold',fg='brown')
		self.pl2.pack()
		
		for row in range(10):
			for col in range(10):
				x1,y1,x2,y2=row*50,col*50,50+row*50,50+col*50
				self.canvas.create_rectangle(x1,y1,x2,y2,fill='yellow')
				self.canvas.create_text((x1+25,y1+25),text='')

		root.mainloop()

	#Calculating player scores
	def game(self,p):

		self.count+=1
		if self.count%2==0:
			color='brown'
		elif self.count%2==1:
			color='green'
		for v in range(10):
			for j in range(10):
				if p == self.matrix[v][j]:
					self.canvas.create_rectangle(v*50,j*50,50+v*50,50+j*50,fill=color)
					self.canvas.create_text((v*50+25,j*50+25),text='')
					self.canvas.create_text((v*50+25,j*50+25),text=p,font='bold')
					if color=='green':
						self.score["player1"]+=1
					elif color=='brown':
						self.score["player2"]+=1
		
		self.pl1["text"]="Player 1:   "+str(self.score["player1"])
		self.pl1.pack()
		self.pl2["text"]=str(self.score["player2"])+"   : Player 2"
		self.pl2.pack()

		if self.count==6:
			self.finalresult()

	def finalresult(self):

		if self.score["player1"]>self.score["player2"]:
			self.result="Player 1 Wins"
		elif self.score["player1"]<self.score["player2"]:
			self.result="Player 2 Wins"
		else:
			self.result="Game is a Tie"
		self.displayres["text"]=self.result
		self.displayres.pack()


	def checkbutton(self,button_id):

		if button_id==1:
			self.b1.pack_forget()
			self.game('1')
		
		elif button_id==2:
			self.b2.pack_forget()
			self.game('2')
		
		elif button_id==3:
			self.b3.pack_forget()
			self.game('3')
		
		elif button_id==4:
			self.b4.pack_forget()
			self.game('4')
		
		elif button_id==5:
			self.b5.pack_forget()
			self.game('5')
		
		elif button_id==6:
			self.b6.pack_forget()
			self.game('6')


CleanSweeper()