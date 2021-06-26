import arcade

from data import constants

class Director(arcade.Window):

    def __init__(self):
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        super().__init__(self.screen_width, self.screen_height, 'Knife Throw')

        arcade.set_background_color(arcade.color.AVOCADO)

    def setup(self):
        pass
    
    def draw_game(self):
        title = 'Knife Throw!'
        arcade.draw_text(title, self.screen_width * .5, self.screen_height * .7, arcade.color.ARSENIC, 40, align = 'center', anchor_x = 'center')

        output = 'Press ENTER to Start'
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.BLACK, align="center", anchor_x="center")
    
    # def draw_menu(self):

    def on_draw(self):
        arcade.start_render()

        self.draw_game()


import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://arcade.academy/arcade.key.html
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass
