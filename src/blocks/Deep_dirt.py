from pyray import *
from src.Block import Block

class Deep_dirt(Block):
	def __init__(self, position: Vector2):
		super().__init__("deep_dirt", position, None)