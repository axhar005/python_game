from pyray import *
from src.Block import Block

class Sand(Block):
	def __init__(self, position: Vector2):
		super().__init__("sand", position, None)