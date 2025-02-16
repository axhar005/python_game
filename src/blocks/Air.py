from src.Data import *

class Air(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("air", position, None)