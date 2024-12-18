'''
from __future__ import annotations

def hello_world() -> None:
	print("Hello world!")

class Vector:
	def __init__(self, x: int, y: int) -> None:
		self.x: int = x
		self.y: int = y
	def __add__(self, other: Vector) -> Vector:
		return Vector(self.x + other.x, self.y + other.y)
	def __sub__(self, other: Vector) -> Vector:
		return Vector(self.x - other.x, self.y - other.y)
'''