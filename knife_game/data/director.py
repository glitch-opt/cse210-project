import arcade
from data.wheel import Wheel
from data.knife import Knife
from enum import Enum
from data import constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

class GameState(Enum):
    """ Store game state in enum """

    MENU = 1
    GAME_RUNNING = 2
    TARGET_DEFEATED = 3
    GAME_OVER = 4

class Director(arcade.Window):

    def __init__(self):
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        super().__init__(self.screen_width, self.screen_height, 'Knife Throw')

        self.current_state = GameState.MENU
        self.wheel = None
        self.knife = None

        self.knife_list = None
        self.wheel_list = None
        self.knife_count = None

        arcade.set_background_color(arcade.color.AVOCADO)

    def setup(self):
        self.knife_list = arcade.SpriteList()
        self.wheel_list = arcade.SpriteList()

        self.knife_count = 5

        self.create_knife()

        self.create_wheel()
    
    def draw_menu(self):
        title = 'Knife Throw!'
        arcade.draw_text(title, self.screen_width * .5, self.screen_height * .7, arcade.color.ARSENIC, 40, align = 'center', anchor_x = 'center')

        output = 'Press ENTER to Start'
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.BLACK, align="center", anchor_x="center")
    
    def draw_game(self):
        self.knife_list.draw()
        self.wheel_list.draw()

        output = f"Press <space> to shoot"
        arcade.draw_text(output, self.screen_height * 0.5, self.screen_height * 0.05, (255,255,255), 12,  align="center", anchor_x="center", anchor_y="center",)


    def on_draw(self):
        arcade.start_render()

        if self.current_state == GameState.MENU:
         self.draw_menu()
        elif self.current_state == GameState.GAME_RUNNING:
            self.draw_game()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://arcade.academy/arcade.key.html
        """
        if key == arcade.key.ENTER:
            self.setup()
            self.current_state = GameState.GAME_RUNNING

    def create_wheel(self):
        self.wheel = Wheel()
        self.wheel_list.append(self.wheel)

    def create_knife(self):
        self.knife = Knife()
        self.knife_list.append(self.knife)

# class MyGame(arcade.Window):
#     """
#     Main application class.

#     NOTE: Go ahead and delete the methods you don't need.
#     If you do need a method, delete the 'pass' and replace it
#     with your own code. Don't leave 'pass' in this program.
#     """

#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)

#         arcade.set_background_color(arcade.color.AMAZON)

#         self.director = Director()

#         # If you have sprite lists, you should create them here,
#         # and set them to None

#     def setup(self):
#         """ Set up the game variables. Call to re-start the game. """
#         # Create your sprites and sprite lists here
#         pass

#     def on_draw(self):
#         """
#         Render the screen.
#         """

#         # This command should happen before we start drawing. It will clear
#         # the screen to the background color, and erase what we drew last frame.
#         arcade.start_render()

#         # Call draw() on all your sprite lists below

#     def on_update(self, delta_time):
#         """
#         All the logic to move, and the game logic goes here.
#         Normally, you'll call update() on the sprite lists that
#         need it.
#         """
#         pass

#     def on_key_press(self, key, key_modifiers):
#         """
#         Called whenever a key on the keyboard is pressed.

#         For a full list of keys, see:
#         https://arcade.academy/arcade.key.html
#         """
#         if key == arcade.key.SPACE:
#             self.setup()
#             self.director.current_state = GameState.GAME_RUNNING


#     def on_mouse_press(self, x, y, button, key_modifiers):
#         """
#         Called when the user presses a mouse button.
#         """
#         pass
