class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if grid == []: return 0
        line, row = len(grid), len(grid[0])
        res = 0
        for l in range(line):
            for r in range(row):
                if grid[l][r] == '1':
                    grid[l][r] = '0'
                    self.counter(grid, l, r)
                    res += 1
        return res

    def get_neighbours(self, i, j):
        return [[i-1,j],
                [i, j-1],
                [i+1, j],
                [i, j+1]
               ]

    def counter(self, grid, x, y):
        neighbours = self.get_neighbours(x, y)
        for neighbour in neighbours:
            try:

                if neighbour[0] < 0 or neighbour[1] < 0 \
                    or neighbour[0] > len(grid)-1 \
                    or neighbour[1] > len(grid[0])-1:
                    continue

                if grid[neighbour[0]][neighbour[1]] == '1':
                    grid[neighbour[0]][neighbour[1]] = '0'

                    self.counter(grid, neighbour[0], neighbour[1])
            except IndexError:
                continue
                
