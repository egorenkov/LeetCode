class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def matr(i,j):
            return [[i + 1, j],
                    [i, j + 1]]
        grid = [[0 for j in range(n)] for i in range(m)]
        grid[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if i - 1 >= 0:
                    grid[i][j] += grid[i-1][j]
                if j - 1 >= 0:
                    grid[i][j] += grid[i][j-1]

        return grid[-1][-1]
