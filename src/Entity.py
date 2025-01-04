from pyray import *
from typing import List

class Entity:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture]) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.sprite_size: int = len(sprite)
		self.current_image: Texture = sprite[0]
		self.animation_speed: float = 0.5
		self.current_frame: int = 0
		self.animation_timer: float = 0.0

	def change_sprite(self, sprite: List[Texture]):
		self.sprite = sprite
		self.current_frame = 0
		self.sprite_size = len(sprite)
		self.current_image = sprite[0]

	def update(self):
		pass
	
	def step(self) -> None:
		pass
	
	def __str__(self) -> str:
		return f"EName: {self.name:5}\nEPos: {int(self.pos.x)},{int(self.pos.y)}"