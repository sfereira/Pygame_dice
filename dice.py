import pygame
import random

# Set up the Pygame window
pygame.init()
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dice Simulator")

# Define the color and size of the die
die_color = (255, 255, 255)
die_size = (200, 200)

# Set up the dice position and size
dice_size = (200, 200)
dice_position = ((window_size[0] - dice_size[0]) // 2, (window_size[1] - dice_size[1]) // 2)

# Loop until the user quits
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Roll the die when the user presses the space bar
            result = random.randint(1, 6)
            
            # Draw the die on the screen
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, die_color, (*dice_position, *die_size))
            if result in (1, 3, 5):
                pygame.draw.circle(screen, (0, 0, 0), (dice_position[0] + die_size[0] // 2, dice_position[1] + die_size[1] // 2), die_size[0] // 10)
            if result in (2, 3, 4, 5, 6):
                pygame.draw.circle(screen, (0, 0, 0), (dice_position[0] + die_size[0] // 4, dice_position[1] + die_size[1] // 4), die_size[0] // 10)
                pygame.draw.circle(screen, (0, 0, 0), (dice_position[0] + 3 * die_size[0] // 4, dice_position[1] + 3 * die_size[1] // 4), die_size[0] // 10)
            if result in (4, 5, 6):
                pygame.draw.circle(screen, (0, 0, 0), (dice_position[0] + 3 * die_size[0] // 4, dice_position[1] + die_size[1] // 4), die_size[0] // 10)
                pygame.draw.circle(screen, (0, 0, 0), (dice_position[0] + die_size[0] // 4, dice_position[1] + 3 * die_size[1] // 4), die_size[0] // 10)
    
    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
