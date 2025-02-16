from pyray import *
from src.Block import Block


class Dirt(Block):
	def __init__(self, position: Vector2):
		super().__init__("dirt", position, None)