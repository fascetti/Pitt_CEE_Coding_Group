import random
import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 400
screen_height = 300

# Set the screen size
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the snake's starting position
x1 = 600
y1 = 500

# Set the snake's size
snake_block = 10
snake_speed = 20
food_block = 10
snake_body = []

# Set the starting position of the snake
snake_x = int(screen_width/2)
snake_y = int(screen_height/2)

# Set the initial food position
food_x = 10*random.randint(0, int((screen_width - food_block)/10))
food_y = 10*random.randint(0, int((screen_height - food_block)/10))

# Set the direction of the snake
x_change = 0
y_change = 0
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
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    # Move the snake
    snake_x += x_change
    snake_y += y_change
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = (snake_body[i-1][0], snake_body[i-1][1])
    if len(snake_body) > 0:
        snake_body[0] = (snake_x, snake_y)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the snake
    #pygame.draw.rect(screen, (0, 0, 0), [snake_x, snake_y, snake_block, snake_block])
    for x, y in snake_body:
        pygame.draw.rect(screen, (0, 0, 0), [x, y, snake_block, snake_block])
    pygame.draw.rect(screen, (0, 0, 0), [snake_x, snake_y, snake_block, snake_block]) # draw the snake's head
    #...

    # Draw the food
    pygame.draw.rect(screen, (0, 255, 0), [food_x, food_y, food_block, food_block])
    pygame.display.update()

    # check for collision with walls
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        print("Collision with wall!")
        pygame.quit()
        quit()

    # check for collision with snake's body
    if snake_x == food_x and snake_y == food_y:
        print("Yummy!!")
        food_x = 10 * random.randint(0, int((screen_width - food_block) / 10))
        food_y = 10 * random.randint(0, int((screen_height - food_block) / 10))
        snake_body.append((snake_x, snake_y))  # add new segment to the snake's body

    # Set the snake's speed
    clock.tick(snake_speed)


