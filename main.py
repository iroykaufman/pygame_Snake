import pygame
from pygame.locals import *
from Snake_game import game

pygame.init() 
pygame.display.set_caption('Snake')
#setting
size=(800,600)
backrond=(0,0,0)
ballcolor=(0,255,0)

screen=pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 64)

text1 = font.render('--click to play--', True, (0, 255, 0))
textRect1 = text1.get_rect()
textRect1.center=(400,500)


text2 = font.render('Snake', True, (0, 255, 0))
textRect2 = text2.get_rect()
textRect2.center=(400,100)

run=True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

		if event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
			if(game()==False):
				text1 = font.render('--click to play again--', True, (0, 255, 0))
				textRect1 = text1.get_rect()
				textRect1.center=(400,500)


	screen.fill(backrond)
	screen.blit(text1,textRect1)
	screen.blit(text2,textRect2)
	pygame.display.flip()
			






























