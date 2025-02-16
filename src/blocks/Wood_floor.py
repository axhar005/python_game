from pyray import *
from src.Block import Block

class Wood_floor(Block):
	def __init__(self, position: Vector2):
		super().__init__("wood_floor", position, None)