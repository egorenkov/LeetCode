class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # matr = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]

        # n,m = len(grid) , len(grid[0])

        # for i in range(n):
        #     for j in range(m):
        #         matr[i][j] = grid[i][j]
        #         if i - 1 >= 0 and j - 1 >= 0:
        #             matr[i][j] += min(matr[i-1][j], matr[i][j-1])
        #         elif j - 1 >= 0:
        #             matr[i][j] += matr[i][j-1]
        #         elif i - 1 >=0:
        #             matr[i][j] += matr[i-1][j]

        #         else:
        #             pass
                

        # return matr[-1][-1]

        return solv(grid)

def solv(nums):

    n = len(nums) -1
    m = len(nums[0]) - 1
    INF = 10**10
    
    @cache
    def run(i,j):
        if i < 0 or j < 0: return INF
        if i == 0 and j == 0: return nums[i][j]
        
        return nums[i][j] + min(run(i-1, j), run(i,j-1))
       
    return run(n,m)    
        
