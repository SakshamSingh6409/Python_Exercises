'''
This is a simple 2D game using Pygame where a player can move around
An NPC will follow him
With terrain generation
'''

import pygame
import time
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()
dt = 0

# Player Properties
PLAYER_COLOR = "blue"
PLAYER_SPEED = 300
PLAYER_SIZE = (10, 10)

# NPC Properties
NPC_COLOR = "white"
NPC_SPEED = 100
NPC_SIZE = (10, 10)

# Bullet Properties
BULLET_COLOR = "red"
BULLET_SPEED = 500
BULLET_SIZE = (5, 5)

# Terrain Properties
TERRAIN_COLOR = "green"
NUM_TERRAINS = 10
TERRAIN_SIZE = (40, 40)

# Create Vector2 position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
npc_pos = pygame.Vector2(0, 0)
draw_player = True
running = True
start_time = time.time()

# Store bullets and terrain
bullets = []
terrain_list = []


class NPC:
    def __init__(self, color, speed, size):
        self.color = color
        self.speed = speed
        self.size = size
        self.pos = self.random_position()

    def random_position(self):
        return pygame.Vector2(random.randint(0, screen.get_width() - self.size[0]),
                              random.randint(0, screen.get_height() - self.size[1]))

    def move_towards(self, target_pos, dt):
        direction = target_pos - self.pos
        if direction.length() != 0:
            direction = direction.normalize()
            self.pos += direction * self.speed * dt

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (*self.pos, *self.size))

    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.size[0], self.size[1])


def handle_player_movement(keys, pos, speed, dt):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        pos.y -= speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        pos.y += speed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        pos.x -= speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        pos.x += speed * dt


def generate_terrain():
    for _ in range(NUM_TERRAINS):
        x = random.randint(0, screen.get_width() - TERRAIN_SIZE[0])
        y = random.randint(0, screen.get_height() - TERRAIN_SIZE[1])
        terrain_list.append(pygame.Rect(x, y, *TERRAIN_SIZE))


def shoot_bullet():
    bullet_pos = pygame.Vector2(player_pos.x + PLAYER_SIZE[0] / 2, player_pos.y + PLAYER_SIZE[1] / 2)
    direction = pygame.Vector2(1, 0)  # Bullets go to the right; can customize later
    bullets.append({"pos": bullet_pos, "dir": direction})


# Create NPC instance
npc = NPC(NPC_COLOR, NPC_SPEED, NPC_SIZE)
generate_terrain()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_e]:
        draw_player = False
    if keys[pygame.K_SPACE]:
        shoot_bullet()

    handle_player_movement(keys, player_pos, PLAYER_SPEED, dt)
    npc.move_towards(player_pos, dt)

    # Update bullets
    for bullet in bullets[:]:
        bullet["pos"] += bullet["dir"] * BULLET_SPEED * dt
        if bullet["pos"].x > screen.get_width():
            bullets.remove(bullet)
        elif pygame.Rect(bullet["pos"].x, bullet["pos"].y, *BULLET_SIZE).colliderect(npc.get_rect()):
            bullets.remove(bullet)
            npc.pos = npc.random_position()  # Respawn NPC

    # Drawing
    screen.fill("black")

    # Draw terrain
    for terrain in terrain_list:
        pygame.draw.rect(screen, TERRAIN_COLOR, terrain)

    # Draw player
    if draw_player:
        pygame.draw.rect(screen, PLAYER_COLOR, (*player_pos, *PLAYER_SIZE))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (*bullet["pos"], *BULLET_SIZE))

    npc.draw(screen)

    pygame.display.flip()
    dt = clock.tick(120) / 1000

# Clean up
pygame.quit()
elapsed_time = round(time.time() - start_time, 2)
print(f"Elapsed time: {elapsed_time} sec")
