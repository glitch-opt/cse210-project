import arcade
from data import constants

class Wheel(arcade.Sprite):

    def __init__(self):
        self.image =  "knife_game/assets/images/wood1.png"
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.wheel_position = (self.screen_width // 2, self.screen_height * (0.7))
        self.rotation_speed = 2

        super().__init__(self.image, .5)

        self.center_x = self.wheel_position[0]
        self.center_y = self.wheel_position[1]

        self.original_position = self.center_y