from pyray import *

class Entity:
	def __init__(self, name: str, position: Vector2, texture: Texture):
		self.name: str = str
		self.pos: Vector2 = position
		self.texture: Texture = texture
		self.velocity: Vector2 = Vector2(0, 0)

	def step(self):
		pass