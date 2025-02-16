from src.Data import *

class Stone_wall(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("stone_wall", position, data.sprites["stone_wall"])