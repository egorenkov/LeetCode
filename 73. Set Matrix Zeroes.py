class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = []
        column = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)

        l = len(matrix[0])
        for k in row:
            for i in range(l):
                matrix[k][i] = 0
        
        r = len(matrix)
        for m in column:
            for i in range(r):
                matrix[i][m] = 0
