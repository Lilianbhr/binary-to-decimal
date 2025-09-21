import pygame

# Window
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bin2Dec")

# Colors
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

# Main loop
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
