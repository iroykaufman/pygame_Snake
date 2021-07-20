import pygame
from pygame.locals import *
class Ball(pygame.sprite.Sprite):

 	"""docstring for Ball"""
 	def __init__(self, place,color=(0,255,0),head=False,radios=10,diraction=None):
 		self.place = place
 		self.color=color
 		self.radios=radios
 		self.head=head
 		self.diraction=diraction
 	def update(self,place,screen=None,diraction=None):
 		self.place=place
 		self.diraction=diraction
 		if screen!=None:
 			self.draw(screen)

 	def draw(self,screen):
 		pygame.draw.circle(screen,self.color,self.place,self.radios)
