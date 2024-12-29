from pyray import *
from src.Engine import Engine
from src.utils import *
from typing import NamedTuple

if __name__ == "__main__":
	engine: Engine = Engine()
	engine.loop()
	close_window()