import pygame
from pygame import *
from pygame.sprite import *
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
big_house = pygame.image.load("field.bmp")
pygame.transform.scale(big_house, (WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Champions of the West")

class Jabrill(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 130

		self.pic = pygame.image.load("jabrill.bmp")
		self.pic = pygame.transform.scale(self.pic, (self.width, self.height))

		self.rect = self.pic.get_rect()
		self.rect.centerx = WINDOW_WIDTH/2
		self.rect.bottom = WINDOW_HEIGHT - 5

		self.horiz = 0
		self.lives = 1

	def update(self):
		keys = pygame.key.get_pressed()

		slide = 15
		if key[K_LEFT]:
			self.horiz = (-1) * slide
		if key[K_RIGHT]:
			self.horiz = slide
		if key[K_SPACE]:
			self.shoot()

		self.rect.pos += self.horiz

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > WINDOW_WIDTH:
			self.rect.right = WINDOW_WIDTH

	# def shoot(self):
	# 	bullet = Helmet(self.centerx, self.top)

class Rival(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 60
		self.height = 95

		self.school_pics = ['osu.bmp', 'msu.bmp']
		self.new_school_pics = []
		for pic in self.school_pics:
			self.img = pygame.image.load(pic)
			self.img = pygame.transform.scale(self.pic, (self.width, self.height))
			self.new_school_pics.append(self.img)

		self.pic = random.choice(self.new_school_pics)
		self.rect = self.pic.get_rect()




sprites_list = pygame.sprite.Group()
jabrill = Jabrill()
sprites_list.add(jabrill)

#schools, helmets = pygame.sprite.Group()
# for x in range(8):
# 	rival = Rival()
# 	sprites_list.add(rival)
# 	schools.add(rival)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

	sprites_list.update()

	pygame.display.flip()

pygame.quit()
quit()
