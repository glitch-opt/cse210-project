import arcade;

class Director(arcade.Window):

    def __init__(self):
        self.screen_width = 540
        self.screen_height = 960

    def menu(self):
        img = 'knife_game/assets/images/bg2.png'
        arcade.draw_texture_rectangle(self.screen_width / 2, self.screen_height / 2, self.screen_width, self.screen_height, arcade.load_texture(img))

        output = "Press ENTER to Start"
        arcade.draw_text(output, self.screen_width * 0.5, self.screen_height * 0.35, arcade.color.WHITE, align="center", anchor_x="center")
