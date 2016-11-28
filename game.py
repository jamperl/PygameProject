import pygame
from pygame import *
from pygame.sprite import *
import random

screen_width = 640
screen_height = 500

white = (255, 255, 255)
red = (255, 0, 0)

class Jabrill(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 80
		self.height = 130

		self.image = pygame.image.load("jabrill.bmp")
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = Rect(0, 130, screen_width, screen_height)
		self.rect.centerx = screen_width/2
		self.rect.bottom = screen_height - 5

		self.speed = 1
		self.lives = 3

	def update(self):
		keys = pygame.key.get_pressed()

		if key[K_LEFT]:
			self.left -= 15
		if key[K_RIGHT]:
			self.right += 15
		if key[K_SPACE]:
			self.shoot()

		if self.right > screen_width:
			self.right = screen_width
		if self.left < 0:
			self.left = 0

	# def shoot(self):
	# 	bullet = Helmet(self.centerx, self.top)

pygame.init()

big_house = pygame.image.load("field.bmp")
pygame.transform.scale(big_house, (screen_width, screen_height))

pygame.display.set_caption("Champions of the West")

pygame.quit()
