'''
Module contains the Knife class, which stands for the objects thrown to the 
targets to hit them
'''

import arcade
import math
from data import constants

class Knife(arcade.Sprite):
    """
    Display class for the Knife
    """

    def __init__(self):
        """
        Initialization of knife
        """
        self.image = constants.KNIFE_IMAGE
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.knife_position = (self.screen_width // 2, self.screen_height * (0.2))

        self.knife_throw_sound = arcade.load_sound(constants.KNIFE_THROW_SOUND)
        self.knife_hit_wheel_sound = arcade.load_sound(constants.KNIFE_HIT_WHEEL_SOUND)
        self.knife_hit_target_sound = arcade.load_sound(constants.KNIFE_HIT_TARGET_SOUND)

        super().__init__(self.image, .25)

        self.center_x = self.knife_position[0]
        self.center_y = self.knife_position[1]
        self.change_y = 0

        self.rotation = 0
        self.wheel_hit = False
        self.target_hit = False
        self.knife_hit = False

        self.stuck_in_wheel = None
        self.stuck_in_target = None

    def throw(self):
        """" Throw the knife """
        self.change_y = constants.KNIFE_THROWN_MOVEMENT_SPEED
        arcade.play_sound(self.knife_throw_sound)

    def hit_wheel(self, wheel):
        '''Initializes the wheel hit state
        
        Args:
            wheel (Wheel): A Wheel object
        '''
        self.stuck_in_wheel = wheel
        arcade.play_sound(self.knife_hit_wheel_sound)

        self.wheel_hit = True
        self.change_y = 0

        self.rotation_radius = (self.stuck_in_wheel.height / 2)
        self.rotation_center = self.stuck_in_wheel.wheel_position

    def hit_target(self, wheel):
        '''
        Initializes the wheel hit and the target hit state
        '''
        self.stuck_in_wheel = wheel
        arcade.play_sound(self.knife_hit_target_sound)

        self.target_hit = True
        self.wheel_hit = True
        self.change_y = 0

        self.rotation_radius = (self.stuck_in_wheel.height / 1.5)
        self.rotation_center = self.stuck_in_wheel.wheel_position
    
    def update(self):
        '''
        Updates the knife state/position
        '''
        self.center_y += self.change_y

        if self.wheel_hit:
            self.rotation_speed = self.stuck_in_wheel.wheel_rotation_speed
            self.rotation += self.rotation_speed
            self.angle = self.rotation
            self.center_x = (self.rotation_radius * math.cos(math.radians(self.rotation+270))) + self.rotation_center[0]
            self.center_y = (self.rotation_radius * math.sin(math.radians(self.rotation+270))) + self.rotation_center[1]
        
        