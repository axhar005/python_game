from src.Data import *

class Wood_floor(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("wood_floor", position, data.sprites["wood_floor"])