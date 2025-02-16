from src.Data import *

class Deep_dirt(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("deep_dirt", position, data.sprites["deep_dirt"])