import arcade
import math
from data import constants

class Target(arcade.Sprite):
    '''Class for targets on wheel for player to aim at.

    Stereotype:
        Information Holder

    Attributes:
    '''
    def __init__(self, position, wheel):
        '''The class initializer'''
        self.image = constants.TARGET_IMAGE
        self.wheel = wheel
        self.rotation_speed = self.wheel.wheel_rotation_speed
        self.rotation_radius = self.wheel.height / 2
        self.rotation_center = self.wheel.wheel_position
        self.initial_target_position = position

        super().__init__(self.image, .05)

        self.rotation = position


    def update(self):
        '''Moves targets with wheel'''
        self.rotation_speed = self.wheel.wheel_rotation_speed
        self.rotation += self.rotation_speed
        self.angle = self.rotation
        self.center_x = (self.rotation_radius * math.cos(math.radians(self.rotation+270))) + self.rotation_center[0]
        self.center_y = (self.rotation_radius * math.sin(math.radians(self.rotation+270))) + self.rotation_center[1]

