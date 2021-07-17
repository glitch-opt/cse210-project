'''
Module runs the game by opening the director file and providing the 
environment for arcade.run
'''

import arcade
from data.director import Director

def main():
    window = Director()
    arcade.start_render()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()