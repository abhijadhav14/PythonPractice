import pygame
import sys
import random

pygame.init()

# Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemies")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

# Load background image and music
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#pygame.mixer.music.load("background.mp3")
#pygame.mixer.music.play(-1)  # Loop forever

def draw_text(text, size, color, x, y, center=True):
    font_obj = pygame.font.SysFont(None, size)
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.blit(background, (0, 0))
        draw_text("Avoid the Enemies", 64, WHITE, WIDTH // 2, HEIGHT // 2 - 80)
        draw_text("Press ENTER to Start", 36, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Press Q to Quit", 28, WHITE, WIDTH // 2, HEIGHT // 2 + 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

def game_loop():
    # Player
    player = pygame.Rect(100, 100, 50, 50)
    player_speed = 5

    # Multiple enemies
    enemies = []
    for _ in range(5):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        rect = pygame.Rect(x, y, 50, 50)
        direction = random.choice([-1, 1])
        speed = random.randint(2, 4)
        enemies.append({"rect": rect, "dir": direction, "speed": speed})

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
        if keys[pygame.K_UP]:
            player.y -= player_speed
        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # Enemy movement
        for e in enemies:
            e["rect"].x += e["dir"] * e["speed"]
            if e["rect"].left <= 0 or e["rect"].right >= WIDTH:
                e["dir"] *= -1

            if player.colliderect(e["rect"]):
                return score

        # Drawing
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, GREEN, player)
        for e in enemies:
            pygame.draw.rect(screen, RED, e["rect"])

        score += 1
        draw_text(f"Score: {score}", 36, WHITE, 10, 10, center=False)

        pygame.display.flip()
        clock.tick(60)

def game_over_screen(score):
    while True:
        screen.blit(background, (0, 0))
        draw_text("Game Over", 64, RED, WIDTH // 2, HEIGHT // 2 - 60)
        draw_text(f"Score: {score}", 48, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Press R to Restart or Q to Quit", 32, WHITE, WIDTH // 2, HEIGHT // 2 + 60)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return True
            elif keys[pygame.K_q]:
                return False

# Main loop
while True:
    main_menu()
    score = game_loop()
    if not game_over_screen(score):
        break
