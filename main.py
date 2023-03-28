import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
game_window = pygame.display.set_mode(WINDOW_SIZE)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"

# Set up the game loop
game_over = False
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_direction = "LEFT"
    elif keys[pygame.K_RIGHT]:
        snake_direction = "RIGHT"
    elif keys[pygame.K_UP]:
        snake_direction = "UP"
    elif keys[pygame.K_DOWN]:
        snake_direction = "DOWN"

    # Update the snake position
    if snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10
    elif snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10

    # Update the snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawned = False
    else:
        snake_body.pop()

    # Draw the game objects
    game_window.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(game_window, BLACK, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.display.update()

    # Limit the game's frame rate
    clock.tick(15)

# Clean up Pygame
pygame.quit()
