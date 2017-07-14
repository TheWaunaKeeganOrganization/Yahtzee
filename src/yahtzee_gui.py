import pygame
from pygame.locals import *
import yahtzee_categories
import yahtzee_scorecard as ys
import yahtzee_interface as yi
import time
import sys
import os
import ctypes

user32 = ctypes.windll.user32
widthTotal, heightTotal = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def initWindowAt(x,y):
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()
initWindowAt(6,25)

screen_width = 1100
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])

diceList = [3,4,3,4,5]
player = 0 # 0: player, 1: AI
rolled = 0 # 0: able to roll, 1: not 
fontSmall=pygame.font.Font(None,20)

P1 = yi.Player()
scorecard = ys.Scorecard(P1)
scorecard.update("ones", [1,1,1,2,2])
scorecard.update("twos", [2,2,2,3,4])
scorecard.update("threes", [3,1,1,2,2])
scorecard.update("fours", [4,4,1,2,2])
#scorecard.update("fives", [5,1,1,2,2])
scorecard.update("sixes", [6,6,1,2,2])


board = pygame.image.load("resources/image/Board.png")
board = pygame.transform.scale(board,(screen_width,screen_height))
screen.blit(board,(0,0))

roll_dice=[]
roll_dice.append(pygame.transform.scale(pygame.image.load("resources/image/RollDice_able.png"),(204,48)))
roll_dice.append(pygame.transform.scale(pygame.image.load("resources/image/RollDice_disable.png"),(204,48)))

dice=[]
for i in range(1,7):
	img = pygame.image.load("resources/image/Dice_%d.png"%(i))
	img = pygame.transform.scale(img,(50,50))
	dice.append(img)

myfont = pygame.font.SysFont("comicsansms", 20)
# Set the height and width of the screen



while True:
	screen.blit(roll_dice[rolled],(280,610))

	for i in range(5):
		screen.blit(dice[i],(215+70*i,680))
	

	for i in range(6):
		key = scorecard.upperScoreKind[i]
		if scorecard.scores[key] != -1:
			text = myfont.render(str(scorecard.scores[key]),1,(0,0,0))
			screen.blit(text,(940+player*60,220+590/15.0*i))


	#if player==

	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

	pygame.display.flip()











'''
class Block(pygame.sprite.Sprite):
	"""
	This class represents the ball.
	It derives from the "Sprite" class in Pygame.
	"""
 
	def __init__(self, color, width, height):
		""" Constructor. Pass in the color of the block,
		and its x and y position. """
 
		# Call the parent class (Sprite) constructor
		super(Block,self).__init__()
 
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
 
		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()
 
# Initialize Pygame

 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
end_list = pygame.sprite.Group()
 

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
start=time.time()
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True
 
	# Clear the screen
	screen.fill(WHITE)
	#text=fontSmall.render(str(time.time-start),1,(0,0,0))
	#textpos=text.get_rect()
	#textpos.centerx=
 
	# Get the current mouse position. This returns the position
	# as a list of two numbers.
	pos = pygame.mouse.get_pos()
 
	# Fetch the x and y out of the list,
	   # just like we'd fetch letters out of a string.
	# Set the player object to the mouse location
	player.rect.x = pos[0]
	player.rect.y = pos[1]
 
	# See if the player block has collided with anything.
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
	
	# Check the list of collisions.

	if pygame.sprite.collide_rect(end,player):
		game=False
		end=pygame.image.load("end.jpg")
		end=pygame.transform.scale(end,(150,80))
		endrect=end.get_rect()
		endrect.x=30
		endrect.y=150        
		screen.blit(end,endrect)

		while not game:
			all_sprites_list.draw(screen)
			pygame.display.flip()
			clock.tick(60)

			pos = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type==pygame.MOUSEBUTTONUP and endrect.left<pos[0]<endrect.right and endrect.top<pos[1]<endrect.bottom:
					end = Block((0,0,255), 25, 25)
					end.rect.x = 650
					end.rect.y = 350
					end_list.add(end)
					all_sprites_list.add(end)
					start=time.time()
					game=True
				if event.type == pygame.QUIT: 
					sys.exit()
		

	for block in blocks_hit_list:
		game=False
		restart=pygame.image.load("restart.jpg")
		restart=pygame.transform.scale(restart,(150,80))
		restartrect=restart.get_rect()
		restartrect.x=30
		restartrect.y=150        
		screen.blit(restart,restartrect)

		while not game:
			all_sprites_list.draw(screen)
			pygame.display.flip()
			clock.tick(60)

			pos = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type==pygame.MOUSEBUTTONUP and restartrect.left<pos[0]<restartrect.right and restartrect.top<pos[1]<restartrect.bottom:
					start=time.time()
					game=True
				if event.type == pygame.QUIT: 
					sys.exit()

	# Draw all the spites
	all_sprites_list.draw(screen)
 
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# Limit to 60 frames per second
	clock.tick(60)

pygame.quit()
'''