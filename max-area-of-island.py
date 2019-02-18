class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if grid == []: return 0
        # if grid == [[0]]: return 0
        # if grid == [[1]]: return 1
        line, row = len(grid), len(grid[0])
        res = 0
        areas = []
        for l in range(line):
            for r in range(row):
                area = 0
                if grid[l][r] == 1:
                    grid[l][r] = 0
                    area = 1
                    area = self.counter(grid, l, r, area)

                    res += 1
                areas.append(area)
        print(areas)
        return max(areas)

    def get_neighbours(self, i, j):
        return [[i-1,j],
                [i, j-1],
                [i+1, j],
                [i, j+1]
               ]

    def counter(self, grid, x, y, area):
        neighbours = self.get_neighbours(x, y)
        for neighbour in neighbours:
            try:

                if neighbour[0] < 0 or neighbour[1] < 0 \
                    or neighbour[0] > len(grid)-1 \
                    or neighbour[1] > len(grid[0])-1:
                    continue

                if grid[neighbour[0]][neighbour[1]] == 1:
                    grid[neighbour[0]][neighbour[1]] = 0
                    area += 1
                    area_ = self.counter(grid, neighbour[0], neighbour[1], 0)
                    area += area_
            except IndexError:
                continue
        print(area)
        return area
