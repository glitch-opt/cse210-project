import arcade
from data import constants

class Knife(arcade.Sprite):
    def __init__(self):
        self.image = "knife_game/assets/images/knife.png"
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.knife_position = (self.screen_width // 2, self.screen_height * (0.2))

        super().__init__(self.image, .25)

        self.center_x = self.knife_position[0]
        self.center_y = self.knife_position[1]