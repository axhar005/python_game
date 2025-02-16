from pyray import *
from src.Block import Block

class Hill(Block):
	def __init__(self, position: Vector2):
		super().__init__("hill", position, None)