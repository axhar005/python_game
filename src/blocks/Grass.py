from src.Data import *

class Grass(Block):
	def __init__(self, position: Vector2, data: Data):
		super().__init__("grass", position, data.sprites["grass"])