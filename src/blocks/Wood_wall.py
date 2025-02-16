from src.Data import *

class Wood_wall(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("wood_wall", position, data.sprites["wood_wall"])