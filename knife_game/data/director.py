import arcade
import random
from data.wheel import Wheel
from data.knife import Knife
from data.target import Target
from data.knifecount import KnifeCount
from enum import Enum
from data import constants

'''
Module contains the main control system for the functionality of the game, including
the setup, update, and draw functions.
'''

class GameState(Enum):
    """ Store game state in enum """
    MENU = 1
    GAME_RUNNING = 2
    TARGET_DEFEATED = 3
    GAME_OVER = 4

class Director(arcade.Window):
    """
    Main game control class
    """
    def __init__(self):
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        super().__init__(self.screen_width, self.screen_height, 'Knife Throw')

        self.current_state = GameState.MENU
        self.level = 0
        self.wheel = None
        self.knife = None
        self.target = None

        self.knife_list = None
        self.wheel_list = None
        self.target_list = None
        self.knife_count_display = None
        self.knife_count_list_display = None
        self.knife_count = None
        self.target_hit = None

        self.score = 0
        self.wheel_rotation_speed = 1

        self.start_knife_count = None

        arcade.set_background_color(arcade.color.AVOCADO)
        self.background_image = arcade.load_texture(constants.BACKGROUND)

    def setup(self):
        """
        Initialization of all the game variables
        """
        self.knife_list = arcade.SpriteList()
        self.wheel_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()
        self.knife_count_list_display = arcade.SpriteList()

        self.knife_count = 5
        self.start_knife_count = self.knife_count
        self.target_hit = False
        if self.level % 3 == 0:
            self.wheel_rotation_speed += .25

        self.create_knife()

        self.create_wheel(self.wheel_rotation_speed)

        self.create_knife_count_display()

        self.place_targets()
    
    def draw_menu(self):
        """
        Method that creates the main menu
        """
        arcade.draw_rectangle_filled(self.screen_width / 2, self.screen_height / 2, self.screen_width - 30, self.screen_height / 2, arcade.color.BLACK)

        title = 'Knife Throw!'
        arcade.draw_text(title, self.screen_width * .5, self.screen_height * .6, arcade.color.WHITE, 40, align = 'center', anchor_x = 'center')

        output = 'Press ENTER to Start'
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.WHITE, align="center", anchor_x="center")
    
    def draw_game(self):
        """
        Method that creates the game view
        """
        self.knife_list.draw()
        self.wheel_list.draw()
        self.target_list.draw()
        self.knife_count_list_display.draw()

        level_display = f'Level: {self.level}'
        arcade.draw_text(level_display, self.screen_width * 0.5, self.screen_height * 0.975, (255,255,255), 14,  align="center", anchor_x="center", anchor_y="center")

        output = f"Press <space> to shoot"
        arcade.draw_text(output, self.screen_height * 0.5, self.screen_height * 0.05, (255,255,255), 12,  align="center", anchor_x="center", anchor_y="center")

        output = f"{self.score}"
        arcade.draw_text(output, self.screen_width * 0.1, self.screen_height * 0.95, (239, 182, 90), 28,  align="center", anchor_x="center", anchor_y="center")

    def draw_level_end(self):
        """
        Method that draws the end screen: displays score, and asks player to play again
        """
        arcade.draw_rectangle_filled(self.screen_width / 2, self.screen_height / 2, self.screen_width - 30, self.screen_height / 2, arcade.color.BLACK)
        
        score = f"Your score is: {self.score}"
        arcade.draw_text(score, self.screen_width * .5, self.screen_height * .6, arcade.color.WHITE, 40, align = 'center', anchor_x = 'center')

        output = "Press ENTER to keep going!"
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.WHITE, align="center", anchor_x="center")

    def draw_game_end(self):
        """
        Method that draws the game over screen: displays score, level reached, and thanks 
        player for playing
        """
        arcade.draw_rectangle_filled(self.screen_width / 2, self.screen_height / 2, self.screen_width - 30, self.screen_height / 2, arcade.color.BLACK)

        game_over = "Game Over"
        arcade.draw_text(game_over, self.screen_width * .5, self.screen_height * .65, arcade.color.WHITE, 40, align = 'center', anchor_x = 'center')

        score = f"Your score was: {self.score}"
        arcade.draw_text(score, self.screen_width * .5, self.screen_height * .55, arcade.color.WHITE, 20, align = 'center', anchor_x = 'center')

        level = f"You reached level {self.level}"
        arcade.draw_text(level, self.screen_width * .5, self.screen_height * .45, arcade.color.WHITE, 20, align = 'center', anchor_x = 'center')

        thanks = 'Thanks for Playing!'
        arcade.draw_text(thanks, self.screen_width * .5, self.screen_height * .3, arcade.color.WHITE, 40, align = 'center', anchor_x = 'center')

    def on_draw(self):
        """
        Render screen
        """
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, self.screen_width, self.screen_height, self.background_image)

        if self.current_state == GameState.MENU:
            self.draw_menu()
        elif self.current_state == GameState.GAME_RUNNING:
            self.draw_game()
        elif self.current_state == GameState.TARGET_DEFEATED:
            self.draw_level_end()
        elif self.current_state == GameState.GAME_OVER:
            self.draw_game_end()

    def on_key_press(self, key, key_modifiers):
        """
        Handle all key presses
        """
        if key == arcade.key.ENTER and self.current_state == GameState.MENU or self.current_state == GameState.TARGET_DEFEATED:
            self.level += 1
            self.setup()
            self.current_state = GameState.GAME_RUNNING

        if key == arcade.key.SPACE and self.knife_count > 0 and self.current_state == GameState.GAME_RUNNING:
            self.knife_count -= 1
            self.knife.throw()

            knife_used = self.start_knife_count - self.knife_count
            self.knife_count_list_display[-knife_used].alpha = (0)

    def on_update(self, delta_time):
        """
        Game logic
        """
        self.knife_list.update()
        self.wheel_list.update()
        self.target_list.update()

        wheel_hit_list = arcade.check_for_collision_with_list(self.knife, self.wheel_list)
        if not self.knife.wheel_hit:
            for x in wheel_hit_list:
                self.knife.hit_wheel(self.wheel)

                if self.knife_count > 0:
                    self.create_knife()

        target_hit_list = arcade.check_for_collision_with_list(self.knife, self.target_list)
        if not self.knife.target_hit:
            for x in target_hit_list:
                self.score += 1
                self.target_hit = True
                self.knife.hit_target(self.wheel)

                if self.knife_count > 0:
                    self.create_knife()

        keep_running = 0
        for knife in self.knife_list:
            if not knife.wheel_hit:
                keep_running += 1
        
        if keep_running == 0:
            if self.target_hit:
                self.current_state = GameState.TARGET_DEFEATED
            else:
                self.current_state = GameState.GAME_OVER

    def create_wheel(self, wheel_rotation_speed):
        """
        Create the wheel
        """
        self.wheel = Wheel(wheel_rotation_speed)
        self.wheel_list.append(self.wheel)

    def create_knife(self):
        """
        Create the knife
        """
        self.knife = Knife()
        self.knife_list.append(self.knife)

    def create_knife_count_display(self):
        """
        Create knife count display
        """
        for i in range(self.knife_count):
            self.knife_count_display = KnifeCount('background', i)
            self.knife_count_list_display.append(self.knife_count_display)

        for i in range(self.knife_count):
            self.knife_count_display = KnifeCount('foreground', i)
            self.knife_count_list_display.append(self.knife_count_display)
            
    def place_targets(self):
        """
        Place targets on the wheel
        """
        target_count = random.randint(1, constants.MAX_TARGET_COUNT)
        positions = []
        for x in range(target_count):
            position_set = False
            
            while not position_set:
                target_position = random.randint(0, 359)

                too_close = 0
                for target in self.target_list:
                    distance = abs(target.rotation - target_position)
                    if distance < 10 or distance > 350:
                        too_close += 1
                if too_close == 0:
                    position_set = True
            
            positions.append(target_position)
            target = Target(positions[-1], self.wheel)
            self.target_list.append(target)