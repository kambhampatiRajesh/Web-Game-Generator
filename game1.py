import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))

def generate_food_position(snake_body):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
        food_pos = (x, y)
        if food_pos not in snake_body:
            return food_pos

def reset_game():
    snake_body = [(100, 100), (80, 100), (60, 100)]
    snake_direction = RIGHT
    food_position = generate_food_position(snake_body)
    score = 0
    game_over = False
    return snake_body, snake_direction, food_position, score, game_over

def display_message(message, score_display=False, score=0):
    font = pygame.font.Font(None, 74)
    text_surface = font.render(message, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text_surface, text_rect)

    if score_display:
        score_font = pygame.font.Font(None, 50)
        score_surface = score_font.render(f"Score: {score}", True, WHITE)
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_surface, score_rect)

    small_font = pygame.font.Font(None, 36)
    restart_surface = small_font.render("Press R to Restart or Q to Quit", True, WHITE)
    restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(restart_surface, restart_rect)

    pygame.display.flip()

# Game loop
running = True
snake_body, snake_direction, food_position, score, game_over = reset_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT
            elif event.key == pygame.K_r and game_over:
                snake_body, snake_direction, food_position, score, game_over = reset_game()
            elif event.key == pygame.K_q and game_over:
                running = False

    if not game_over:
        # Move the snake
        head_x, head_y = snake_body[0]
        new_head = (head_x + snake_direction[0] * GRID_SIZE,
                    head_y + snake_direction[1] * GRID_SIZE)

        # Check for collisions
        # Wall collision
        if not (0 <= new_head[0] < SCREEN_WIDTH and 0 <= new_head[1] < SCREEN_HEIGHT):
            game_over = True
        # Self collision
        if new_head in snake_body[1:]:
            game_over = True
        
        if not game_over:
            snake_body.insert(0, new_head)

            # Food collision
            if new_head == food_position:
                score += 1
                food_position = generate_food_position(snake_body)
            else:
                snake_body.pop()

    # Drawing
    screen.fill(BLACK)
    # draw_grid() # Optional: Uncomment to see grid lines

    # Draw food
    pygame.draw.rect(screen, RED, (*food_position, GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (5, 5))

    if game_over:
        display_message("Game Over!", True, score)
    else:
        pygame.display.flip()

    # Control game speed
    clock.tick(10 + score // 5) # Increase speed with score

pygame.quit()