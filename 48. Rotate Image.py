class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[i][j] = matrix[len(matrix) - j -1][i]

        matrix[:] = new_matrix
