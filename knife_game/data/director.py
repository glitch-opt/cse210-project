import arcade
import random
from data.wheel import Wheel
from data.knife import Knife
from data.target import Target
from data.knifecount import KnifeCount
from enum import Enum
from data import constants

class GameState(Enum):
    """ Store game state in enum """

    MENU = 1
    GAME_RUNNING = 2
    TARGET_DEFEATED = 3
    GAME_OVER = 4

class Director(arcade.Window):
    """
    Main game controll class
    """

    def __init__(self):
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        super().__init__(self.screen_width, self.screen_height, 'Knife Throw')

        self.current_state = GameState.MENU
        self.level = 1
        self.wheel = None
        self.knife = None
        self.target = None

        self.knife_list = None
        self.wheel_list = None
        self.target_list = None
        self.knife_count_display = None
        self.knife_count_list_display = None
        self.knife_count = None

        self.score = 0

        self.start_knife_count = None

        arcade.set_background_color(arcade.color.AVOCADO)

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

        self.create_knife()

        self.create_wheel()

        self.create_knife_count_display()

        self.place_targets()
    
    def draw_menu(self):
        """
        Method that creates the main menu
        """

        title = 'Knife Throw!'
        arcade.draw_text(title, self.screen_width * .5, self.screen_height * .7, arcade.color.ARSENIC, 40, align = 'center', anchor_x = 'center')

        output = 'Press ENTER to Start'
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.BLACK, align="center", anchor_x="center")
    
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


    def on_draw(self):
        """
        Render screen
        """

        arcade.start_render()

        if self.current_state == GameState.MENU:
            self.draw_menu()
        elif self.current_state == GameState.GAME_RUNNING:
            self.draw_game()

    def on_key_press(self, key, key_modifiers):
        """
        Handle all key presses
        """
        if key == arcade.key.ENTER and self.current_state == GameState.MENU:
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
                self.score -= 1
                self.knife.hit_wheel(self.wheel)

                if self.knife_count > 0:
                    self.create_knife()

        target_hit_list = arcade.check_for_collision_with_list(self.knife, self.target_list)
        if not self.knife.target_hit:
            for x in target_hit_list:
                self.score += 1
                self.knife.hit_target(self.wheel)

                if self.knife_count > 0:
                    self.create_knife()

        knife_hit_list = arcade.check_for_collision_with_list(self.knife, self.knife_list)
        if not self.knife.knife_hit:
            for x in knife_hit_list:
                self.score -= 1
                self.knife.hit_knife(self.wheel)

    def create_wheel(self):
        """
        Create the wheel
        """
        self.wheel = Wheel()
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
                print(target_position)

                too_close = 0
                for target in self.target_list:
                    distance = abs(self.target.initial_target_position - target_position)
                    if distance < 10 or distance > 350:
                        too_close += 1
                if too_close == 0:
                    position_set = True
            
            positions.append(target_position)

        for i in positions:
            self.target = Target(i)
            self.target_list.append(self.target)
