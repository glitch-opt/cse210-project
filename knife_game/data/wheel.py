import arcade
from data import constants

class Wheel(arcade.Sprite):

    def __init__(self):
        self.image =  "../assets/images/wood1.png"
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.position = (self.screen_width // 2, self.screen_height * (0.7))

        super().__init__(self.image, 1)

        self.center_x = self.position[0]
        self.center_y = self.position[1]