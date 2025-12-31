import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()
SNAKE_SPEED = 10

# Font for score and game over message
font_style = pygame.font.SysFont(None, 30)
game_over_font = pygame.font.SysFont(None, 50)

def display_message(msg, color, y_displace=0, font=font_style):
    text = font.render(msg, True, color)
    screen.blit(text, [SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2 + y_displace])

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, CELL_SIZE, CELL_SIZE])

def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, SCREEN_WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
        food_y = round(random.randrange(0, SCREEN_HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
        if (food_x, food_y) not in snake_list:
            return food_x, food_y

def game_loop():
    game_over = False
    game_close = False

    # Snake initial position and movement
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food initial position
    food_x, food_y = generate_food(snake_list)

    score = 0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            display_message("Game Over! Press C-Play Again or Q-Quit", RED, -50, game_over_font)
            display_message(f"Score: {score}", WHITE, 20)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -CELL_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = CELL_SIZE
                    x1_change = 0

        # Boundary checks
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        snake_head = (x1, y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_message(f"Score: {score}", WHITE, -SCREEN_HEIGHT / 2 + 30)

        pygame.display.update()

        # Food collision
        if x1 == food_x and y1 == food_y:
            food_x, food_y = generate_food(snake_list)
            length_of_snake += 1
            score += 10

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()