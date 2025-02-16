from pyray import *
from src.Block import Block


class Grass(Block):
	def __init__(self, position: Vector2):
		super().__init__("grass", position, None)