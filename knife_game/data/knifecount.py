import arcade
from data import constants

'''
Module for the KnifeCount class, which holds information about the knife count in game.
'''

class KnifeCount(arcade.Sprite):
    """
    Display class for number of Knives
    """

    def __init__(self, image_name, knife_count):
        """
        Initialization for the knife display
        """

        self.main_img = constants.KNIFE_COUNT_MAIN
        self.background_img = constants.KNIFE_COUNT_BACKGROUND
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT

        self.image_name = self.main_img

        if(image_name == "background"):
            self.image_name = self.background_img

        super().__init__(self.image_name, .4)

        self.knife_count = knife_count
        self.center_x = self.screen_width * .1
        self.center_y = (self.screen_height * .1) + (self.knife_count * self.screen_height * .03)