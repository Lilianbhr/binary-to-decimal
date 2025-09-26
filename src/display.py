import pygame


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
        self.font = pygame.font.Font("../assets/font.ttf", 25)

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
