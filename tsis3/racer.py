import pygame
import random
from datetime import datetime


WIDTH = 420
HEIGHT = 700

ROAD_X = 60
ROAD_W = 300
LANES = 3
LANE_W = ROAD_W // LANES

BG = (224, 244, 255)
ROAD = (242, 247, 255)
LANE = (255, 255, 255)
HUD = (30, 60, 110)

WHEEL = (50, 60, 80)

DIFF = {
    "easy": {"speed": 200, "finish": 3000, "traffic_ms": 1900, "obstacle_ms": 2400},
    "normal": {"speed": 240, "finish": 4200, "traffic_ms": 1500, "obstacle_ms": 1900},
    "hard": {"speed": 290, "finish": 5200, "traffic_ms": 1100, "obstacle_ms": 1500}
}

CAR_COLORS = {
    "red": ((220, 80, 80), (255, 160, 160)),
    "blue": ((100, 180, 255), (180, 230, 255)),
    "green": ((80, 220, 140), (160, 255, 200)),
    "yellow": ((240, 220, 80), (255, 250, 160))
}


def lane_x(lane):
    return ROAD_X + lane * LANE_W + LANE_W // 2


def img(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(image, size)


class RacerGame:
    def __init__(self, screen, settings, username):
        self.screen = screen
        self.settings = settings
        self.username = username

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 19)

        d = DIFF[settings["difficulty"]]

        self.base_speed = d["speed"]
        self.finish = d["finish"]
        self.traffic_interval = d["traffic_ms"]
        self.obs_interval = d["obstacle_ms"]

        self.distance = 0
        self.score = 0
        self.coins = 0

        self.player_lane = 1
        self.player_y = 590

        self.running = True
        self.result_status = "game_over"

        self.road_offset = 0

        self.active_power = None
        self.power_until = 0
        self.shield = False

        self.slow_until = 0
        self.speed_mult = 1

        self.player_w = 56
        self.player_h = 92

        self.car_color = settings["car_color"]

        self.enemy = img("assets/Enemyy.png", (55, 88))
        self.coin = img("assets/coinn.png", (34, 34))
        self.shield_img = img("assets/shield.png", (36, 36))
        self.heal_img = img("assets/heal.png", (36, 36))
        self.boost_img = img("assets/boost.png", (36, 36))
        self.oil_img = img("assets/oil.png", (42, 28))

        self.traffic = []
        self.obstacles = []
        self.coin_list = []
        self.powerups = []

        self.last_traffic = 0
        self.last_obs = 0
        self.last_coin = 0
        self.last_power = 0

    def player_rect(self):
        rect = pygame.Rect(0, 0, self.player_w, self.player_h)
        rect.center = (lane_x(self.player_lane), self.player_y)
        return rect

    def draw_player(self):
        car = self.player_rect()

        base, light = CAR_COLORS[self.car_color]

        pygame.draw.rect(self.screen, base, car, border_radius=18)

        top = pygame.Rect(car.x + 10, car.y + 14, car.w - 20, 26)
        pygame.draw.rect(self.screen, light, top, border_radius=10)

        for y in [car.y + 18, car.y + 60]:
            pygame.draw.circle(self.screen, WHEEL, (car.x + 6, y), 7)
            pygame.draw.circle(self.screen, WHEEL, (car.right - 6, y), 7)

        pygame.draw.circle(self.screen, (255, 255, 220), (car.centerx - 10, car.y + 10), 4)
        pygame.draw.circle(self.screen, (255, 255, 220), (car.centerx + 10, car.y + 10), 4)

        if self.shield:
            pygame.draw.circle(self.screen, (150, 220, 255), car.center, 44, 4)

    def current_speed(self):
        now = pygame.time.get_ticks()
        mult = self.speed_mult

        if now < self.slow_until:
            mult *= 0.7

        return self.base_speed * mult

    def activate(self, power_type):
        if self.active_power and power_type != "repair":
            return

        now = pygame.time.get_ticks()

        if power_type == "nitro":
            self.active_power = "nitro"
            self.power_until = now + 4000
            self.speed_mult = 1.6

        elif power_type == "shield":
            self.active_power = "shield"
            self.shield = True

        elif power_type == "repair":
            if self.obstacles:
                self.obstacles.pop(0)
            self.coins += 2

    def clear_power(self):
        self.active_power = None
        self.shield = False
        self.speed_mult = 1

    def safe_lane(self):
        lanes = [0, 1, 2]
        lanes.remove(self.player_lane)
        return random.choice(lanes)

    def spawn_traffic(self):
        if len(self.traffic) >= 2:
            return

        rect = self.enemy.get_rect()
        lane = self.safe_lane()

        rect.centerx = lane_x(lane)
        rect.y = -100

        self.traffic.append(rect)

    def spawn_obstacle(self):
        if len(self.obstacles) >= 2:
            return

        lane = self.safe_lane()

        rect = self.oil_img.get_rect()
        rect.centerx = lane_x(lane)
        rect.y = -60

        kind = random.choice(["oil", "bump"])

        self.obstacles.append({
            "rect": rect,
            "type": kind
        })

    def spawn_coin(self):
        rect = self.coin.get_rect()

        rect.centerx = lane_x(random.randint(0, 2))
        rect.y = -40

        self.coin_list.append(rect)

    def spawn_power(self):
        kind = random.choice(["nitro", "shield", "repair"])

        rect = pygame.Rect(0, 0, 36, 36)
        rect.centerx = lane_x(random.randint(0, 2))
        rect.y = -40

        self.powerups.append({
            "type": kind,
            "rect": rect,
            "born": pygame.time.get_ticks()
        })

    def update(self, dt):
        now = pygame.time.get_ticks()

        if self.active_power == "nitro" and now > self.power_until:
            self.clear_power()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player_lane = max(0, self.player_lane - 1)

        if keys[pygame.K_RIGHT]:
            self.player_lane = min(2, self.player_lane + 1)

        if now - self.last_traffic > self.traffic_interval:
            self.spawn_traffic()
            self.last_traffic = now

        if now - self.last_obs > self.obs_interval:
            self.spawn_obstacle()
            self.last_obs = now

        if now - self.last_coin > 900:
            self.spawn_coin()
            self.last_coin = now

        if now - self.last_power > 6500:
            self.spawn_power()
            self.last_power = now

        self.powerups = [
            pwr for pwr in self.powerups
            if now - pwr["born"] < 5000
        ]

        speed = self.current_speed()

        self.distance += speed * dt / 17

        self.road_offset = (self.road_offset + speed * dt * 0.45) % 60

        player = self.player_rect()

        for traffic_car in self.traffic:
            traffic_car.y += speed * dt

        for obstacle in self.obstacles:
            obstacle["rect"].y += speed * dt

        for coin in self.coin_list:
            coin.y += speed * dt

        for powerup in self.powerups:
            powerup["rect"].y += speed * dt

        self.traffic = [t for t in self.traffic if t.y < HEIGHT]
        self.obstacles = [o for o in self.obstacles if o["rect"].y < HEIGHT]
        self.coin_list = [c for c in self.coin_list if c.y < HEIGHT]

        for coin in list(self.coin_list):
            if player.colliderect(coin):
                self.coins += random.choice([1, 2, 3])
                self.coin_list.remove(coin)

        for powerup in list(self.powerups):
            if player.colliderect(powerup["rect"]):
                self.activate(powerup["type"])
                self.powerups.remove(powerup)

        for traffic_car in self.traffic:
            if player.colliderect(traffic_car):
                if self.shield:
                    self.clear_power()
                    traffic_car.y = 900
                else:
                    self.running = False

        for obstacle in list(self.obstacles):
            if player.colliderect(obstacle["rect"]):
                if obstacle["type"] == "oil":
                    self.player_lane = max(
                        0,
                        min(2, self.player_lane + random.choice([-1, 1]))
                    )
                else:
                    self.slow_until = now + 1200

                self.obstacles.remove(obstacle)

        self.score = int(self.coins * 15 + self.distance)

        if self.distance >= self.finish:
            self.running = False
            self.result_status = "finished"

    def draw(self):
        self.screen.fill(BG)

        pygame.draw.rect(self.screen, ROAD, (ROAD_X, 0, ROAD_W, HEIGHT))

        for i in range(1, 3):
            x = ROAD_X + i * LANE_W
            y = -60 + int(self.road_offset)

            while y < HEIGHT:
                pygame.draw.line(self.screen, LANE, (x, y), (x, y + 35), 5)
                y += 60

        for coin in self.coin_list:
            self.screen.blit(self.coin, coin)

        for obstacle in self.obstacles:
            self.screen.blit(self.oil_img, obstacle["rect"])

        for traffic_car in self.traffic:
            self.screen.blit(self.enemy, traffic_car)

        for powerup in self.powerups:
            if powerup["type"] == "nitro":
                self.screen.blit(self.boost_img, powerup["rect"])
            elif powerup["type"] == "shield":
                self.screen.blit(self.shield_img, powerup["rect"])
            else:
                self.screen.blit(self.heal_img, powerup["rect"])

        self.draw_player()

        power = "None"

        if self.active_power == "nitro":
            left = max(0, (self.power_until - pygame.time.get_ticks()) / 1000)
            power = f"Nitro {left:.1f}s"

        elif self.active_power == "shield":
            power = "Shield"

        left_distance = max(0, int(self.finish - self.distance))

        hud = [
            f"{self.username}",
            f"Coins {self.coins}",
            f"Score {self.score}",
            f"Dist {int(self.distance)}",
            f"Left {left_distance}",
            f"Power {power}"
        ]

        for i, text in enumerate(hud):
            self.screen.blit(
                self.font.render(text, True, HUD),
                (12, 12 + i * 24)
            )

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return {"quit": True}

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.update(dt)
            self.draw()

        return {
            "quit": False,
            "status": self.result_status,
            "username": self.username,
            "score": self.score,
            "coins": self.coins,
            "distance": int(self.distance),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }