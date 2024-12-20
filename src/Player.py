from pyray import *
from src.Engine import *
from src.Entity import *

class Player(Entity):
	def __init__(self, name, position, texture):
		super().__init__(name, position, texture)
	
	def step(self):
		if(is_key_down(KeyboardKey.KEY_W)):
			self.pos.y -= 0.5
		if(is_key_down(KeyboardKey.KEY_S)):
			self.pos.y += 0.5
		if(is_key_down(KeyboardKey.KEY_A)):
			self.pos.x -= 0.5
		if(is_key_down(KeyboardKey.KEY_D)):
			self.pos.x += 0.5