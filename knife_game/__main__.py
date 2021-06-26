import arcade
from data.director import Director

def main():
    window = Director()
    arcade.start_render()
    window.menu()
    arcade.run()

main()