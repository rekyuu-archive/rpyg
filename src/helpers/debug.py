def mazegen (maze):

	width = len(maze[0])
	height = len(maze)

	x_border = [' ']
	for i in range(width):
		x_border.append('+---')
	x_border.append('+\n')
	x_border = ''.join(x_border)

	inner = []
	for row in maze:
		if row[0].entrance == True:
			inner.append('  ')
		else:
			inner.append(' |')
		for tile in row:
			if tile.wall_east == True:
				if tile.exit == True:
					inner.append('    ')
				else:
					inner.append('   |')
			else:
				inner.append('    ')
		inner.append('\n')
		inner.append(' +')
		for tile in row:
			if tile.wall_south == True:
				inner.append('---+')
			else:
				inner.append('   +')
		inner.append('\n')

	inner = ''.join(inner)

	return (
		x_border
		+ inner
	)
