grid = []
borderCoordinates = []

for _ in range(7):
	grid.append(["."] * 10)

for x in range(len(grid)):
	for y in range(len(grid[0])):
		if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1:
			grid[x][y] = "#"
			borderCoordinates.append((x,y))
				
print(borderCoordinates)