from pyray import *

class Block:
	def __init__(self):
		self.name: str = ""
		self.pos: Vector2 = None
		self.texture: Texture = None

	def __str__(self):
		return f"{self}"