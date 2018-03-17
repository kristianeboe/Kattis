def dfs(root, grid, explored, directions):
  region_size = 1
  fronteir = [root]
  while fronteir:
    node = fronteir.pop(0)
    for dire in directions:
        try:
          new_node = grid[node[0]+dire[0]][node[1]+dire[1]]
          new_coord = (node[0]+dire[0],node[1]+dire[1])
          if new_coord in explored:
            continue
          explored.add(new_coord)
          if new_node == 1:
            grid[node[0]+dire[0]][node[1]+dire[1]] = 'X'
            printGrid(grid)
            region_size += 1
            if new_coord not in fronteir or new_coord not in explored:
              fronteir.append(new_coord)
        except:
          pass
  return region_size

def printGrid(grid):
  for line in grid:
    print(''.join([str(x) for x in line]))
  print()

def getBiggestRegion(grid):
  # iterate through matrix to find roots
  # keep track of explored cooridinates
  # do a dfs to find size of region
  directions = [(0,1), (1,1),(1,0), (1,-1), (0,-1), (-1, -1), (-1, 0), (-1,1)]
  explored = set()
  largest_region = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      coord = (i, j)
      if coord in explored:
        continue
      explored.add(coord)
      node = grid[i][j]
      if node == 1:
        new_region = dfs(coord, grid, explored, directions)
        if new_region > largest_region:
          largest_region = new_region
  return largest_region
          
      

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
