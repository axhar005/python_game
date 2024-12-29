from pyray import *
from src.Entity import *
from src.Player import *
from src.Block import *
from src.utils import *
from typing import Dict
from typing import List

class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Engine(metaclass=Singleton):
	
	def __init__(self) -> None:
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "PtiCraft")
		self.FPS = 60
		#set_target_fps(60)
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.tile_size = 32
		self.grid_size = 30
		self.mouse_pos: Vector2 = Vector2(0, 0)
		self.grid_width_px = self.grid_size * self.tile_size
		self.grid_height_px = self.grid_size * self.tile_size
		self.sprites: Dict[str, List[Texture]] = {}
		file: str = "assets/images"
		self.texture_path = {
			"player":		[f"{file}/player/32/player_down_0.png", f"{file}/player/32/player_down_1.png"],
			"dirt": 		[f"{file}/dirt/32/dirt_0.png"],
			"selector": 	[f"{file}/selector.png"],
			"grass":		[f"{file}/grass/32/grass_{i}.png" for i in range(16)],
			"water":		[f"{file}/water/32/water_{i}.png" for i in range(16)],
			"deep_dirt":	[f"{file}/deep_dirt/32/deep_dirt_{i}.png" for i in range(16)],
			"stone": 		[f"{file}/stone/stone_wall/32/stone_wall_{i}.png" for i in range(16)]
		}
		self.load_texure()
		self.objects: Dict[str, Entity] = {}
		self.objects["player"] = Player("player", Vector2(0, 0), self.sprites["player"])
		self.player = self.objects["player"]
		self.grid: List[List[Block]] = [
			[
				Block("grass", Vector2(row, col), self.sprites["grass"], 0)
				for col in range(self.grid_size)
			]
			for row in range(self.grid_size)
		]
		self.grid[0][0] = Block("water", Vector2(0, 0), self.sprites["water"], 0)
		auto_tiling_area(self.grid[int(self.grid_size/2)][int(self.grid_size/2)], self.grid_size, self.grid, self.grid_size)

	def load_texure(self) -> None:
		for key, paths in self.texture_path.items():
			self.sprites[key] = [load_texture(path) for path in paths]
			if key == "selector":
				print(f"Selector texture size: {self.sprites['selector'][0].width}x{self.sprites['selector'][0].height}")

	def render(self) -> None:
		grid_player_pos: Vector2 = Vector2(self.player.pos.x/self.tile_size, self.player.pos.y/self.tile_size)
		
		start_x = int(grid_player_pos.x - 14)
		end_x = int(grid_player_pos.x + 14)
		start_y = int(grid_player_pos.y - 9)
		end_y = int(grid_player_pos.y + 9)

		for row_index in range(start_x, end_x):
			for col_index in range(start_y, end_y):
				grid_x = row_index % self.grid_size
				grid_y = col_index % self.grid_size
				screen_x = row_index * self.tile_size
				screen_y = col_index * self.tile_size
				block = self.grid[grid_x][grid_y]
				draw_texture_ex(block.current_image, Vector2(screen_x, screen_y), 0, 1, WHITE)
				if (grid_x == self.mouse_pos.x and grid_y == self.mouse_pos.y):
					draw_texture_ex(self.sprites["selector"][0], Vector2(screen_x, screen_y), 0, 1, WHITE)
		draw_texture_ex(self.player.current_image, self.player.pos, 0, 1, WHITE)

	def draw(self) -> None:
		begin_mode_2d(self.cam)
		clear_background(GRAY)
		self.render()
		end_mode_2d()

	def draw_gui(self) -> None:
		draw_rectangle(5, 5, 200, 440, Color(0, 0, 0, 100))
		draw_fps(10, 20)
		t: Block = self.grid[int(self.mouse_pos.x)][int(self.mouse_pos.y)]
		draw_text(f"{t}", 10, 60, 20, WHITE)

	def game_step(self) -> None:
		# Player
		if (self.player.pos.x < 0):
			self.player.pos.x = self.grid_size * self.tile_size
		if (self.player.pos.x > self.grid_size * self.tile_size):
			self.player.pos.x = 0
		if (self.player.pos.y < 0):
			self.player.pos.y = self.grid_size * self.tile_size
		if (self.player.pos.y > self.grid_size * self.tile_size):
			self.player.pos.y = 0

		# Mouse
		mouse_screen_pos = get_mouse_position()
		mouse_world_pos = get_screen_to_world_2d(mouse_screen_pos, self.cam)
		self.mouse_pos.x = int(mouse_world_pos.x // self.tile_size) % self.grid_size
		self.mouse_pos.y = int(mouse_world_pos.y // self.tile_size) % self.grid_size
		if self.mouse_pos.x < 0:
			self.mouse_pos.x = self.grid_size + self.mouse_pos.x
		if self.mouse_pos.y < 0:
			self.mouse_pos.y = self.grid_size + self.mouse_pos.y
		if(is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)):
			block: Block = self.grid[int(self.mouse_pos.x)][int(self.mouse_pos.y)]
			if (block.name != "dirt"):
				self.grid[int(self.mouse_pos.x)][int(self.mouse_pos.y)] = Block("dirt", block.pos, self.sprites["dirt"], 2)
				auto_tiling_area(block, self.grid_size, self.grid, 3)	
			
		# Objects
		for obj in self.objects.values():
			obj.update()
			obj.step()
		
		# Cam
		self.cam.target = self.player.pos
	
	def loop(self) -> None:
		FRAME_DURATION = 1.0 / self.FPS
		time_accumulator = 0.0
		while not window_should_close():
			delat_time = get_frame_time()
			time_accumulator += delat_time

			while time_accumulator >= FRAME_DURATION:
				self.game_step()
				time_accumulator -= FRAME_DURATION

			begin_drawing()
			self.draw()
			self.draw_gui()
			end_drawing()

	def __str__(self) -> str:
		return f"{self}"