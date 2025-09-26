"""
This module contain two class that manage the UI
"""

import pygame
from logic import get_resource_path


class Area:
    def __init__(self, color: tuple, screen: tuple[int, int]):
        """
        Area is a subdivision of the main window, this class is useful to organize
        the UI in a clean way
        :param color: tuple that contain the RGB values
        :param screen: tuple that contain the size of the window as integer values
        """
        self.bg_color = pygame.Color(color)
        self.screen_width, self.screen_height = screen
        self.area = pygame.surface.Surface((self.screen_width, self.screen_height // 2))
        self.font = pygame.font.Font(get_resource_path("../assets/font.ttf"), 25)

    def draw(self, screen: pygame.Surface, data_type: str, data: str,
             text_colors: list[tuple, tuple], area_pos: int) -> None:
        """
        display the elements on the Surface, and display the Surface on the Window
        :param screen: pygame surface that refer to the window
        :param data_type: string, "decimal" or "binary"
        :param data: string, the decimal or binary number
        :param text_colors: list, RGB values (in tuples) of the texts
        :param area_pos: integer, y position of the current area
        :return: nothing
        """
        self.area.fill(self.bg_color)

        text = self.font.render(data_type, 1, pygame.Color(text_colors[0]))
        text_pos = text.get_rect(centerx=self.screen_width // 4,
                                 centery=self.screen_height // 4)
        self.area.blit(text, text_pos)

        text = self.font.render(data, 1, pygame.Color(text_colors[1]))
        text_pos = text.get_rect(centerx=self.screen_width * 2//3,
                                 centery=self.screen_height // 4)
        self.area.blit(text, text_pos)

        screen.blit(self.area, (0, area_pos))


class Button:
    def __init__(self, screen_size: tuple[int, int]):
        """
        the button allow the user to invert the convertion direction
        :param screen_size: tuple, first integer for width, second integer for height
        """
        self.image = pygame.image.load(get_resource_path("../assets/swap.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.position = self.image.get_rect(centerx=screen_size[0]//2, centery=screen_size[1]//2)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.position)

    def clicked(self, mouse_pos: tuple) -> bool:
        return self.position.collidepoint(mouse_pos)
