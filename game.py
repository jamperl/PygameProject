import pygame
from pygame import *
from pygame.sprite import *
from pygame.locals import *
import random
import sys

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 675
WHITE = (255, 255, 255)

finalscore_x = 200
finalscore_y = (WINDOW_HEIGHT/2) - 75
gameover_x = 320
gameover_y = finalscore_y + 100

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
big_house = pygame.image.load('field.bmp')
big_house = pygame.transform.scale(big_house, (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Champions of the West")

myfont = pygame.font.SysFont("helvetica", 30, bold=True)
myfont2 = pygame.font.SysFont("helvetica", 60, bold=True)


pygame.mixer.music.load('hail2.mp3')
pygame.mixer.music.play(loops= -1)

class Jabrill(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 95
		self.height = 140

		self.image = pygame.image.load('jabrill.bmp')
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()
		self.rect.centerx = WINDOW_WIDTH/2
		self.rect.bottom = WINDOW_HEIGHT - 15

		self.lives = 3
		self.score = 0

	def update(self):
		keys = pygame.key.get_pressed()

		self.horiz = 0
		
		if keys[K_LEFT]:
			self.horiz -= 15
		if keys[K_RIGHT]:
			self.horiz += 15
		if keys[K_SPACE] and len(helmets) < 10:
			self.shoot()
			

		self.rect.x += self.horiz

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > WINDOW_WIDTH:
			self.rect.right = WINDOW_WIDTH

	def shoot(self):
		helmet = Helmet(self.rect.centerx, self.rect.top)
		sprites_list.add(helmet)
		helmets.add(helmet)


class Rival(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.width = 40
		self.height = 45

		self.school_pics = ['osu.bmp', 'msu.bmp', 'psu.bmp', 'minn.bmp', 'nebrask.bmp', 'wisco.bmp', 'north.bmp', 'mary.bmp', 'pur.bmp', 'iu.bmp', 'ill.bmp', 'iowa.bmp']
		self.new_school_pics = []
		for pic in self.school_pics:
			self.image = pygame.image.load(pic)
			self.new_school_pics.append(self.image)

		self.image = random.choice(self.new_school_pics)
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		self.rect = self.image.get_rect()

		self.rect.y = -20
		self.rect.x = random.randrange(0, (WINDOW_WIDTH - self.rect.width))
		self.vert = random.randrange(4, 9)

	def update(self):
		self.rect.y += self.vert
		if self.rect.top > WINDOW_HEIGHT - 5:
			self.rect.y = -20
			self.rect.x = random.randrange(0, (WINDOW_WIDTH - self.rect.width))
			self.vert = random.randrange(4, 12)

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
		self.vert = -4

	def update(self):
		self.rect.y += self.vert
		if self.rect.y > WINDOW_HEIGHT + 5:
			helmets.remove(self)
		

sprites_list = pygame.sprite.Group()
jabrill = Jabrill()
sprites_list.add(jabrill)

schools = pygame.sprite.Group()
for x in range(15):
		rival = Rival()
		sprites_list.add(rival)
		schools.add(rival)

helmets = pygame.sprite.Group()

game_exit = False
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		elif event.type == pygame.KEYDOWN:
			if event.key == K_RETURN:
				done = True

	if not game_exit:
		sprites_list.update()
		
		for helmet in helmets:
			collisions = pygame.sprite.groupcollide(schools, helmets, True, True)
			if collisions:
				helmets.remove(helmet)
				jabrill.score += 100
		if len(schools) < 14:
			rival = Rival()
			sprites_list.add(rival)
			schools.add(rival)
		jabrill_lives = pygame.sprite.spritecollide(jabrill, schools, True)	
		if jabrill_lives:
			jabrill.lives -= 1

		if jabrill.lives < 1:
			game_exit = True

		life_count = myfont.render('Lives: ' + str(jabrill.lives), 1, WHITE)
		score_count = myfont.render('Score: ' + str(jabrill.score), 1, WHITE)
		screen.blit(big_house, (0,0))
		sprites_list.draw(screen)
		screen.blit(life_count, (20, 20))
		screen.blit(score_count, (WINDOW_WIDTH - 220, 20))

	else:
		harbaugh = pygame.image.load('harbaugh.bmp')
		harbaugh = pygame.transform.scale(harbaugh, (WINDOW_WIDTH, WINDOW_HEIGHT))
		game_over = myfont.render('HIT RETURN TO EXIT', 1, WHITE)
		update_score = myfont2.render('FINAL SCORE: ' + str(jabrill.score), 1, WHITE)
		screen.blit(harbaugh, (0,0))
		screen.blit(update_score, (finalscore_x, finalscore_y))
		screen.blit(game_over, (gameover_x, gameover_y))

	pygame.display.flip()
	
pygame.quit()
