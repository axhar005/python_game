from src.Data import *

class Sand(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("sand", position, data.sprites["sand"])