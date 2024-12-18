import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = -4 
ball_speed_y = -4 

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 30
paddle_speed = 8

# Score
score = 0

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.Font(None, 36)

# Game loop flag
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y *= -1
        score += 1

    if ball_y > SCREEN_HEIGHT:
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    screen.fill(BLACK)  # Clear screen
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  # Draw ball
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))  # Draw paddle

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
