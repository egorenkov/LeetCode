class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        row = len(triangle)
        if row == 1:
            return triangle[0][0]


        for i in range(1,row):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1,len(triangle[i]) -1):
                triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
            triangle[i][-1] += triangle[i-1][-1] 

        return min(triangle[-1])
