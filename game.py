import pygame
from pygame import *
from pygame.sprite import *
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 500

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
big_house = pygame.image.load('field.bmp')
big_house = pygame.transform.scale(big_house, (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Champions of the West")

class Jabrill(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 130

		self.image = pygame.image.load('jabrill.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = WINDOW_WIDTH/2
		self.rect.bottom = WINDOW_HEIGHT - 5


	def update(self):
		keys = pygame.key.get_pressed()

		self.horiz = 0
		
		if keys[K_LEFT]:
			self.horiz -= 15
		if keys[K_RIGHT]:
			self.horiz += 15
		if keys[K_SPACE]:
			self.shoot()

		self.rect.x += self.horiz

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > WINDOW_WIDTH:
			self.rect.right = WINDOW_WIDTH

	def shoot(self):
		helmet = Helmet(self.rect.centerx, self.rect.top)
		sprites_list.add(helmet)


class Rival(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 40
		self.height = 45

		self.school_pics = ['osu.bmp', 'msu.bmp', 'psu.bmp', 'minn.bmp', 'nebrask.bmp', 'wisco.bmp']
		self.new_school_pics = []
		for pic in self.school_pics:
			self.image = pygame.image.load(pic)
			self.image = pygame.transform.scale(self.image, (self.width, self.height))
			self.new_school_pics.append(self.image)

		self.image = random.choice(self.new_school_pics)
		self.rect = self.image.get_rect()

		self.rect.y = -20
		self.rect.x = random.randrange(0, (WINDOW_WIDTH - self.rect.width))
		self.vert = random.randrange(1, 13)

	def update(self):
		self.rect.y += self.vert
		if self.rect.top > WINDOW_HEIGHT - 5:
			self.rect.y = -20
			self.rect.x = random.randrange((0 + self.rect.width), (WINDOW_WIDTH - self.rect.width))
			self.vert = random.randrange(3, 10)

class Helmet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.width = 25
		self.height = 25

		self.image = pygame.image.load('mich.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.top = y
		self.vert = -2

	def update(self):
		self.rect.y += self.vert



sprites_list = pygame.sprite.Group()
jabrill = Jabrill()
sprites_list.add(jabrill)

schools = pygame.sprite.Group()
for x in range(8):
	rival = Rival()
	sprites_list.add(rival)
	schools.add(rival)

helmets = pygame.sprite.Group()

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	sprites_list.update()
	screen.blit(big_house, (0,0))
	sprites_list.draw(screen)

	pygame.display.flip()
pygame.quit()
quit()
