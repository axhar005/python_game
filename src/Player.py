from pyray import *
from src.Entity import *
from typing import List

class Player(Entity):
	def __init__(self, name: str, position: Vector2, sprite: List[Texture]) -> None:
		super().__init__(name, position, sprite)
		self.speed: float = 5.0

	def step(self) -> None:
		if(is_key_down(KeyboardKey.KEY_W)):
			self.pos.y -= self.speed
		if(is_key_down(KeyboardKey.KEY_S)):
			self.pos.y += self.speed
		if(is_key_down(KeyboardKey.KEY_A)):
			self.pos.x -= self.speed
		if(is_key_down(KeyboardKey.KEY_D)):
			self.pos.x += self.speed
