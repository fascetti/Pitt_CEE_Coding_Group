import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 300))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the snake's starting position
x1 = 300
y1 = 300

# Set the snake's size
snake_block = 10
snake_speed = 30

# Set the direction of the snake
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Get the arrow key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Move the snake
    x1 += x1_change
    y1 += y1_change

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the snake
    pygame.draw.rect(screen, (0, 0, 0), [x1, y1, snake_block, snake_block])
    pygame.display.update()

    # Set the snake's speed
    clock.tick(snake_speed)
