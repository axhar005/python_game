from src.Data import *

class Water(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("water", position, data.sprites["water"])