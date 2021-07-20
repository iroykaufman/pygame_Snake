import pygame
from pygame.locals import *
import random as rd
from snake import Snake
from Ball import Ball
pygame.init() 
pygame.display.set_caption('Snake')
def game():
		
	#setting
	size=(800,600)
	backrond=(0,0,0)
	ballcolor=(0,255,0)

	screen=pygame.display.set_mode(size)
	ball_place=[400,300]
	run=True

	img=pygame.image.load("pythonimg.png")
	img=pygame.transform.scale(img,(50,50))

	img_rect= pygame.Rect((rd.randrange(50,650),rd.randrange(50,450)),(40,40))
	flag=True
	diraction='left'
	body=Snake(Ball(ball_place,head=True))

	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('1', True, (0, 255, 0))
	textRect = text.get_rect()
	textRect.center=(10,15)
	while run:
		if body.checkcolision() or ball_place[0]==0 or ball_place[0]==800 or ball_place[1]==0 or ball_place[1]==600:
			run=False
		colision=False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
		if pygame.key.get_pressed()[pygame.K_LEFT]==True:
			if ball_place[0]>0 and diraction!='right':
				diraction='left'
				flag=True
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
				if ball_place[0]<800 and diraction!='left':
					diraction='right'
					flag=True
		elif pygame.key.get_pressed()[pygame.K_UP]:
				if ball_place[1]>0 and  diraction!='down':
					diraction='up'
					flag=True
		elif pygame.key.get_pressed()[pygame.K_DOWN]:
				if ball_place[1]<600 and diraction!='up':
					diraction='down'
					flag=True


		if diraction=='left' and ball_place[0]>0:
			ball_place[0]-=0.25
		elif diraction=='right' and ball_place[0]<800 :
			ball_place[0]+=0.25
		elif diraction=='up' and ball_place[1]>0:
			ball_place[1]-=0.25
		elif diraction=='down' and ball_place[1]<600  :
			ball_place[1]+=0.25

		if img_rect.collidepoint(ball_place):
			colision=True
			img_rect= pygame.Rect((rd.randrange(50,700),rd.randrange(50,500)),(50,50))

		
		screen.fill(backrond)
		body.update(ball_place,colision,diraction,screen)
		screen.blit(img,img_rect)
		text = font.render(body.getlen(), True, (0, 255, 0))
		textRect = text.get_rect()
		textRect.center=(10,15)
		screen.blit(text,textRect)
			
		pygame.display.flip()
	return run

