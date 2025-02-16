from pyray import *
from src.Block import Block

class Water(Block):
	def __init__(self, position: Vector2):
		super().__init__("water", position, None)