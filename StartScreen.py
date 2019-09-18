import pygame.font

# display title screen
class Title:
    def __init__(self, screen, msg, line):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.text_color = (150, 150, 150)
        self.font = pygame.font.SysFont(None, 72)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx, self.rect.centery = self.screen_rect.centerx, self.screen_rect.centery/2 + line
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, (0, 153, 76))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

# start game once play button is clicked
class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (150, 150, 150)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)