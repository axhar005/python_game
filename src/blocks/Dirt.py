from src.Data import *

class Dirt(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("dirt", position, data.sprites["dirt"])