from pyray import *
from src.Engine import *
from src.Entity import *
from typing import List

class Player(Entity):
	def __init__(self, name: str, position: Vector2, sprite: List[Texture]) -> None:
		super().__init__(name, position, sprite)

	def step(self) -> None:
		if(is_key_down(KeyboardKey.KEY_W)):
			self.pos.y -= 0.2
		if(is_key_down(KeyboardKey.KEY_S)):
			self.pos.y += 0.2
		if(is_key_down(KeyboardKey.KEY_A)):
			self.pos.x -= 0.2
		if(is_key_down(KeyboardKey.KEY_D)):
			self.pos.x += 0.2


