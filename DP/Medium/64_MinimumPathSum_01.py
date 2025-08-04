from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        @lru_cache(None)
        def make_recursion(i,j):

            if i==(no_of_rows-1) and j==(no_of_cols-1):
                return grid[i][j] 
            if i==(no_of_rows-1):
                return grid[i][j] + make_recursion(i,j+1)
            if j==(no_of_cols-1):
                return grid[i][j] + make_recursion(i+1,j)

            down = grid[i][j] + make_recursion(i+1,j)
            right = grid[i][j] + make_recursion(i,j+1) 

            result = min(down, right)
            return result

        return make_recursion(0,0)
        