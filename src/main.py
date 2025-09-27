# Version 1.1 -> 26/09/2025 (dd/mm/yyyy)

from display import *
from logic import *
pygame.init()

# Window
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bin2Dec")
pygame.display.set_icon(pygame.image.load(get_resource_path("assets/swap.png")).convert_alpha())

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
grey = (235, 235, 235)
dark_grey1 = (161, 161, 161)
dark_grey2 = (181, 181, 181)

# Initialisation
mode = 0    # 0 for binary, 1 for decimal
if mode:
    user_input = "0"
else:
    user_input = ""
surface1 = Area(grey, (width, height))
surface2 = Area(white, (width, height))
button = Button((width, height))

# Main loop
running = True
while running:

    # Draw elements on screen
    if mode:
        if int(user_input) > 255:
            user_input = "255"
        converted_input = convert_decimal_to_binary(int(user_input))
        surface1.draw(screen, "decimal", user_input, [dark_grey1, black], 0)
        surface2.draw(screen, "binary", converted_input, [dark_grey2, black], width//2)
    else:
        tmp_user_input = ""
        for i in range(8 - len(user_input)):
            tmp_user_input += "0"
        tmp_user_input += user_input
        converted_input = convert_binary_to_decimal(tmp_user_input)
        surface1.draw(screen, "binary", tmp_user_input, [dark_grey1, black], 0)
        surface2.draw(screen, "decimal", converted_input, [dark_grey2, black], width//2)

    button.draw(screen)

    # Events management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(user_input) > 0:
                user_input = user_input[:-1]
                if mode and user_input == "":
                    user_input = "0"
            else:
                character = chr(event.key)
                if character_verification(character, mode):
                    if user_input == '0':
                        user_input = ""
                    user_input += character
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            if button.clicked(pygame.mouse.get_pos()):
                mode = 1 - mode
                if mode and user_input == "":
                    user_input = "0"
                user_input = converted_input

    pygame.display.flip()

pygame.quit()
