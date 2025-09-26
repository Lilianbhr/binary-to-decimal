import pygame
from display import Area
from logic import *
pygame.init()

# Window
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bin2Dec")
pygame.display.set_icon(pygame.image.load("../assets/swap.png").convert_alpha())

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
grey = (235, 235, 235)
dark_grey1 = (161, 161, 161)
dark_grey2 = (181, 181, 181)

# Main loop
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
