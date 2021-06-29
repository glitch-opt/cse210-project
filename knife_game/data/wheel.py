import arcade
import math
from data import constants

class Wheel(arcade.Sprite):
    """
    Display class for the wheel
    """

    def __init__(self):
        """
        Initialization of wheel
        """

        self.image = "knife_game/assets/images/wheel.png"
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.wheel_position = (self.screen_width // 2, self.screen_height * (0.7))
        self.wheel_rotation_speed = 2
        self.speed = 0

        super().__init__(self.image, .5)

        self.center_x = self.wheel_position[0]
        self.center_y = self.wheel_position[1]

        self.original_position = self.center_y
    
    def update(self):
        """
        Movement of wheel
        """
        # # Convert angle in degrees to radians.
        # angle_rad = math.radians(self.angle)

        self.change_angle = self.wheel_rotation_speed
        self.angle += self.change_angle
