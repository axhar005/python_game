from src.Data import *

class Stone_floor(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("stone_floor", position, data.sprites["stone_floor"])