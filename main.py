import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Game with Lives and Audience')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Set up game variables
score = 0
lives = 3
level = 1
player_speed = 5
target_speed = 2
game_over = False

# Player setup
player = pygame.Rect(screen_width // 2, screen_height - 50, 50, 50)

# Target setup
target = pygame.Rect(random.randint(0, screen_width - 50), random.randint(0, screen_height // 2), 50, 50)

# Function to display text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Game Over screen
def game_over_screen():
    screen.fill(WHITE)
    draw_text('Game Over', large_font, RED, screen, screen_width // 2, screen_height // 2 - 100)
    draw_text('The audience is excited! Play again?', font, BLACK, screen, screen_width // 2, screen_height // 2)
    draw_text('Press R to Restart or Q to Quit', font, BLACK, screen, screen_width // 2, screen_height // 2 + 50)
    pygame.display.flip()

# Main game loop
running = True
while running:
    if not game_over:
        # Fill background
        screen.fill(WHITE)

        # Get user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < screen_width:
            player.x += player_speed
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.bottom < screen_height:
            player.y += player_speed

        # Move the target randomly
        target.y += target_speed
        if target.y > screen_height:
            target.x = random.randint(0, screen_width - 50)
            target.y = random.randint(0, screen_height // 2)
            lives -= 1

        # Collision detection
        if player.colliderect(target):
            score += 10
            target.x = random.randint(0, screen_width - 50)
            target.y = random.randint(0, screen_height // 2)

            # Leveling up
            if score % 50 == 0:
                level += 1
                target_speed += 1

        # Draw player and target
        pygame.draw.rect(screen, GREEN, player)
        pygame.draw.rect(screen, RED, target)

        # Draw the score, lives, and level
        draw_text(f'Score: {score}', font, BLACK, screen, 100, 50)
        draw_text(f'Lives: {lives}', font, BLACK, screen, 100, 100)
        draw_text(f'Level: {level}', font, BLACK, screen, 100, 150)

        # Check for game over
        if lives <= 0:
            game_over = True

        pygame.display.flip()
    else:
        game_over_screen()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart the game
                score = 0
                lives = 3
                level = 1
                target_speed = 2
                game_over = False
            elif event.key == pygame.K_q:
                running = False

    # FPS
    pygame.time.Clock().tick(60)

pygame.quit()
