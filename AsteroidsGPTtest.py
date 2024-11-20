import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Game Window Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Game Variables
player_pos = [WIDTH // 2, HEIGHT // 2]
player_velocity = [0, 0]
player_speed = 5
player_health = 100
coins = 0
score = 0
overdrive_active = False
overdrive_time = 0

# Load Assets
player_image = pygame.Surface((50, 50))
player_image.fill(WHITE)  # Placeholder, use an actual image
bullet_image = pygame.Surface((5, 10))
bullet_image.fill(RED)
enemy_bullet_image = pygame.Surface((5, 10))
enemy_bullet_image.fill(YELLOW)

# Game Objects (Player, Bullets, Enemies, Coins)
bullets = []
asteroids = []
enemies = []
enemy_bullets = []

# Font
font = pygame.font.Font(None, 36)


# Helper Function: Draw Text
def draw_text(text, x, y):
    label = font.render(text, True, WHITE)
    screen.blit(label, (x, y))


# Helper Function: Spawn Enemy
def spawn_enemy():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    enemy = {"pos": [x, y], "velocity": [random.choice([-1, 1]), random.choice([-1, 1])], "health": 50}
    enemies.append(enemy)


# Helper Function: Spawn Enemy Bullet
def spawn_enemy_bullet(enemy_pos):
    bullet_velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    bullet = {"pos": [enemy_pos[0], enemy_pos[1]], "velocity": bullet_velocity}
    enemy_bullets.append(bullet)


# Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle Player Movement and Rotation
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx = mouse_x - player_pos[0]
    dy = mouse_y - player_pos[1]
    angle = math.atan2(dy, dx)

    # Move Player Towards Mouse
    if pygame.mouse.get_pressed()[0]:  # Left Click for movement
        player_velocity[0] = player_speed * math.cos(angle)
        player_velocity[1] = player_speed * math.sin(angle)
    else:
        player_velocity = [0, 0]

    # Apply Movement
    player_pos[0] += player_velocity[0]
    player_pos[1] += player_velocity[1]

    # Player Wrap Around Screen
    if player_pos[0] < 0:
        player_pos[0] = WIDTH
    elif player_pos[0] > WIDTH:
        player_pos[0] = 0
    if player_pos[1] < 0:
        player_pos[1] = HEIGHT
    elif player_pos[1] > HEIGHT:
        player_pos[1] = 0

    # Handle Bullet Firing (Right Mouse Button)
    if pygame.mouse.get_pressed()[2]:  # Right Click to shoot
        bullet_pos = [player_pos[0], player_pos[1]]
        bullet_velocity = [10 * math.cos(angle), 10 * math.sin(angle)]
        bullets.append([bullet_pos, bullet_velocity])

    # Update and Draw Bullets
    for bullet in bullets[:]:
        bullet[0][0] += bullet[1][0]
        bullet[0][1] += bullet[1][1]
        pygame.draw.rect(screen, RED, pygame.Rect(bullet[0][0], bullet[0][1], 5, 10))
        if bullet[0][0] < 0 or bullet[0][0] > WIDTH or bullet[0][1] < 0 or bullet[0][1] > HEIGHT:
            bullets.remove(bullet)

    # Handle Overdrive (Spacebar)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        overdrive_active = True
        overdrive_time = pygame.time.get_ticks()  # Track time for overdrive duration
    if overdrive_active:
        if pygame.time.get_ticks() - overdrive_time > 5000:  # Overdrive lasts for 5 seconds
            overdrive_active = False
        else:
            player_speed = 10  # Speed boost during overdrive

    # Draw Player (Fixed Size, Rotating)
    rotated_player = pygame.transform.rotate(player_image, -math.degrees(angle))
    screen.blit(rotated_player,
                (player_pos[0] - rotated_player.get_width() // 2, player_pos[1] - rotated_player.get_height() // 2))

    # Spawn Enemies and Enemy Bullets
    if random.random() < 0.02:  # Chance to spawn enemies
        spawn_enemy()

    # Move and Draw Enemies
    for enemy in enemies[:]:
        enemy["pos"][0] += enemy["velocity"][0] * player_speed * 0.5  # Slower than player
        enemy["pos"][1] += enemy["velocity"][1] * player_speed * 0.5

        # Wrap enemy around the screen if it moves offscreen
        if enemy["pos"][0] < 0:
            enemy["pos"][0] = WIDTH
        elif enemy["pos"][0] > WIDTH:
            enemy["pos"][0] = 0
        if enemy["pos"][1] < 0:
            enemy["pos"][1] = HEIGHT
        elif enemy["pos"][1] > HEIGHT:
            enemy["pos"][1] = 0

        # Draw enemies
        pygame.draw.circle(screen, GREEN, (int(enemy["pos"][0]), int(enemy["pos"][1])), 20)

        # Spawn enemy bullets randomly
        if random.random() < 0.05:  # Chance to shoot
            spawn_enemy_bullet(enemy["pos"])

        # Handle Collisions (between bullets and enemies)
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet[0][0], bullet[0][1], 5, 10)
            enemy_rect = pygame.Rect(enemy["pos"][0] - 20, enemy["pos"][1] - 20, 40, 40)
            if bullet_rect.colliderect(enemy_rect):
                enemies.remove(enemy)  # Enemy is destroyed
                bullets.remove(bullet)  # Bullet disappears
                score += 100  # Add score
                coins += 10  # Drop coins
                break

    # Handle Enemy Bullets
    for enemy_bullet in enemy_bullets[:]:
        enemy_bullet["pos"][0] += enemy_bullet["velocity"][0] * 5
        enemy_bullet["pos"][1] += enemy_bullet["velocity"][1] * 5
        pygame.draw.rect(screen, YELLOW, pygame.Rect(enemy_bullet["pos"][0], enemy_bullet["pos"][1], 5, 10))

        # Check for collision with player
        player_rect = pygame.Rect(player_pos[0] - 25, player_pos[1] - 25, 50, 50)
        bullet_rect = pygame.Rect(enemy_bullet["pos"][0], enemy_bullet["pos"][1], 5, 10)
        if player_rect.colliderect(bullet_rect):
            enemy_bullets.remove(enemy_bullet)  # Remove enemy bullet
            player_health -= 10  # Decrease health
            if player_health <= 0:
                print("Game Over!")  # Handle game over
                running = False

    # Display Score, Coins, and Player Health
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Coins: {coins}", 10, 40)
    draw_text(f"Health: {player_health}", WIDTH - 150, 10)

    # Game Update
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
