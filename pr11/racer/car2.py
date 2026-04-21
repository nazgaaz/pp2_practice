import pygame, sys
from pygame.locals import *
import random
import time

clock = pygame.time.Clock()

pygame.init()
width = 500
height = 700
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load("images/way.png")
bg = pygame.transform.scale(bg, (width, height))


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy_car.png")
        self.image = pygame.transform.scale(self.image, (80, 170))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, width - 50), 0)
        self.speed = 3

    def move_ecar(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.center = (random.randint(30, width - 30), 0)

    def draw_ecar(self):
        screen.blit(self.image, self.rect)


E1 = EnemyCar()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 4
        self.random_place()

    def random_place(self):
        self.rect.center = (random.randint(30, width - 30), 0)

    def move_coin(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.random_place()

    def draw_coin(self):
        screen.blit(self.image, self.rect)


C1 = Coin()


class BigCoin(Coin):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin_big.png")
        self.image = pygame.transform.scale(self.image, (80, 80))


C2 = BigCoin()


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load("images/car.png")
        self.image1 = pygame.transform.scale(self.image1, (120, 150))
        self.rect = self.image1.get_rect()
        self.rect.center = (width // 2, 620)

    def move_car(self, keys):
        if keys[K_LEFT] and self.rect.left > 10:
            self.rect.x -= 10
        if keys[K_RIGHT] and self.rect.right < width - 10:
            self.rect.x += 10

    def draw(self):
        screen.blit(self.image1, self.rect)


player_car = Car()
score = 0
last_speed_increase = 0
font = pygame.font.Font(None, 41)
flag = True

while flag:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

    E1.move_ecar()
    E1.draw_ecar()
    C1.draw_coin()
    C2.draw_coin()
    C1.move_coin()
    C2.move_coin()

    if player_car.rect.colliderect(C1.rect):
        score += 1
        C1.random_place()

    if player_car.rect.colliderect(C2.rect):
        score += 3
        C2.random_place()

    if score != last_speed_increase and (score > 11 and score > 16):
        E1.speed += 2
        last_speed_increase = score

    if player_car.rect.colliderect(E1.rect):
        h = pygame.image.load("images/game_over.jpeg")
        h = pygame.transform.scale(h, (width, height))
        screen.blit(h, (0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    keys = pygame.key.get_pressed()
    player_car.move_car(keys)
    player_car.draw()

    score_text = font.render(f"Score: {score}", True, (128, 52, 36))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)