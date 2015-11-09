from objects import maze, town


class World (object):

	def __init__ (self, rooms, size, seed):

		self.seed = seed
		self.areas = self.generate(rooms, size, self.seed)

	def generate (self, rooms, size, seed):

		areas = []

		t = town.Town(str(0) + seed)
		m = maze.Maze(size + 2, size + 2, str(0) + seed)
		areas.append(t)
		areas.append(m)
		print(m.display_maze())

		for i in range(1, rooms):
			t = town.Town(str(i) + seed)
			t.add_shop()

			x = (size + 2) * (1 + i)
			y = (size + 2) * (i)
			m = maze.Maze(x, y, str(i) + seed)

			areas.append(t)
			areas.append(m)
			print(m.display_maze())

		return areas
