class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.vec2d = []
        for arr in matrix:
            temp = [0,arr[0]]
            for i in range(1,len(arr)):
                temp.append(temp[i] + arr[i])
            self.vec2d.append(temp)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in range(row1, row2 + 1):
            ans += (self.vec2d[i][col2+1] - self.vec2d[i][col1])
        return ans
