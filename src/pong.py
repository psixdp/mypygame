#coding=utf-8

#This script is used to monitor a Pong-game

import pygame
from pygame.locals import *
from sys import exit


srcdir='../res'
# class table(object)
# 	width=640
# 	height=480
# 	color=(0,0,0)
# 	def __init__(self,width,height,color):
# 		self.width=width
# 		self.height=height
# 		self.color=color
# 	def drawtable(self):
class paddle(object):
	width=5
	height=20
	pos_y=240
	color=(0,0,0)
	pos_x=635
	def __init__(self,width,height,pos_y,color,ismine):
		self.width=width
		self.height=height
		self.pos_y=pos_y
		self.color=color
		if ismine:
			self.pos_x=640-width
		if not ismine:
			self.pos_x=0
	def move(self,direction):
		if direction==1:
			self.pos_y=max(0,self.pos_y-1)
		elif direction==-1:
			self.pos_y=min(480-self.height,self.pos_y+1)
			# print self.pos_y
		# elif direction=='stay':
			# self.pos_y=self.pos_y
class ball(object):
	speed_x=1
	speed_y=1
	radius=10
	pos_x=320
	pos_y=240
	color=(255,255,255)
	def __init__(self,radius,pos_x,pos_y,color,speed_x,speed_y):
		self.radius=radius
		self.pos_x=pos_x
		self.pos_y=pos_y
		self.color=color
		self.speed_x=speed_x
		self.speed_y=speed_y

	def move(self,move_x,move_y,bounce):
		if bounce:
			if self.pos_x+move_x<=640-self.radius and self.pos_x+move_x>=0:
				self.pos_x+=move_x
			elif self.pos_x+move_x>640-self.radius:
				self.pos_x=640-(self.pos_x+move_x-640)
				self.speed_x=-self.speed_x
			elif self.pos_x+move_x<0:
				self.pos_x=-(self.pos_x+move_x)
				self.speed_x=-self.speed_x
		if not bounce:
			self.pos_x+=move_x
		#posy:
		if self.pos_y+move_x<=480-self.radius and self.pos_y+move_x>=0:
			self.pos_y+=move_y
		elif self.pos_y+move_x>480-self.radius:
			self.pos_y=480-(self.pos_y+move_y-480)
			self.speed_y=-self.speed_y
		elif self.pos_y+move_x<0:
			self.pos_y=-(self.pos_y+move_y)
			self.speed_y=-self.speed_y
if __name__=='__main__':
	#init the table
	# table=table.init()
	pygame.init()
	mypad=paddle(10, 80, 240,(255,255,255), True)
	screen=pygame.display.set_mode((640,480))
	direction=0
	# ball=pygame.image.load(srcdir+'/pongball.png').convert_alpha()
	myball=ball(5,320,240,(255,255,255),1,1)
	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			if event.type==KEYDOWN:
				if event.key==K_ESCAPE:
					exit()
				# mypad.move(event)
				elif event.key==K_UP:
					direction=1
				elif event.key==K_DOWN:
					direction=-1
			elif event.type==KEYUP:
				direction=0

	#绘制桌面背景
		# table_surface=pygame.Surface((640,480))
		# screen.blit(table_surface,(0,0))
		screen.fill((0,0,0))
	#更新球拍位置
		mypad.move(direction)
	#更新球
		myball.move(myball.speed_x, myball.speed_y, True)
		
		pygame.draw.rect(screen,mypad.color,(mypad.pos_x,mypad.pos_y,mypad.width,mypad.height))
		pygame.draw.circle(screen,myball.color,(myball.pos_x,myball.pos_y),myball.radius)
		pygame.display.update()





