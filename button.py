import pygame
import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialized button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Setting the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (255, 171, 76)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("alien_invasion\\fonts\PressStart2P-Regular.ttf", 48)

        # Building the button's rect object and center.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message need to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turning msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Drawing blank button and then the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)