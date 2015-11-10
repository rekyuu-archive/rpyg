from objects import mazes, towns


class World (object):

	def __init__ (self, rooms, size, seed):

		self.seed = seed
		self.areas = self.generate(rooms, size, self.seed)

	def generate (self, rooms, size, seed):

		areas = []

		t = towns.Town(str(0) + seed)
		m = mazes.Maze(size + 2, size + 2, str(0) + seed)
		areas.append(t)
		areas.append(m)
		print(m.display_maze())

		for i in range(1, rooms):
			t = towns.Town(str(i) + seed)
			t.add_shop()

			x = (size + 2) * (1 + i)
			y = (size + 2) * (i)
			m = mazes.Maze(x, y, str(i) + seed)

			areas.append(t)
			areas.append(m)
			print(m.display_maze())

		return areas
