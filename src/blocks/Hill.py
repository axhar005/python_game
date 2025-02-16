from src.Data import *

class Hill(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("hill", position, data.sprites["hill"])