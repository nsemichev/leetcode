class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        
        max_row = []
        max_col = []
        for j in range(len(grid[0])):
            max_num = 0
            for i in range(len(grid)):
                if grid[i][j] > max_num:
                    max_num = grid[i][j]
            max_col.append(max_num)
        
        for i in range(len(grid)):
            max_row.append(max(grid[i]))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(max_row[i], max_col[j]) - grid[i][j]
        
        return total
