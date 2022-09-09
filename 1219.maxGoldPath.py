class Solution(object):
    def gold(self, grid, i, j):
        t = 0
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0 or grid[i][j] in self.lst:
            return 0
        self.lst.append(grid[i][j])
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            value = self.gold(grid, x, y)
            t = max(t, value)

        return t + grid[i][j]

    def getMaximumGold(self, grid):
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.lst = []
                if grid[i][j] != 0:
                    m = self.gold(grid, i, j)
                    result = max(result, m)
        return result


obj = Solution()
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(obj.getMaximumGold(grid))
