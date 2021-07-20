import pygame
from pygame.locals import *
from Ball import Ball
class Snake(pygame.sprite.Sprite):
	"""docstring for Snake"""
	def __init__(self,head):
		super(Snake, self).__init__()
		self.body =[head]

	def getlen(self):
		return str(len(self.body))
	def update(self,newplace,colison,diraction,screen):
		a=[]
		if colison:

			if self.body[len(self.body)-1].diraction== None:
				self.body.append(Ball(self.get_new_place(diraction),diraction=diraction))
			else:
				self.body.append(Ball(self.get_new_place(self.body[len(self.body)-1].diraction),diraction=self.body[len(self.body)-1].diraction))

		else:
			saveplase=None
			savediraction=None
			
			for x in self.body:
				#a.append(x.diraction)
				if x.head:
					saveplase=x.place
					savediraction=diraction
					x.update(newplace,screen)

				else:

					if savediraction!=x.diraction:
						if (savediraction=='left' or savediraction=='right') and x.diraction=='up':
							x.place[1]-=0.25
							if  x.place[1]==saveplase[1] :
								x.diraction=savediraction
						elif (savediraction=='left' or savediraction=='right') and x.diraction=='down':
							x.place[1]+=0.25
							if  x.place[1]==saveplase[1] :
								x.diraction=savediraction
						elif (savediraction=='up' or savediraction=='down') and x.diraction=='left':
							x.place[0]-=0.25
							if  x.place[0]==saveplase[0] :
								x.diraction=savediraction
						elif (savediraction=='up' or savediraction=='down') and x.diraction=='right':
							x.place[0]+=0.25
							if  x.place[0]==saveplase[0] :
								x.diraction=savediraction
						elif (savediraction=='down' or savediraction=='up') and (x.diraction=='up' or x.diraction=='down'):
							if x.diraction=='down':
								x.place[1]+=0.25
							else:
								x.place[1]-=0.25
							if x.place[1]==saveplase[1]:
								if x.place[0]>saveplase[0]:
									x.diraction='left'
								else:
									x.diraction='right'

						
						elif (savediraction=='left' or savediraction=='right') and (x.diraction=='left' or x.diraction=='right'):
							if x.diraction=='left':
								x.place[0]-=0.25
							else:
								x.place[0]+=0.25
							if x.place[0]==saveplase[0]:
								if x.place[1]>saveplase[1]:
									x.diraction='up'
								else:
									x.diraction='down'


						
					else:
						if x.place[0]==saveplase[0]:
								if x.place[1]>saveplase[1]:
									x.diraction='up'
								else:
									x.diraction='down'
						if x.place[1]==saveplase[1]:
								if x.place[0]>saveplase[0]:
									x.diraction='left'
								else:
									x.diraction='right'
						if savediraction=='left':
							x.place[0]-=0.25
						elif savediraction=='right':
							x.place[0]+=0.25
						elif savediraction=='up':
							x.place[1]-=0.25
						elif savediraction=='down':
							x.place[1]+=0.25
					#temp=x.place
					#tempd=x.diraction
					#x.update(self.adjact_place(savediraction,saveplase),screen,savediraction)
					saveplase=x.place
					#savediraction=x.diraction
					x.draw(screen)
		#print(a)
	def get_new_place(self,diraction):
		x=None
		y=None
		if diraction=='left':

			x=self.body[len(self.body)-1].place[0]+self.body[len(self.body)-1].radios
			y=self.body[len(self.body)-1].place[1]
		elif diraction=='right':
			x=self.body[len(self.body)-1].place[0]-self.body[len(self.body)-1].radios
			y=self.body[len(self.body)-1].place[1]
		elif diraction=='up':
			x=self.body[len(self.body)-1].place[0]
			y=self.body[len(self.body)-1].place[1]+self.body[len(self.body)-1].radios
		elif diraction=='down':
			x=self.body[len(self.body)-1].place[0]
			y=self.body[len(self.body)-1].place[1]-self.body[len(self.body)-1].radios
		return [x,y]
	def checkcolision(self):
		for x in self.body:
			d=(x.place[0]-self.body[0].place[0])*(x.place[0]-self.body[0].place[0])+(x.place[1]-self.body[0].place[1])*(x.place[1]-self.body[0].place[1])
			if d<10 and d!=0:
				return True
				break
		return False
		




	