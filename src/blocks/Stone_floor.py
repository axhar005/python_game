from pyray import *
from src.Block import Block

class Stone_floor(Block):
	def __init__(self, position: Vector2):
		super().__init__("stone_floor", position, None)