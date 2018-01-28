import time as t
from pygame import *
import numpy as np
from random import *
from textbox import TextBox
import webbrowser

green=(0,255,0)
greengrass=(1,166,17)
black=(0,0,0)
white=(255,255,255)
bluesky=(135,206,235)
red=(255,5,5)
bloodred=(138,7,7)
blue=(0,0,255)
darkblue=(0,0,139)

colors= [ [ green,bluesky,red], [bloodred,greengrass,darkblue], [white,blue,black] ]

res=[800,590]

init()
window=display.set_mode(res)
clock = time.Clock()




class Button(object):
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",36)
		self.act=False
		
	def event(self,game):
		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			game.new()

		
	def click(self):
		if mouse.get_pressed()[0]:
			if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
				return True

	def draw(self):

		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),1)
		else:
			draw.rect(window,white,Rect(self.x,self.y,self.w,self.h),1)
		text = self.Font.render(self.text,True,white)
		window.blit(text,(self.x+5,self.y+5))


class CheckButton(object):
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",36)
		self.act=False
		
	def event(self, board,game):
		good=True
		counter=0
		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:			
			for i in range(9):
				for k in range(9):
					if str(board[i][k].final)!="":
						for j in range(k+1,9):
							if board[i][k].final==board[i][j].final:
								good=False
				for k in range(9):
					if str(board[k][i].final)!="":
						for j in range(k+1,9):
							if board[k][i].final==board[j][i].final:
								good=False
								
			game.good = good
			
			for i in range(9):
				for j in range(9):
					if str(board[i][j].final)!="":
						counter=counter+1
			if counter==81:
				game.full=True
			

		
	def click(self):
		if mouse.get_pressed()[0]:
			if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
				return True

	def draw(self):

		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),1)
		else:
			draw.rect(window,white,Rect(self.x,self.y,self.w,self.h),1)
		text = self.Font.render(self.text,True,white)
		window.blit(text,(self.x+5,self.y+5))


def nic (a, b):
	pass



class Game(object):
	def __init__(self):
		self.good=True
		self.full=False
		self.board=[]
		self.Font=font.SysFont("arial",36)
		for i in range(9):
			tmp = []
			for j in range(9):
				tmp.append(TextBox((i*60+25,j*60+25,45,45),command=nic,clear_on_enter=True,inactive_on_enter=False,active=False))
			self.board.append(tmp)



		file=open("sud001.dat")

		for i in range(9):
			line=file.readline()
			for j in range(9):
				if line[j]!='0':
					self.board[i][j].buffer = [line[j]]
					self.board[i][j].act=False
					
	
	def draw(self):
		for i in range(3):
			for j in range(3):
				draw.rect(window,colors[i][j],Rect(20+i*180,20+j*180,175,175),0)
	
		for a in self.board:
			for b in a:
				#if b.act:
				b.update()
				b.draw(window)
		if not self.good:
			text = self.Font.render("Mistake",True,red)
			window.blit(text,(600,500))
		elif self.good and self.full:
			text = self.Font.render("You win!",True,green)
			window.blit(text,(600,500))
			
	def new(self):
		self.good=True
		self.full=False
		self.board=[]
		self.Font=font.SysFont("arial",36)
		for i in range(9):
			tmp = []
			for j in range(9):
				tmp.append(TextBox((i*60+25,j*60+25,45,45),command=nic,clear_on_enter=True,inactive_on_enter=False,active=False))
			self.board.append(tmp)



		file=open("sud001.dat")

		for i in range(9):
			line=file.readline()
			for j in range(9):
				if line[j]!='0':
					self.board[i][j].buffer = [line[j]]

game=Game()
end=False

newgame=Button(570,100,180,50,"New game")
check=CheckButton(570,300,180,50,"Check")

while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
		if zet.type==MOUSEBUTTONUP:
			newgame.event(game)
			check.event(game.board,game)
			#s.event()
			#timer.event(timerbox.final)
		#timerbox.get_event(zet)
		for a in game.board:
			for b in a:
				b.get_event(zet)

		
	window.fill(black)
	newgame.draw()
	check.draw()
	game.draw()

	
	#timerbox.update()
	#timerbox.draw(window)

	clock.tick(20)
	display.flip()