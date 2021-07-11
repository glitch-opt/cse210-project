import pytest
import arcade
import knife
import constants
import director
import target


# Testing: knife.py

def test_throw():
    """Test Knife.throw function to verify knife is moving at
    the speed defined in constants.py"""
    k = knife.Knife()
    k.throw()
    assert k.change_y == constants.KNIFE_THROWN_MOVEMENT_SPEED


def test_hit_target():
    """Test Knife.hit_target to verify that knife travel ends
    and target_hit/wheel_hit equal true"""
    k = knife.Knife()
    k.hit_target(self)
    assert k.change_y == 0
    assert k.target_hit == True
    assert k.wheel_hit == True


# Testing: director.py

def test_setup_knife_count():
    """Test Director.setup function to verify knife_count is
    no longer defined as None"""
    d = director.Director()
    d.setup()
    assert d.knife_count == 5
    
def test_setup_knife_list(self):
    """Test Director.setup function to verify knife_list is
    no longer defined as None"""
    d = director.Director()
    d.setup(self)
    assert d.knife_list != None

def test_setup_wheel_list(self):
    """Test Director.setup function to verify wheel_list is
    no longer definead as None"""
    d = director.Director()
    d.setup(self)
    assert d.knife_count != None

def test_on_key_press_enter():
    """Test Director.on_key_press to verify that pressing
    ENTER changes current_state of game to running."""
    d = director.Director()
    key = arcade.key.ENTER
    
    d.on_key_press(key, None)
    assert d.current_state == director.GameState.GAME_RUNNING
    
def test_on_key_press_space():
    """Test Director.on_key_press to verify that pressing
    SPACE removes 1 knife from knife_count."""
    d = director.Director()
    d.setup()
    key = arcade.key.SPACE
    before_throw = d.knife_count
    d.on_key_press(key, None)
    after_throw = d.knife_count
    assert after_throw == before_throw - 1

def test_place_targets():
    """Test Director.place_targets to verify that quantity of
    targets placed is between 1-4."""
    d = director.Director()
    d.setup(self)
    assert len(d.target_list) > 0 and len(d.target_list) < 5

def test_speed_increase():
    """Test Director.setup to verify that speed increases
    every 3rd level."""
    d = director.Director()
    d.setup(self)
    if self.level % 3 == 0:
        assert self.wheel_rotation_speed += .25

def test_on_update():
    """Test Director.on_update to verify gamestate change
    when a target is hit and keep_running = 0."""
    d = director.Director()
    d.on_update(self)
    if keep_running == 0 and if self.target_hit:
        assert self.current_state = GameState.TARGET_DEFEATED


# Testing: target.py

def test_target_position():
    """Test Target.__init__ to verify that rotation is equal
    to position."""
    t = target.Target()
    t.__init__(self, position, wheel)
    assert self.rotation = position


# Call the main function that is part of pytest so that
# the test functions in this file will execute.
pytest.main(["-v", "--tb=no", "test_jumper.py"])