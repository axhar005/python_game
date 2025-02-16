from pyray import *
from src.Block import Block

class Air(Block):
	def __init__(self, position: Vector2):
		super().__init__("air", position, None)