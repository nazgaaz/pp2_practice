import pygame
import random
import sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

width = 500
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")

road_color = (50, 50, 50)
line_color = (255, 255, 255)
player_color = (0, 100, 255)
enemy_color = (200, 0, 0)
coin_color = (255, 215, 0)
big_coin_color = (255, 140, 0)
text_color = (255, 255, 255)

font = pygame.font.Font(None, 40)

score = 0
N = 5
last_speed_increase = 0
flag = True


class EnemyCar:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(80, width - 140), 0, 70, 120)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.x = random.randint(80, width - 140)
            self.rect.y = -120

    def draw(self):
        pygame.draw.rect(screen, enemy_color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 10, self.rect.y + 15, 15, 25))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 45, self.rect.y + 15, 15, 25))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 10, self.rect.y + 80, 15, 25))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 45, self.rect.y + 80, 15, 25))


class Coin:
    def __init__(self):
        self.radius = 18
        self.value = 1
        self.speed = 4
        self.x = random.randint(80, width - 80)
        self.y = 0

    def random_place(self):
        self.x = random.randint(80, width - 80)
        self.y = -self.radius

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.random_place()

    def draw(self):
        pygame.draw.circle(screen, coin_color, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)


class BigCoin(Coin):
    def __init__(self):
        super().__init__()
        self.radius = 28
        self.value = 3

    def draw(self):
        pygame.draw.circle(screen, big_coin_color, (self.x, self.y), self.radius)


class PlayerCar:
    def __init__(self):
        self.rect = pygame.Rect(width // 2 - 40, 560, 80, 120)
        self.speed = 10

    def move(self, keys):
        if keys[K_LEFT] and self.rect.left > 60:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < width - 60:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, player_color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 10, self.rect.y + 15, 20, 30))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 50, self.rect.y + 15, 20, 30))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 10, self.rect.y + 80, 20, 30))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 50, self.rect.y + 80, 20, 30))


def draw_road():
    screen.fill((30, 160, 30))
    pygame.draw.rect(screen, road_color, (50, 0, 400, height))

    for y in range(0, height, 80):
        pygame.draw.rect(screen, line_color, (245, y, 10, 40))


def game_over():
    screen.fill((0, 0, 0))
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (160, 320))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


enemy = EnemyCar()
coin = Coin()
big_coin = BigCoin()
player = PlayerCar()

while flag:
    draw_road()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    enemy.move()
    enemy.draw()

    coin.move()
    coin.draw()

    big_coin.move()
    big_coin.draw()

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()

    if player.rect.colliderect(coin.get_rect()):
        score += coin.value
        coin.random_place()

    if player.rect.colliderect(big_coin.get_rect()):
        score += big_coin.value
        big_coin.random_place()

    if score // N > last_speed_increase:
        enemy.speed += 1
        last_speed_increase = score // N

    if player.rect.colliderect(enemy.rect):
        game_over()

    score_text = font.render(f"Score: {score}", True, text_color)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)